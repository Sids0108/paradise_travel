from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import frontpage
import login
import booking
import mysql.connector

def search():

    user = str(login.username.get())
    _id = str(booking.get())

    mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
    mycur = mydb.cursor()
    cust_det = "SELECT username,customer_id FROM customers WHERE username=%s"
    mycur.execute(cust_det,(user,))
    custlst = []
    final1 = mycur.fetchall()
    for q in final1:
        custlst.append(q)

    
    if (user,_id) not in custlst:
        messagebox.showerror('WARNING','The number you entered is not valid')
    else:
        mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
        mycur = mydb.cursor()
        cust_det1 = "SELECT * FROM customers WHERE customer_id=%s"
        mycur.execute(cust_det1,(_id,))
        custlst1 = []
        final2 = mycur.fetchall()
        for w in final2:
            custlst1.append(w)

        msg.destroy()
        booking_id.destroy()
        srch.destroy()
        back.destroy()
        booking.destroy()
    
        billfile = open("Bill.txt",'w')
        billfile.write("=============================================\n====================INVOICE==================\n=============================================\n")
        billfile.write("\nCustomer Number: \t")
        billfile.write(str(custlst1[0][1]))
        billfile.write("\nName:\t\t")
        billfile.write(str(custlst1[0][2]))
        billfile.write(" ")
        billfile.write(str(custlst1[0][3]))
        billfile.write("\nAddress: \t\t")
        billfile.write(str(custlst1[0][4]))
        billfile.write("\nPin Code: \t\t")
        billfile.write(str(custlst1[0][5]))
        billfile.write("\nPlace: \t\t")
        billfile.write(str(custlst1[0][6]))
        billfile.write("\nMail Id: \t\t")
        billfile.write(str(custlst1[0][7]))
        billfile.write("\nGender: \t\t")
        billfile.write(str(custlst1[0][8]))
        billfile.write("\nD.O.B: \t\t")
        billfile.write(str(custlst1[0][9]))
        billfile.write("\nID Type: \t\t")
        billfile.write(str(custlst1[0][10]))
        billfile.write("\nCheck-In Date:\t\t")
        billfile.write(str(custlst1[0][11]))
        billfile.write("\nNo. of days:\t\t")
        billfile.write(str(custlst1[0][12]))
        billfile.write("\nFood Type: \t\t")
        billfile.write(str(custlst1[0][13]))
        billfile.write("\nRoom Type: \t\t")
        billfile.write(str(custlst1[0][14]))
        billfile.write("\nVehicle Type: \t\t")
        billfile.write(str(custlst1[0][15]))
        billfile.write("\nNo of persons: \t\t")
        billfile.write(str(custlst1[0][16]))
        billfile.write("\n\n=============================================\n===============TAX & TOTAL===================")
        billfile.write("\n\nHotel Charge: \t\t\t\t")
        billfile.write(str(custlst1[0][17]))
        billfile.write("\nService Charge: \t\t\t\t")
        billfile.write(str(custlst1[0][18]))
        billfile.write("\nTransportation Charge: \t\t\t\t")
        billfile.write(str(custlst1[0][19]))
        billfile.write("\nSubTotal: \t\t\t\t")
        billfile.write(str(custlst1[0][20]))
        billfile.write("\nGST: \t\t\t\t")
        billfile.write(str(custlst1[0][21]))
        billfile.write("\n\nTOTAL: \t\t\t\t")
        billfile.write(str(custlst1[0][22]))
        billfile.write("\n\n============================================\n===============THANK YOU====================")
        billfile.close()

        file = open("Bill.txt")
        read = file.read()
        file.close()

        invoicetxt = Text(bookfrm,width=45,height=32)
        invoicetxt.place(x=70,y=5)

        invoicetxt.insert(1.0,read)
        invoicetxt.config(state=DISABLED)

        def Print():
            return

        def Save():
            txt = filedialog.asksaveasfilename(defaultextension=".*",title="INVOICE",filetypes=(("Text Files","*.txt"),("All Files","*.*")))
            txt = open(txt,'w')
            txt.write(read)
            txt.close()
            
        def Cancel():

            mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
            mycur = mydb.cursor()
            delquery = " DELETE FROM customers WHERE customer_id=%s"
            mycur.execute(delquery,(_id,))
            mydb.commit()
            
            messagebox.showwarning("CANCELLED","The booking has been cancelled")
            return frontpage.frontpage()


        pri = Button(bookfrm,text="PRINT",padx=60,pady=5,command=Print)
        save = Button(bookfrm,text="SAVE",padx=62,pady=5,command=Save)
        cancel = Button(bookfrm,text="CANCEL BOOKING",padx=25,pady=5,command=Cancel)
        out = Button(bookfrm,text="GO HOME",padx=48,pady=5,command=frontpage.frontpage)

        pri.place(x=485,y=150)
        save.place(x=485,y=200)
        cancel.place(x=485,y=250)
        out.place(x=485,y=300)
    
    
def status():

    frontpage.top.destroy()
    frontpage.middle.destroy()
    frontpage.bottom.destroy()

    global msg
    global booking_id
    global srch
    global back
    global bookfrm
    global booking

    booklbl = Label(text="MY BOOKINGS",relief=SOLID,width=69,height=2,font="arial 13 bold")
    booklbl.place(x=2,y=0)
    
    back = Button(booklbl,text="X",font="arial 10 bold",bg="red",command=frontpage.frontpage)
    back.place(x=670,y=5)

    bookfrm = LabelFrame(text="Bookings",height=555,width=698,relief=SOLID,font="arial 10 bold",bg="black")
    bookfrm.place(x=1,y=44)

    msg = Label(bookfrm,text="",font="arial 15 bold",relief=SOLID,height=4,width=47)
    msg.place(x=60,y=50)

    booking_id = Label(bookfrm,text="Booking Id",font="arial 13 bold")
    booking_id.place(x=100,y=230)
    booking = Entry(bookfrm,width=30)
    booking.place(x=220,y=235)
    srch = Button(bookfrm,text="SEARCH",font="arial 10 bold",padx=45,pady=5,command=search)
    srch.place(x=100,y=380)
    back = Button(bookfrm,text="BACK",font="arial 10 bold",padx=45,pady=5,command=frontpage.frontpage)
    back.place(x=300,y=380) 


