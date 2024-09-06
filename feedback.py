from tkinter import *
import frontpage
import login


def feedback():
    frontpage.top.destroy()
    frontpage.middle.destroy()
    frontpage.bottom.destroy()

    fbacklbl = Label(text="FEEDBACK",relief=SOLID,width=69,height=2,font="arial 13 bold")
    fbacklbl.place(x=2,y=0)

    back = Button(fbacklbl,text="X",font="arial 10 bold",bg="red",command=frontpage.frontpage)
    back.place(x=670,y=5)

    fbackfrm = LabelFrame(text="FEEDBACKS",height=275,width=698,relief=SOLID,font="arial 10 bold",fg="white",bg="black")
    fbackfrm.place(x=1,y=44)

    commentdisplay = Text(fbackfrm,height=15,width=86)
    commentdisplay.place(x=1,y=1)

    commentfrm =  LabelFrame(text="Comment here",height=279,width=698,relief=SOLID,font="arial 9 bold",fg="white",bg="black")
    commentfrm.place(x=1,y=318)

    fbfile1 = open("Feedbacks2.txt")
    fbread1 = fbfile1.read()
    fbfile1.close()

    commentdisplay.insert(1.0,fbread1)

    def submit():

        name1 = name.get()
        mailid1 = mailid.get()
        rateus1 = rateus.get()
        commenttxt1 = commenttxt.get(1.0,END)
        
        fbfile = open("Feedbacks1.txt","w")
        fbfile.write("Name: ")
        fbfile.write(name1)
        fbfile.write("\nMail Id: ")
        fbfile.write(mailid1)
        fbfile.write("\nRatings: ")
        fbfile.write(rateus1)
        fbfile.write("/5\n")
        fbfile.write("Opinon: ")
        fbfile.write(commenttxt1)
        fbfile.write("\n\n")
        fbfile.close()

        fbfile = open("Feedbacks1.txt")
        fbread = fbfile.read()
        fbfile.close()

        commentdisplay.insert(1.0,fbread)

        fbfile2 = open("Feedbacks2.txt","w")
        fbread2 = fbfile2.write(str(commentdisplay.get(1.0,END)))
        fbfile2.close()

        name.delete(0,END)
        mailid.delete(0,END)
        rateus.delete(0,END)
        commenttxt.delete(1.0,END)
    
    def clear():
        name.delete(0,END)
        mailid.delete(0,END)
        rateus.delete(0,END)
        commenttxt.delete(1.0,END)

    namelbl = Label(commentfrm,text="Name",font="arial 11 bold")
    namelbl.place(x=10,y=10)
    
    name = Entry(commentfrm)
    name.place(x=65,y=13)

    mailidlbl = Label(commentfrm,text="Mail ID",font="arial 11 bold")
    mailidlbl.place(x=210,y=10)

    mailid = Entry(commentfrm,width=25)
    mailid.place(x=275,y=13)

    rateuslbl = Label(commentfrm,text="Ratings",font="arial 11 bold")
    rateuslbl.place(x=445,y=10)

    rateus = Spinbox(commentfrm,from_=0,to=5)
    rateus.place(x=520,y=13)

    commenttxt = Text(commentfrm,width=66,height=11)
    commenttxt.place(x=10,y=53)

    Submit = Button(commentfrm,text="Submit",font="arial 10 bold",padx=20,pady=2,command=submit)
    Submit.place(x=565,y=75)

    Clear = Button(commentfrm,text="Clear",font="arial 10 bold",padx=25,pady=2,command=clear)
    Clear.place(x=565,y=125)

'''def feedback():
    frontpage.top.destroy()
    frontpage.middle.destroy()
    frontpage.bottom.destroy()

    fbacklbl = Label(text="FEEDBACK",relief=SOLID,width=69,height=2,font="arial 13 bold")
    fbacklbl.place(x=2,y=0)

    back = Button(fbacklbl,text="X",font="arial 10 bold",command=frontpage.frontpage)
    back.place(x=670,y=5)

    fbackfrm = LabelFrame(height=555,width=698,relief=SOLID)
    fbackfrm.place(x=1,y=44)

    txt = Label(fbackfrm,text="Leave Us A Comment",font="arial 14 bold")
    txt.place(x=260,y=40)

    global ename
    global eemail
    global eno
    global erateus
    global emsg

    name = Label(fbackfrm,text="Name",font="arial 12 bold")
    name.place(x=35,y=110)
    ename = Entry(fbackfrm,width=35)
    ename.place(x=37,y=140)

    email = Label(fbackfrm,text="Email",font="arial 12 bold")
    email.place(x=35,y=210)
    eemail = Entry(fbackfrm,width=35)
    eemail.place(x=37,y=240)

    no = Label(fbackfrm,text="Mobile Number",font="arial 12 bold")
    no.place(x=35,y=310)
    eno = Entry(fbackfrm,width=35)
    eno.place(x=37,y=340)

    rateus = Label(fbackfrm,text="Ratings",font="arial 12 bold")
    rateus.place(x=35,y=410)
    erateus = Spinbox(fbackfrm,from_=0,to=5,width=33)
    erateus.place(x=37,y=440)

    msg = Label(fbackfrm,text="Message",font="arial 12 bold")
    msg.place(x=318,y=110)
    emsg = Text(fbackfrm,height=15,width=40)
    emsg.place(x=320,y=150)

    send = Button(fbackfrm,text="Send",font="arial 12",width=15,command=sub)
    send.place(x=400,y=430)

    reset = Button(fbackfrm,text="Reset",font="arial 12",width=15,command=again)
    reset.place(x=400,y=480)

def again():
    ename.delete(0,END)
    eemail.delete(0,END)
    eno.delete(0,END)
    erateus.delete(0,END)
    emsg.delete(1.0,END)

def sub():

    en = ename.get()
    ee = eemail.get()
    phno = eno.get()
    er = erateus.get()
    em = emsg.get(1.0,END)
    print(en,ee,phno,er,em)

    msg = "Thank You"+str(en)+",for your valuable feedback\n Your message:-\n\t"+str(em)

    sender = "ptotpsab@gmail.com"
    recieve = ee
    pw = "ptotpsab123"
#    msg = "OTP to change Password for Paradise Travel is"+" "+str(otp)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,pw)
    server.sendmail(sender,recieve,msg)'''    

