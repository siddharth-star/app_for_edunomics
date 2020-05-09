
"""
Created on 4 and 5,May 2020
Siddharth kajle
subject:Edunomics Assignment
=========  ===========   =============
"""
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import tkinter as tk
from tkinter import Message ,Text,messagebox
import cv2,os
import shutil
import csv
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
re=100
window = tk.Tk()
window.title("Edunomics                               .")

window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

path = "class2.png"
img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window, image = img )


panel.pack( side='left', fill='both', expand = 'yes')



txt = tk.Entry(window ,width=20 ,bg="yellow" ,fg="red",font=('times', 26, ' bold '))
txt.focus_set()
txt.place(x=100, y=215)


txt2 = tk.Entry(window,width=20  ,bg="yellow"  ,fg="red",font=('times', 26, ' bold ')  )
txt2.place(x=900, y=215)

message = tk.Label(window, text=": Notification :" ,bg="yellow"  ,fg="red"  ,width=35  ,height=3, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
message.place(x=700-re-120, y=500)

def number(s):
    c=0
    k=0
    l=[]
    t=[]
    for i in s:
        if i.isdigit():
            l.append(i)
            c=1
        elif i=='x' and c==1:
            l.append(i)
        elif i=='-' and c==1 and k!=1:
            l.append(i)
            k=1
        else:
            t.append(i)
            
    return ("".join(l),''.join(t))

def quit():
    messagebox.showinfo(title='Thankyou For using', message='Created by :\nSiddharth for Edunomics team')
    window.destroy()

def clear():
    txt.delete(0, 'end')    
    res = ""
    message.configure(text= res)

def clear2():
    txt2.delete(0, 'end')    
    res = ""
    message.configure(text= res)    
    
def company():
    name=txt.get()
    num,s=number(name)
    data = pd.read_csv('sku.csv')
    data2=pd.read_csv('new.csv')
    data["Distributor Item code"].fillna("Not Define", inplace = True) 
    dis=[]
    for i in range(len(data2['new'])):
        if (fuzz.WRatio(num,data2['Company Dscription'][i])>=95.0):
            if (fuzz.WRatio(s,data2['new'][i])>=95.0):
                dis.append([data['Distributor Item code'][i],data['Company Dscription'][i]])

    with open('distributor.txt', 'w') as file_handler:
        file_handler.write(f"Distributor with has name {name}\n")
        for item in dis:
            file_handler.write("{}\n".format(item))
    res = "See Distributor.txt file for result"
    message.configure(text= res)
    
    print(len(dis))

def distributor():
    name=txt2.get()
    data = pd.read_csv('sku.csv')
    data2=pd.read_csv('new.csv')
    data["Distributor Item code"].fillna("Not Define", inplace = True) 
    l=[]
    for i in range(len(data['Distributor Item code'])):
        if name==data['Distributor Item code'][i]:
            l.append((data['Distributor Item code'][i],data['Company Dscription'][i]))
    with open('company.txt', 'w') as file_handler:
        file_handler.write(f"Distributor deal with company {name}\n")
        for item in l:
            file_handler.write("{}\n".format(item))
    res = "See Company.txt file for result"
    message.configure(text= res)
    print(len(l))


clearButton = tk.Button(window, text="Search Distributor", command=company  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=160, y=280)
clearButton2 = tk.Button(window, text="Search Company", command=distributor  ,fg="red"  ,bg="yellow"  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton2.place(x=950+10, y=280)    

quitWindow = tk.Button(window, text="Quit", cursor='circle',command=quit  ,fg="red"  ,bg="yellow"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=700-re-50, y=650)




 
window.mainloop()