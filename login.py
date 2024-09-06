from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import frontpage
import mysql.connector
import smtplib
import random
import math
import re
root = Tk()
root.geometry("700x600+300+20")
root.title("PARADISE TRAVEL")
root.resizable(False,False)

mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
mycur = mydb.cursor()
#mycur.execute("CREATE TABLE signin (fname CHAR(100), lname CHAR(100),mobno VARCHAR(10), dob VARCHAR(20), mail VARCHAR(100), pw VARCHAR(10))")
mydb.commit()

def login1():

#     frontpage.frontpage()
    
    global username1
    global password1
    
    username1 = str(username.get())
    password1 = str(password.get())
    
    mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
    mycur = mydb.cursor()
    sqlcheck = "SELECT mail,pw FROM signin WHERE mail=%s and pw=%s"
    mycur.execute(sqlcheck,(username1,password1))
    search = []
    result = mycur.fetchall()
    for check in result:
        search.append(check)
    if username1=="" or password1=="":
        emptyerror = messagebox.showerror("ERROR","Enteries are left free") 
    elif len(search)==0:
        pwerror = messagebox.showerror("ERROR","Invalid password!")       
    else:
        frontpage.frontpage()

def logup():

    global fname1
    global lname1
    global mobno1
    global dob1
    global mail1
    global pw1

    fname1 = str(fname.get())
    lname1 = str(lname.get())
    mobno1 = str(mobno.get())
    dob1 = str(dob.get())
    mail1 = str(username.get())
    pw1 = str(pw.get())

    signupdetails = (fname1,lname1,mobno1,dob1,mail1,pw1)

    for i in range(6):
        if signupdetails[i] == "":
            blankerror = messagebox.showerror("ERROR","No Entry can be left empty")
            break
    if len(signupdetails[5])<8 or len(signupdetails[5])>10:
        pwerror = messagebox.showerror("ERROR","Password should be between 8-10 characters")
    elif len(signupdetails[2])!=10:
        noerror = messagebox.showerror("ERROR","Invalid Mobile Number")
    else:
        mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
        mycur = mydb.cursor()
        sqlcheck1 = "SELECT mail FROM signin WHERE mail=%s"
        mycur.execute(sqlcheck1,(mail1,))
        search1 = []
        result1 = mycur.fetchall()
        for check1 in result1:
            search1.append(check1)
        if len(search1)!=0:
            mailerror = messagebox.showerror("ERROR","Mail already exists")
        else:
            mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
            mycur = mydb.cursor()
            sql = "INSERT INTO signin (fname, lname, mobno, dob, mail, pw) VALUES (%s,%s,%s,%s,%s,%s)"
            val = fname.get(),lname.get(), mobno.get(), dob.get(), username.get(), pw.get()
            mycur.execute(sql,val)
            mydb.commit()     
            frontpage.frontpage()
    
def signup():

    welcome.destroy()
    passwordlbl.destroy()
    password.destroy()
    Login.destroy()
    Signup.destroy()
    forgot_pw.destroy()

    global fname
    global lname
    global mobno
    global dob
    global pw
    
    fnamelbl = Label(frm,text="First Name",font="arial 13 bold")
    lnamelbl = Label(frm,text="Last Name",font="arial 13 bold")
    mobnolbl = Label(frm,text="Mobile No.",font="arial 13 bold")
    pwlbl = Label(frm,text="Password",font="arial 13 bold")
    doblbl = Label(frm,text="Date Of Birth",font="arial 13 bold")

    fnamelbl.place(x=80,y=100)
    lnamelbl.place(x=80,y=150)
    mobnolbl.place(x=80,y=200)
    pwlbl.place(x=80,y=300)
    doblbl.place(x=80,y=350)

    fname = Entry(frm,width=30)
    lname = Entry(frm,width=30)
    mobno = Entry(frm,width=30)
    pw = Entry(frm,width=30,show="*")
    dob = Entry(frm,width=30)

    fname.place(x=200,y=105)
    lname.place(x=200,y=155)
    mobno.place(x=200,y=205) 
    pw.place(x=200,y=305)
    dob.place(x=200,y=355)

    Logup = Button(frm,text="LOG UP",font="arial 10 bold",padx=45,pady=5,command=logup)
    Logup.place(x=300,y=450)
    out = Button(frm,text="Back",font="arial 10 bold",padx=45,pady=5,command=reload)
    out.place(x=100,y=450)

def confirm():

    oun = str(username.get())
    npw = str(newpassword.get())
    cpw = str(cnfrmpassword.get())
    
    mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
    mycur = mydb.cursor()
    sql = "SELECT mail FROM signin WHERE mail=%s"
    mycur.execute(sql,(oun,))
    srch = []
    res = mycur.fetchall()
    for add in res:
        srch.append(add)

    det = [oun,npw,cpw]

    for i in range(3):
        if det[i] == "":
            messagebox.showerror("ERROR","No Entry can be left empty")
            break
    if len(srch)==0:
        messagebox.showerror("ERROR","Username doesn't exist")
    elif npw != cpw:
        messagebox.showerror("ERROR","Password doesn't match")
    elif len(npw)<8 or len(npw)>10:
        messagebox.showerror("ERROR","Password should be between 8-10 characters")
    else:
        mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
        mycur = mydb.cursor()
        sqlquery = "UPDATE signin SET pw=%s WHERE mail=%s"
        mycur.execute(sqlquery,(npw,oun,))
        mydb.commit()
        frontpage.frontpage()

def change():

    global username
    global newpassword
    global cnfrmpassword

    if otpentry.get() != " " and otpentry.get() == otp :
        otpentry.config(state=DISABLED)
        mailentry.config(state=DISABLED)
        cont = Button(frm,text="Continue",font="arial 10 bold",padx=45,pady=5,state=DISABLED)
        cont.place(x=270,y=250)

        oldusernamelbl = Label(frm,text="Old Username",font="arial 12")
        oldusernamelbl.place(x=100,y=350)
        username = Entry(frm,width=25)
        username.place(x=240,y=353)

        newpasswordlbl = Label(frm,text="New Password",font="arial 12")
        newpasswordlbl.place(x=100,y=400)
        newpassword = Entry(frm,width=25,show="*")
        newpassword.place(x=240,y=403)

        cnfrmpasswordlbl = Label(frm,text="Confirm Password",font="arial 12")
        cnfrmpasswordlbl.place(x=100,y=450)
        cnfrmpassword = Entry(frm,width=25,show="*")
        cnfrmpassword.place(x=240,y=453)

        changepw = Button(frm,text="Change Password",font="arial 10 bold",padx=45,pady=5,command=confirm)
        changepw.place(x=200,y=520)
    else:
        messagebox.showerror("WARNING","invalid OTP")
   
def pw():
    global otplbl
    global otpentry
    global sendotp
    global cont
    global otp
    global email

    data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(data)
    otp = ""
    for i in range(6):
        otp += data[math.floor(random.random()*l)]
    email = str(mailentry.get())
    print(type(email))
    print(email)

    if  re.search("@gmail.com",mailentry.get()) or re.search("@svvv.in",mailentry.get()):
        sender = "ptotpsab@gmail.com"
        recieve = email
        pw = "ptotpsab123"
        msg = "OTP to change Password for Paradise Travel is"+" "+str(otp)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,pw)
        server.sendmail(sender,recieve,msg)

        otplbl = Label(frm,text="Enter OTP",font="arial 10 bold")
        otplbl.place(x=100,y=150)
        otpentry = Entry(frm,width=30)
        otpentry.place(x=200,y=150)
        cont = Button(frm,text="Continue",font="arial 10 bold",padx=45,pady=5,command=change)
        cont.place(x=270,y=250)
        sendotp = Button(frm,text="Request OTP",font="arial 8 bold",state=DISABLED)
        sendotp.place(x=400,y=96)
    else:
          messagebox.showerror("ERROR","Invalid Email")
        
            
       
def forgot():
    welcome.destroy()
    usernamelbl.destroy()
    username.destroy()
    passwordlbl.destroy()
    password.destroy()
    Login.destroy()
    Signup.destroy()
    forgot_pw.destroy()

    global mailentry

    out1 = Button(frm,text="Back",font="arial 10 bold",padx=45,pady=5,command=reload)
    out1.place(x=100,y=250)
    cont = Button(frm,text="Continue",font="arial 10 bold",padx=45,pady=5,state=DISABLED)
    cont.place(x=270,y=250)
    mail = Label(frm,text="Enter Mail-Id",font="arial 10 bold")
    mail.place(x=100,y=100)
    mailentry = Entry(frm,width=30)
    mailentry.place(x=200,y=100)
    sendotp = Button(frm,text="Request OTP",font="arial 8 bold",command=pw)
    sendotp.place(x=400,y=96)

def reload():

    global frm
    global p
    global plbl
    global welcome
    global usernamelbl
    global passwordlbl
    global username
    global password
    global Login
    global Signup
    global forgot_pw

    frm = Frame(root,height=600,width=700)
    frm.place(x=0,y=0)

    p = ImageTk.PhotoImage(Image.open("photos/loginbg.png"))
    plbl = Label(frm,image=p)
    plbl.place(x=0,y=0)

    welcome = Label(frm,text="WELCOME\n to\n PARADISE TRAVEL",font="arial 15 bold",relief=SOLID,height=4,width=47)
    welcome.place(x=60,y=50)

    usernamelbl = Label(frm,text="Username",font="arial 13 bold")
    usernamelbl.place(x=80,y=250)

    passwordlbl = Label(frm,text="Password",font="arial 13 bold")
    passwordlbl.place(x=80,y=300)

    username = Entry(frm,width=30)
    username.place(x=200,y=255)

    password = Entry(frm,width=30,show="*")
    password.place(x=200,y=305)

    Login = Button(frm,text="LOG IN",font="arial 10 bold",padx=45,pady=5,command=login1)
    Login.place(x=100,y=380)

    Signup = Button(frm,text="SIGN UP",font="arial 10 bold",padx=45,pady=5,command=signup)
    Signup.place(x=300,y=380)

    forgot_pw = Button(frm,text="Forgot Password?",font="arial 10 bold",padx=45,pady=5,command=forgot)
    forgot_pw.place(x=170,y=440)
    
reload()



