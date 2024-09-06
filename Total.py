from tkinter import *
import booking

def Total():
    
    booking.customer_no.delete(0,END)
    booking.first_name.delete(0,END)
    booking.last_name.delete(0,END)
    booking.address.delete(0,END)
    booking.pincode.delete(0,END)
    booking.place.delete(0,END)
    booking.email.delete(0,END)
    booking.gender.delete(0,END)
    booking.dob.delete(0,END)
    booking.id_type.delete(0,END)
    booking.check_In.delete(0,END)
    booking.check_out.delete(0,END)
    booking.food.delete(0,END)
    booking.room_type.delete(0,END)
    booking.vehicle_type.delete(0,END)

    total = Button(text="Total",font="arial 10 bold",padx=26,pady=4,state=DISABLED)
    total.place(x=10,y=490)
