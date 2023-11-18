from cProfile import label
import datetime
from tkinter import *
import time
from tkinter import font
from turtle import color

from matplotlib.pyplot import fill

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=150,y=70)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
clock_window=Tk()
clock_window.title("DIGITAL CLOCK")
clock_window.geometry('400x400')
Canvas=Canvas(clock_window,width=1000,height=750,bg="Black")
Canvas.create_text(200,50,text="DIGITAL CLOCK",fill="white",font=("Helvetica 15 bold"))
Canvas.pack()
app=App(clock_window)
clock_window.after(1000,app.update_clock)        
clock_window.mainloop()