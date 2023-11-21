from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup as bs



mf = open("GetPars3.txt", "w",  encoding="utf-8")
give = []
pgNum = 17
for ttt in range(pgNum):
    URL_TEMPLATE = "https://remi.ru/news/?PAGEN_1=" + str(ttt + 1)
    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, "html.parser")
    div_names = soup.find_all('div', class_='news__item__header')
    for name in div_names:
        ass = name.a
        if "цена" in ass.text:
            url_more = ass.get('href')
            URL_TEMPLATE1 = "https://remi.ru" + url_more
            print(URL_TEMPLATE1)
            r1 = requests.get(URL_TEMPLATE1)
            soup1 = bs(r1.text, "html.parser")
            per = soup1.find_all('div', class_='news-detail')
            for names in per:
                strr = names.find_all('p')
                dvss = names.find_all('div')
                spns = names.find_all('span')
                for tftf in strr:
                    vau = tftf.text
                    if "✓" in vau:
                        give.append(vau)
                for ttf in dvss:
                    viu = ttf.text
                    if "✓" in viu:
                        give.append(viu)
                for pps in spns:
                    vsp = pps.text
                    if "✓" in vsp:
                        give.append(vsp)

for el in give:
    mf.write(str(el))
    mf.write('\n')

mf.close()
with open('GetPars3.txt', encoding='utf-8') as f:
    lines = f.readlines()
    non_empty_lines = (line for line in lines if not line.isspace())
    newnew = list(non_empty_lines)
    with open('finish.txt', 'w', encoding='utf-8') as n_f:
        for i in range(len(newnew)):
            if "✓" in newnew[i]:
                n_f.writelines(newnew[i])

def open_txt():
    txt = open('finish.txt', 'r', encoding='utf-8')
    txt = ''.join(txt)
    text = ttk.Label(text=txt,font='20',background='#eff1f4')
    text.pack()
    button.destroy()



root = Tk()
root.title('remi')
root.geometry('1000x870+550+50')
root.resizable(False,False)
frame = Frame(root)
frame['bg']='#eff1f4'
frame.place(relheight=1,relwidth=1)
button = Button(frame, text="Начать", command=open_txt, width=30,height=7, font=40,background='#8eb1e6')
button.pack(expand=True)

root.mainloop()