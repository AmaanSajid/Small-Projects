from struct import pack
import tkinter as tk
from turtle import left

from matplotlib.pyplot import fill
from matplotlib.sankey import RIGHT
from pyparsing import col

def submit():
    
	expense=entry_var.get()
	amount=entry_value.get()
	
	print("Expense "+expense)
	print(amount)
	
	entry_var.set("")
	entry_value.set("")

expense=tk.Tk()
expense.title("EXPENSES")
expense.geometry('500x500')
entry_var=tk.StringVar()
entry_value=tk.IntVar()
Canvas=tk.Canvas(expense,width=1000,height=750,bg="Black")
Canvas.create_text(250,50,text="EXPENSES",fill="white",font=("Helvetica 15 bold"))
Canvas.pack(fill="both",expand=True)
name_label = tk.Label(Canvas, text = 'Expense', font=('calibre',15, 'bold'))
name_entry = tk.Entry(Canvas,textvariable = entry_var, font=('calibre',15,'normal'))
passw_label = tk.Label(Canvas, text = 'Amount', font = ('calibre',15,'bold'))
passw_entry=tk.Entry(Canvas, textvariable = entry_value, font = ('calibre',15,'normal'))
sub_btn=tk.Button(Canvas,text = 'Add', command = submit,font=('calibre',15,'normal'))
name_label.place(relx = 0.25,rely = 0.25,anchor = 'center')
name_entry.place(relx = 0.65,rely = 0.25,anchor = 'center')
passw_label.place(relx = 0.25,rely = 0.38,anchor = 'center')
passw_entry.place(relx = 0.65,rely = 0.38,anchor = 'center')
sub_btn.place(x=210, y=220)
expense.mainloop()