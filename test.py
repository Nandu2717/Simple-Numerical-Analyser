import tkinter
from tkinter import *
import tkinter.scrolledtext as st
import numpy as np
window=Tk()
window.geometry("1980x1080")
window.title("SMART NUMERIC ANALYSER")


l1 = Label(window,text="INPUT",fg="black",font=("times new roman",20,"bold")).place(x=130,y=30)
l2=Label(window,text="Filter Process",font=("times new roman",22,"bold")).place(x=445,y=300)
l3=Label(window,text="CUSTOM VALUES",font=("times new roman",20,"bold")).place(x=725,y=30)
l4=Label(window,text="OUTPUT",font=("times new roman",20,"bold")).place(x=1130,y=30)
l5=Label(window,text="FORMAT",font=("times new roman",20,"bold")).place(x=465,y=450)

e1=st.ScrolledText(window,width=45,height=45,bg='white')
e1.place(x=10,y=70)

e2=Entry(window,width=18,relief="solid",bg='white',font=("ariel",20))
e2.place(x=385,y=350)

e3=st.ScrolledText(window,width=40,height=20,bg='white')
e3.place(x=670,y=70)

e4=st.ScrolledText(window,width=40,height=20,bg='white')
e4.place(x=670,y=395)

e5=st.ScrolledText(window,width=45,height=45,bg='white')
e5.place(x=1000,y=70)

e6=Text(window,height=1.3,width=18,relief="solid",bg='white',font=("ariel",20))
e6.place(x=385,y=500)


def start():
    list=[]
    name_list=[]
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data=e1.selection_get()
        for i in data.split("\n"):
            index=i.find(': ')
            sp=i[index+2:index+5]
            name=i[16:index]
            name_list.append(name)
            list.append(sp)
    for k in list:
        e3.insert(tkinter.END,k)
        e3.insert(tkinter.END,'\n')

def process():
    list = []
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data = e1.selection_get()
        for i in data.split("\n"):
            sp = i[-3:]
            list.append(sp)
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
            sp = i[-3:]
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

def enter():
    name_list = []
    list = []
    e1.tag_add("sel", "1.0", "end")
    e1.tag_config("sel", background="grey")
    if e1.selection_get():
        data = e1.selection_get()
        for i in data.split("\n"):
            index = i.find(': ')
            name = i[16:index]
            name_list.append(name)
            sp = i[index + 2: index + 5]
            list.append(sp)
    y = np.unique(list)
    x = 1
    for i in range(1,len(y)):
        n = name_list[x]
        e5.insert(tkinter.END,n)
        e5.insert(tkinter.END," : ")
        e5.insert(tkinter.END,y[i])
        e5.insert(tkinter.END, '\n')
        x=x+1





b1=Button(window,text="START",width=10,fg='orange',bg='white',relief="solid",font=("times new roman",30,"bold"),command=start)
b1.place(x=415,y=70)


b2=Button(window,text="PROCESS",width=10,fg='orange',bg='white',relief="solid",font=("times new roman",30,"bold"),command=process)
b2.place(x=415,y=140)

b3=Button(window,text="RESET",width=10,fg='orange',bg='white',relief="solid",font=("times new roman",30,"bold"),command=reset1)
b3.place(x=415,y=210)

b4=Button(window,text="FILTER",width=5,fg='orange',bg='white',relief="solid",font=("times new roman",17,"bold"),command=filter)
b4.place(x=385,y=390)

b5=Button(window,text="RESET",width=5,fg='orange',bg='white',relief="solid",font=("times new roman",17,"bold"),command=reset2)
b5.place(x=545,y=390)

b6=Button(window,text="ENTER",width=5,fg='orange',bg='white',relief="solid",font=("times new roman",17,"bold"),command=enter)
b6.place(x=470,y=550)














window.mainloop()
