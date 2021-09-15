import requests
from bs4 import BeautifulSoup
from plyer import notification
import time
from tkinter import *
from tkinter.messagebox import showinfo
def compte():
     c=requests.get("http://123.orange.mg/InfoConso")
     c1=BeautifulSoup(c.text,"html.parser")
     dc=c1.find_all("div",class_="infoConsoItemTitle")
     notification.notify(title="infoOrange",message=str(dc[1].text.strip()))

def plan():
     p=requests.get("http://123.orange.mg/InfoConso")
     p1=BeautifulSoup(p.text,"html.parser")
     dp=p1.find_all("div",class_="infoConsoItemTitle")
     notification.notify(title="infoOrange",message=str(dp[0].text.strip()))


n=requests.get("http://123.orange.mg/Accueil")
n1=BeautifulSoup(n.text,"html.parser")
dn=n1.find_all("span")
message=str(dn[0].text.strip()) 


def i():
     showinfo("info","merci d'avoir choisi cette apk \n ceci est un apk pour faciliter \n votre demande info conso orange\n reporter votre probleme a \n Cael'v Rajaofalia ")

f=Tk()
f.title("info conso")
f.resizable(False,False)
f.iconbitmap('logo.ico')
f.geometry("280x150")
pres=Label(f,text="service info conso Orange", font=("arial",16,"bold"))
pres.grid(row=0,column=0)
bc=Button(f,text="compte principal",bg="black",fg="orange",command=compte)
bc.grid(row=1,column=0)
bp=Button(f,text="plan tarifaire",bg="black",fg="orange",command=plan)
bp.grid(row=2,column=0)
n=Label(f,text=message,font=("arial",16,"bold"))
n.place(x=00,y=100)
i=Button(f,text="i",command=i,font=("arial",20,"bold"))
i.place(x=250,y=100)
f.mainloop()