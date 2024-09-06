from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from datetime import datetime
import mysql.connector
import frontpage
import login
import Clear
import Pay
import random
import math

cn = random.randint(111111,999999)+100000

Hotel_Charge_amt = 600
Service_Charge_amt = 150

hatchback = 800
sadan = 1200
suv = 1800
tempo = 2500



def select():
    newtk = Tk()
    newtk.title("Check-In Date")
    cal = Calendar(newtk,selectmode="day",year=2020,month=11,day=21)
    cal.pack()
    def done():
        check_In.config(text=cal.get_date(),font="arial 11")
        newtk.destroy()
    b = Button(newtk,text="OK",command=done)
    b.pack()

def Total():

    a = cn
    print(cn)
    b = first_name.get()
    c = last_name.get()
    d = address.get()
    e = pincode.get()
    f = email.get()
    g = gender.get()
    h = dob.get()
    i = id_type.get()
    j = check_In['text']
    k = check_out.get()
    l = food.get()
    m = room_type.get()
    n = vehicle_type.get()
    o = noppl.get()
    p = place.get()

    lst = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]

    now = datetime.now()
    date = now.strftime('%x')

    for l in range(15):
        if lst[l]=="":
            messagebox.showerror('WARNING','No Entry can be left empty')
            break
    else:
        
        billtxt.config(state=NORMAL)
        billtxt.delete(1.0,END)

        transprtation_amt = int()
        
        trans = vehicle_type.get()

        if trans == "None":
            transprtation_amt+=0
        elif trans == "Hatchback":
            transprtation_amt+=(int(hatchback)*int(check_out.get()))
        elif trans == "Sedan":
            transprtation_amt+=(int(sadan)*int(check_out.get()))
        elif trans == "SUV":
            transprtation_amt+=(int(suv)*int(check_out.get()))
        elif trans == "Tempo":
            transprtation_amt+=(int(tempo)*int(check_out.get()))

        hotel_amt = int(Hotel_Charge_amt)*int(check_out.get())*int(noppl.get())
        service_amt = int(Service_Charge_amt)*int(check_out.get())
        subtotal_amt = (hotel_amt)+(service_amt)+(transprtation_amt)
        gst_amt = subtotal_amt*18/100
        total_amt = (subtotal_amt) + (gst_amt)

        billfile = open("Bill.txt",'w')
        billfile.write("=============================================\n====================INVOICE==================\n=============================================\n")
        billfile.write("\nCustomer Number: \t")
        billfile.write(str(cn))
        billfile.write("\nName:\t\t")
        billfile.write(str(first_name.get().capitalize()))
        billfile.write(" ")
        billfile.write(last_name.get())
        billfile.write("\nAddress: \t\t")
        billfile.write(str(address.get()))
        billfile.write("\nPin Code: \t\t")
        billfile.write(str(pincode.get()))
        billfile.write("\nPlace: \t\t")
        billfile.write(str(place.get()))
        billfile.write("\nMail Id: \t\t")
        billfile.write(str(email.get()))
        billfile.write("\nGender: \t\t")
        billfile.write(str(gender.get()))
        billfile.write("\nD.O.B: \t\t")
        billfile.write(str(dob.get()))
        billfile.write("\nID Type: \t\t")
        billfile.write(str(id_type.get()))
        billfile.write("\nCheck-In Date:\t\t")
        billfile.write(str(check_In['text']))
        billfile.write("\nNo. of days:\t\t")
        billfile.write(str(check_out.get()))
        billfile.write("\nFood Type: \t\t")
        billfile.write(str(food.get()))
        billfile.write("\nRoom Type: \t\t")
        billfile.write(str(room_type.get()))
        billfile.write("\nVehicle Type: \t\t")
        billfile.write(str(vehicle_type.get()))
        billfile.write("\nNo of persons: \t\t")
        billfile.write(str(noppl.get()))
        billfile.write("\n\n=============================================\n===============TAX & TOTAL===================")
        billfile.write("\n\nHotel Charge: \t\t\t\t")
        billfile.write(str(hotel_amt))
        billfile.write("\nService Charge: \t\t\t\t")
        billfile.write(str(service_amt))
        billfile.write("\nTransportation Charge: \t\t\t\t")
        billfile.write(str(transprtation_amt))
        billfile.write("\nSubTotal: \t\t\t\t")
        billfile.write(str(subtotal_amt))
        billfile.write("\nGST: \t\t\t\t")
        billfile.write(str(gst_amt))
        billfile.write("\n\nTOTAL: \t\t\t\t")
        billfile.write(str(total_amt))
        billfile.write("\n\n============================================\n===============THANK YOU====================")
        billfile.close()

        file = open("Bill.txt")
        read = file.read()
        file.close()

        mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
        mycur = mydb.cursor()
#        mycur.execute("CREATE TABLE customers (username VARCHAR(100),customer_id VARCHAR(50),first_name VARCHAR(100),last_name VARCHAR(100),address VARCHAR(100),pincode VARCHAR(100),places VARCHAR(100),email VARCHAR(100),gender VARCHAR(100),dob VARCHAR(100),id_type VARCHAR(100),check_In VARCHAR(100),check_out VARCHAR(100),food VARCHAR(100),room_type VARCHAR(100),vehicle_type VARCHAR(100),noppl VARCHAR(100),hotel_amt VARCHAR(100),service_amt VARCHAR(100),transprtation_amt VARCHAR(100),subtotal_amt VARCHAR(100),gst_amt VARCHAR(100),total_amt VARCHAR(100))")
        sq = ("INSERT INTO customers (username,customer_id,first_name,last_name,address,pincode,places,email,gender,dob,id_type,check_In,check_out,food,room_type,vehicle_type,noppl,hotel_amt,service_amt,transprtation_amt,subtotal_amt,gst_amt,total_amt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val = (login.username.get(),a,b,c,d,e,p,f,g,h,i,j,k,l,m,n,o,str(hotel_amt),str(service_amt),str(transprtation_amt),str(subtotal_amt),str(gst_amt),str(total_amt))
        mycur.execute(sq,val)
        mydb.commit()
        
        billtxt.insert(1.0,read)
        billtxt.config(state=DISABLED)

#        first_name.delete(0,END)
#        last_name.delete(0,END)
#        address.delete(0,END)
#        pincode.delete(0,END)
#        place.delete(0,END)
#        email.delete(0,END)
#        gender.delete(0,END)
#        dob.delete(0,END)
#        id_type.delete(0,END)
#        food.delete(0,END)
#        room_type.delete(0,END)
#        vehicle_type.delete(0,END)
#        noppl.delete(0,END)
#        check_out.delete(0,END)

        cid = Button(bookingfrm,text="",state=DISABLED)
        cid.place(x=280,y=291)

        first_name.config(state=DISABLED)
        last_name.config(state=DISABLED)
        address.config(state=DISABLED)
        pincode.config(state=DISABLED)
        place.config(state=DISABLED)
        email.config(state=DISABLED)
        gender.config(state=DISABLED)
        dob.config(state=DISABLED)
        id_type.config(state=DISABLED)
        check_In.config(state=DISABLED)
        check_out.config(state=DISABLED)
        food.config(state=DISABLED)
        room_type.config(state=DISABLED)
        vehicle_type.config(state=DISABLED)
        noppl.config(state=DISABLED)

        total = Button(bookingfrm,text="Total",font="arial 10 bold",padx=26,pady=4,state=DISABLED)
        total.place(x=10,y=490)
        payment = Button(bookingfrm,text="Pay",font="arial 10 bold",padx=30,pady=4,command=Pay.Pay)
        payment.place(x=105,y=490)
        cancel = Button(bookingfrm,text="Edit",font="arial 10 bold",padx=25,pady=4,command=edit)
        cancel.place(x=200,y=490)


def edit():
        first_name.config(state=NORMAL)
        last_name.config(state=NORMAL)
        address.config(state=NORMAL)
        pincode.config(state=NORMAL)
        place.config(state=NORMAL)
        email.config(state=NORMAL)
        gender.config(state=NORMAL)
        dob.config(state=NORMAL)
        id_type.config(state=NORMAL)
        check_In.config(state=NORMAL)
        check_out.config(state=NORMAL)
        food.config(state=NORMAL)
        room_type.config(state=NORMAL)
        vehicle_type.config(state=NORMAL)
        noppl.config(state=NORMAL)

        total1 = Button(bookingfrm,text="Total",font="arial 10 bold",padx=26,pady=4,command=Total)
        total1.place(x=10,y=490)
        payment = Button(bookingfrm,text="Pay",font="arial 10 bold",padx=30,pady=4,state=DISABLED)
        payment.place(x=105,y=490)
        cid = Button(bookingfrm,text="",command=select)
        cid.place(x=280,y=291)
        cancel = Button(bookingfrm,text="Edit",font="arial 10 bold",padx=25,pady=4,state=DISABLED)
        cancel.place(x=200,y=490)

    


def booking():

    global bookingfrm
    global billtxt

    global first_name
    global last_name
    global address
    global pincode
    global place
    global email
    global gender
    global dob
    global id_type
    global check_In
    global check_out
    global food
    global room_type
    global vehicle_type
    global noppl    

    frontpage.top.destroy()
    frontpage.middle.destroy()
    frontpage.bottom.destroy()

    booknowlbl = Label(text="BOOK NOW",relief=SOLID,width=69,height=2,font="arial 13 bold")
    booknowlbl.place(x=2,y=0)

    back = Button(booknowlbl,text="X",font="arial 10 bold",bg="red",command=frontpage.frontpage)
    back.place(x=670,y=5)
    
    bookingfrm = LabelFrame(height=555,width=698,relief=SOLID,font="arial 10 bold",bg="black")
    bookingfrm.place(x=1,y=46)

    var = StringVar()
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    var4 = StringVar()

    id_type = ttk.Combobox(bookingfrm,width=22,textvariable=var)
    id_type['values'] = ("Aadhar Card","PAN Card","Passport",'Birth Certificate','Ration Card') 

    vehicle_type = ttk.Combobox(bookingfrm,width=22,textvariable=var1)
    vehicle_type['values'] = ("None","Hatchback","Sedan","SUV","Tempo")

    food = ttk.Combobox(bookingfrm,width=22,textvariable=var2)
    food['values'] = ('Veg','Non-Veg')

    gender = ttk.Combobox(bookingfrm,width=22,textvariable=var3)
    gender['values'] = ('Male','Female')

    place = ttk.Combobox(bookingfrm,width=22,textvariable=var4)
    place['values'] = ('Ooty','Kodaikanal','Nanital','Munnar','Dehradun')
    
    first_namelbl = Label(bookingfrm,text="First Name",font="arial 10 bold")
    last_namelbl = Label(bookingfrm,text="Last Name",font="arial 10 bold")
    addresslbl = Label(bookingfrm,text="Address",font="arial 10 bold")
    pincodelbl = Label(bookingfrm,text="Pin Code",font="arial 10 bold")
    placelbl = Label(bookingfrm,text="Place to Visit",font="arial 10 bold")
    emaillbl = Label(bookingfrm,text="Mail Id",font="arial 10 bold")
    genderlbl = Label(bookingfrm,text="Gender",font="arial 10 bold")
    doblbl = Label(bookingfrm,text="D.O.B",font="arial 10 bold")
    id_typelbl = Label(bookingfrm,text="ID Type",font="arial 10 bold")
    check_Inlbl = Label(bookingfrm,text="Check-In Date",font="arial 10 bold")
    check_outlbl = Label(bookingfrm,text="No. of Days",font="arial 10 bold")
    foodlbl = Label(bookingfrm,text="Food Type",font="arial 10 bold")
    room_typelbl = Label(bookingfrm,text="Room Type",font="arial 10 bold")
    vehicle_typelbl = Label(bookingfrm,text="Vehicle Type",font="arial 10 bold")
    noppllbl = Label(bookingfrm,text="No.of persons",font="arial 10 bold")

    first_namelbl.place(x=10,y=20)
    last_namelbl.place(x=10,y=50)
    addresslbl.place(x=10,y=80)
    pincodelbl.place(x=10,y=110)
    placelbl.place(x=10,y=140)
    emaillbl.place(x=10,y=170)
    genderlbl.place(x=10,y=200)
    doblbl.place(x=10,y=230)
    id_typelbl.place(x=10,y=260)
    check_Inlbl.place(x=10,y=290)
    check_outlbl.place(x=10,y=320)
    foodlbl.place(x=10,y=350)
    room_typelbl.place(x=10,y=380)
    vehicle_typelbl.place(x=10,y=410)
    noppllbl.place(x=10,y=440)

    customer_no = Label(bookingfrm,text=str(cn),width=25)
    first_name = Entry(bookingfrm,width=25)
    last_name = Entry(bookingfrm,width=25)
    address = Entry(bookingfrm,width=25)
    pincode = Entry(bookingfrm,width=25)
    email = Entry(bookingfrm,width=25)
    
    dob = Entry(bookingfrm,width=25)
    check_In = Label(bookingfrm)
    check_out = Entry(bookingfrm,width=25)
    room_type = Entry(bookingfrm,width=25)
    noppl = Entry(bookingfrm,width=25)

    first_name.place(x=135,y=22)
    last_name.place(x=135,y=52)
    address.place(x=135,y=82)
    pincode.place(x=135,y=112)
    place.place(x=135,y=142)
    email.place(x=135,y=172)
    gender.place(x=135,y=202)
    dob.place(x=135,y=232)
    id_type.place(x=135,y=262)
    check_In.place(x=135,y=292)
    check_out.place(x=135,y=322)
    food.place(x=135,y=352)
    room_type.place(x=135,y=382)
    vehicle_type.place(x=135,y=412)
    noppl.place(x=135,y=442)

    cid = Button(bookingfrm,text="",command=select)
    cid.place(x=280,y=291)

    billtxt = Text(bookingfrm,width=45,height=33)
    billtxt.place(x=310,y=10)

    total = Button(bookingfrm,text="Total",font="arial 10 bold",padx=26,pady=4,command=Total)
    total.place(x=10,y=490)
    payment = Button(bookingfrm,text="Pay",font="arial 10 bold",padx=30,pady=4,state=DISABLED)
    payment.place(x=105,y=490)
    cancel = Button(bookingfrm,text="Edit",font="arial 10 bold",padx=25,pady=4,state=DISABLED)
    cancel.place(x=200,y=490)

    file = open("Bill1.txt")
    read = file.read()
    file.close()

    billtxt.insert(1.0,read)
    billtxt.config(state=DISABLED)
    
