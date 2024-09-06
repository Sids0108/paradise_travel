from tkinter import *
from tkinter import ttk 
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
import frontpage
import booking

def out():
    booking_Id = (str(booking.cn),)

    mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
    mycur = mydb.cursor()
    delquery = " DELETE FROM customers WHERE customer_id=%s"
    ans = booking_Id
    mycur.execute(delquery,ans)
    mydb.commit()
    
    messagebox.showwarning("CANCELLED","The payment has been cancelled")
    return frontpage.frontpage()

def confirm():

    cno = card_no.get()
    if len(cno)==16:
        messagebox.showinfo("SUCCESSFUL","Successfully BOOKED")
        frontpage.frontpage()
    else:
        messagebox.showwarning("WARNING","Invalid Card Number")

def Pay():

    global card_no
    global month
    global year
    global c
    global c1
    global c2

    booking.bookingfrm.destroy()
    
    paymentfrm = LabelFrame(height=555,width=698,relief=SOLID,font="arial 10 bold",bg="black")
    paymentfrm.place(x=1,y=46)

    c = ImageTk.PhotoImage(Image.open("photos/c1.png"))
    cp = Label(paymentfrm,image=c)
    cp.place(x=150,y=80)

    c1 = ImageTk.PhotoImage(Image.open("photos/c2.png"))
    cp1 = Label(paymentfrm,image=c1)
    cp1.place(x=250,y=80)

    c2 = ImageTk.PhotoImage(Image.open("photos/c3.png"))
    cp2 = Label(paymentfrm,image=c2)
    cp2.place(x=350,y=80)

    card_type_lbl = Label(paymentfrm,text="Card Type",font="arial 14")
    card_type_lbl.place(x=50,y=50)

    var = IntVar()
    var1 = IntVar()

    month = ttk.Combobox(paymentfrm,width=10,textvariable=var)
    month['values'] = ('01','02','03','04','05','06','07','08','09','10','11','12') 
    month.place(x=100,y=290)

    year = ttk.Combobox(paymentfrm,width=10,textvariable=var1)
    year['values'] = ('2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030') 
    year.place(x=300,y=290)
    
    card_no_lbl = Label(paymentfrm,text="Card Number",font="arial 13")
    expiry_lbl = Label(paymentfrm,text="Expiry",font="arial 13")
    month_lbl = Label(paymentfrm,text="Month",font="arial 11")
    year_lbl = Label(paymentfrm,text="Year",font="arial 11")
    cvv_lbl = Label(paymentfrm,text="CVV",font="arial 13")
    card_name_lbl = Label(paymentfrm,text="Card Name",font="arial 13")

    card_no_lbl.place(x=50,y=150)
    expiry_lbl.place(x=50,y=250)
    month_lbl.place(x=50,y=290)
    year_lbl.place(x=250,y=290)
    cvv_lbl.place(x=50,y=350)
    card_name_lbl.place(x=50,y=450)


    card_no = Entry(paymentfrm,width=55)
    card_no.place(x=50,y=185)

    card_name = Entry(paymentfrm,width=55)
    card_name.place(x=50,y=485)

    cvv = Entry(paymentfrm,width=10,show="*")
    cvv.place(x=50,y=385)

    pay = Button(paymentfrm,text="PAY",padx=40,pady=5,command=confirm)
    pay.place(x=450,y=500)

    CANCEL = Button(paymentfrm,text="CANCEL",padx=25,pady=5,command=out)
    CANCEL.place(x=570,y=500)

    
    
    
    
    
