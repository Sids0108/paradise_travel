from tkinter import *
import booking
import frontpage

def Clear():
    booking.first_name.delete(0,END)
    booking.last_name.delete(0,END)
    booking.address.delete(0,END)
    booking.pincode.delete(0,END)
    booking.place.delete(0,END)
    booking.email.delete(0,END)
    booking.gender.delete(0,END)
    booking.dob.delete(0,END)
    booking.id_type.delete(0,END)
    booking.food.delete(0,END)
    booking.room_type.delete(0,END)
    booking.vehicle_type.delete(0,END)
    booking.noppl.delete(0,END)
    return frontpage.frontpage()
