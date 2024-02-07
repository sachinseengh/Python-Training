import tkinter as tk
from tkinter import ttk

# TK is the main window
window=tk.Tk()
# window.geometry("800x700+100+100")
window.minsize(width=500,height=500)

window.title("GUI")


# Textfield
my_textfield = ttk.Entry(master=window)
my_textfield.place(x=100,y=100)

my_textfield2 = ttk.Entry(master=window)
my_textfield2.place(x=100,y=200)

# get the value of textfield

def my_button_handler():
    # print("Button Clicked")
    textfieldvalue=int(my_textfield.get())
    textfieldvalue2 =int( my_textfield2.get())
    print(textfieldvalue+textfieldvalue2)


# there is no parenthesis while calling function it means it will only call when the button is clicked
my_button = ttk.Button(master=window,text="Add",command=my_button_handler)
my_button.place(x=120,y=350)
my_button



window.mainloop()
# any code below will not execute until the main window is closed
# print("hello")