import tkinter
from tkinter import *
import tkinter.scrolledtext as st
import numpy as np
import datetime as dt
from time import strftime
window=Tk()
window.geometry("1980x1080")
window.configure(bg='light blue')

def time():
    string=strftime('%H:%M:%S %p')
    l7.config(text = string)
    l7.after(1000, time)

l7=Label(window,font= ('calibiri',12,"bold"))
l7.place(x=500,y=5)
time()
date= dt.datetime.now()
window.title("SMART NUMERIC ANALYSER")

l1 =Label(window,text="INPUT",fg="black",font=("times new roman",14,"bold")).place(x=140,y=40)
l2=Label(window,text="FILTER PROCESS",font=("times new roman",14,"bold")).place(x=420,y=310)
l3=Label(window,text="CUSTOM VALUES",font=("times new roman",14,"bold")).place(x=710,y=40)
l4=Label(window,text="OUTPUT",font=("times new roman",14,"bold")).place(x=1060,y=40)
l5=Label(window,text="FORMAT",font=("times new roman",14,"bold")).place(x=465,y=465)
l6=Label(window,text=f"{date:%A, %B %d, %Y}", font=("calibiri",12,"bold")).place(x=600,y=4.5)

e1=st.ScrolledText(window,width=40,height=35,bg='azure')
e1.place(x=10,y=70)

e2=Entry(window,width=18,relief="solid",bg='azure',font=("ariel",20))
e2.place(x=370,y=350)

e3=st.ScrolledText(window,width=30,height=15,bg='azure')
e3.place(x=670,y=70)

e4=st.ScrolledText(window,width=30,height=15,bg='azure')
e4.place(x=670,y=390)

e5=st.ScrolledText(window,width=35,height=35,bg='azure')
e5.place(x=950,y=70)

e6=Entry(window,width=18,relief="solid",bg='azure',font=("ariel",20))
e6.place(x=370,y=500)

def start():
    list=[]
    dict={}
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data=e1.selection_get()
        for i in data.split("."):
            if(': ') in i:

                index=i.find(': ')
                sp=i[index+2:]
                list.append(sp)
            else:
                list.append(i)

    for k in range(0,len(list)-1):
        e3.insert(tkinter.END,list[k])
        e3.insert(tkinter.END,'\n')

def process():
    list = []
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data = e1.selection_get()
        for i in data.split("."):
            if (': ') in i:

                index = i.find(': ')
                sp = i[index + 2:]
                list.append(sp)
            elif ('-') in i:
                for j in i.split("-"):
                    sa = j[::]
                    list.append(sa)
            else:
                list.append(i)


    y=np.unique(list)
    q=[]
    for i in y:
        if i in list:
            q.append(list.count(i))
    w=1
    for j in range(1,len(y)):
        x=q[w]
        e4.insert(tkinter.END,y[j])
        e4.insert(tkinter.END,"(")
        e4.insert(tkinter.END,x)
        e4.insert(tkinter.END,")")
        e4.insert(tkinter.END,'\n')
        w=w+1

def reset1():
    e1.delete("1.0","end")
    e3.delete("1.0","end")
    e4.delete("1.0","end")
    e5.delete("1.0","end")

def filter():
    b=int(e2.get())
    list = []
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data = e1.selection_get()
        for i in data.split("\n"):
            index = i.find(': ')
            sp = i[index + 2:index + 5]
            list.append(sp)
    y = np.unique(list)
    q = []
    for i in y:
        if i in list:
            q.append(list.count(i))
    w = 1
    for j in range(1, len(y)):
        x = q[w]-b
        e5.insert(tkinter.END, y[j])
        e5.insert(tkinter.END, "(")
        e5.insert(tkinter.END,x )
        e5.insert(tkinter.END, ")")
        e5.insert(tkinter.END, "      ")
        e5.insert(tkinter.END,y[j])
        e5.insert(tkinter.END, '\n')
        w = w + 1

def reset2():
    e5.delete("1.0",END)

b1=Button(window,text="START",width=10,fg='red',bg='white',relief="solid",font=("times new roman",20,"bold"),command=start)
b1.place(x=420,y=70)

b2=Button(window,text="PROCESS",width=10,fg='red',bg='white',relief="solid",font=("times new roman",20,"bold"),command=process)
b2.place(x=420,y=140)

b3=Button(window,text="RESET",width=10,fg='red',bg='white',relief="solid",font=("times new roman",20,"bold"),command=reset1)
b3.place(x=420,y=210)

b4=Button(window,text="FILTER",width=8,fg='red',bg='white',relief="solid",font=("times new roman",14,"bold"),command=filter)
b4.place(x=385,y=400)

b5=Button(window,text="RESET",width=8,fg='red',bg='white',relief="solid",font=("times new roman",14,"bold"),command=reset2)
b5.place(x=530,y=400)

b6=Button(window,text="ENTER",width=8,fg='red',bg='white',relief="solid",font=("times new roman",14,"bold"))
b6.place(x=465,y=550)

window.mainloop()