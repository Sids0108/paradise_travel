from tkinter import *
import frontpage
import login
from tkinter import ttk

def contact():
    frontpage.top.destroy()
    frontpage.middle.destroy()
    frontpage.bottom.destroy()

    with open('CS.txt','r') as cs:
        r = cs.read()

    abtlbl = Label(text="ABOUT & CONTACT US",relief=SOLID,width=69,height=2,font="arial 13 bold")
    abtlbl.place(x=2,y=0)

    back = Button(abtlbl,text="X",font="arial 10 bold",command=frontpage.frontpage,bg="red")
    back.place(x=670,y=5)

    abtus = LabelFrame(text="About Us",height=276,width=698,relief=SOLID,font="arial 10 bold",fg="white",bg="black")
    abtus.place(x=1,y=44)

    contactfrm =  LabelFrame(text="Contact",height=279,width=698,relief=SOLID,font="arial 8 bold",fg="white",bg="black")
    contactfrm.place(x=1,y=320)

    abtdisplay = Text(abtus,height=15,width=86)
    abtdisplay.place(x=1,y=1)

    abtdisplay.insert(1.0,r)
    abtdisplay.config(state=DISABLED)

    table = ttk.Treeview(contactfrm,height=5,show="headings")
    table.place(x=50,y=50)

    table['columns'] = ('OFFICIALS','PHONE NUMBER','EMAIL')

    table.column('OFFICIALS',width=180,anchor=CENTER)
    table.column('PHONE NUMBER',width=200,anchor=CENTER)
    table.column('EMAIL',width=200,anchor=CENTER)

    table.heading('OFFICIALS',text="OFFICALS")
    table.heading('PHONE NUMBER',text="PHONE NUMBER")
    table.heading('EMAIL',text="EMAIL")

    officials = [' ','Siddharth.S.Swamy','Abhishek.S','Debasish Nayak']
    phnno = [' ','+91 989420 2251','+91 75502 61248','+91 80724 43776']
    mail = [' ','siddharthsswamy2003@gmail.com','abhisheksairam0@gmail.com','debasishnayak1104@gmail.com']

    for val in range(4):
        table.insert('',val,values=(officials[val],phnno[val],mail[val]))

    
