from tkinter import *
from PIL import ImageTk,Image
import time
import webbrowser
import mysql.connector
import login
import booking
import status
import feedback
import contact
import Pay

def exit():
    top.destroy()
    middle.destroy()
    bottom.destroy()
    return login.reload()
    
def web():
    webbrowser.open("file:///C:/Users/acer/Desktop/Work/projecthtml/firstpage.html")
    
def frontpage():

    global top
    global middle
    global bottom
    global p
    global p1
    global last

    top = Frame(height=220)
    top.pack(fill=BOTH)

    p = ImageTk.PhotoImage(Image.open("photos/ptbg.png"))
    plbl = Label(top,image=p)
    plbl.place(x=0,y=0)
    
    middle = Frame(height=35,bg='lavender')
    middle.pack(fill=BOTH)

    bottom = Frame(height=350)
    bottom.pack(fill=BOTH)

    p1 = ImageTk.PhotoImage(Image.open("photos/bottombg.png"))
    plbl1 = Label(bottom,image=p1)
    plbl1.place(x=0,y=0)

    def clock():
        hour = time.strftime("%I")
        minute = time.strftime("%M") 
        seconds = time.strftime("%S")
        am_pm = time.strftime("%p")
        day = time.strftime("%A")
        date = time.strftime("%d")
        month = time.strftime("%b")
        year = time.strftime("%Y")
        time1.config(text=hour+":"+minute+":"+seconds+" "+am_pm)
        time1.after(1000,clock)
        time2.config(text=day)
        time3.config(text=date+"/"+month+"/"+year)
    time1 = Label(middle,font="arial 14 bold",bg='lavender')
    time2 = Label(middle,font="arial 14 bold",bg='lavender')
    time3 = Label(middle,font="arial 14 bold",bg='lavender')
    time1.place(x=120,y=3)
    time2.place(x=295,y=3)
    time3.place(x=460,y=3)
    clock()

    a = login.username.get()
    mydb = mysql.connector.connect(host="localhost",user="root",password="0108",database="signup")
    mycur = mydb.cursor()
    sql = "SELECT fname FROM signin WHERE mail=%s"
    mycur.execute(sql,(a,))
    name = []
    final = mycur.fetchall()
    for n in final:
        name.append(n)
    
    wellbl = Label(bottom,text="Welcome",font="arial 9 bold")
    wellbl.place(x=5,y=5)
    welname = Label(bottom,text=name,font="arial 9 bold")
    welname.place(x=65,y=5)

    
    places_to_visit = Button(bottom,text="Places to visit",bg='lavender',font="arial 10 bold",padx=34,pady=10,command=web)
    book_now = Button(bottom,text="Book Now",bg='lavender',font="arial 10 bold",padx=46,pady=10,command=booking.booking)
    Status = Button(bottom,text="My Bookings",bg='lavender',font="arial 10 bold",padx=39,pady=10,command=status.status)
    Feedback = Button(bottom,text="Feedback",bg='lavender',font="arial 10 bold",padx=44,pady=10,command=feedback.feedback)
    Contact = Button(bottom,text="Contact",bg='lavender',font="arial 10 bold",padx=50,pady=10,command=contact.contact)
    log_out = Button(bottom,text="Log Out",bg='lavender',font="arial 10 bold",padx=45,pady=10,command=exit)

    places_to_visit.place(x=120,y=70)
    book_now.place(x=120,y=150)
    Status.place(x=120,y=230)
    Feedback.place(x=425,y=70)
    Contact.place(x=425,y=150)
    log_out.place(x=425,y=230)

    
