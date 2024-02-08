import tkinter as tk
from tkinter import ttk

# TK is the main window
window=tk.Tk()
# window.geometry("800x700+100+100")
window.minsize(width=500,height=500)

window.title("GUI")



result_label = ttk.Label(master=window,text="Num 1 =",font=("Arial",16))
result_label.grid(row=0,column=0)

# Textfield
my_textfield = ttk.Entry(master=window)
# pady for vertical gap
my_textfield.grid(row=0,column=1 ,pady=10,sticky="E")


result_label = ttk.Label(master=window,text="Num 2 =",font=("Arial",16))
result_label.grid(row=1,column=0)

my_textfield2 = ttk.Entry(master=window)
my_textfield2.grid(row=1,column=1 ,pady=10,sticky="E")



# get the value of textfield

def my_button_handler():
    # print("Button Clicked")
    textfieldvalue=int(my_textfield.get())
    textfieldvalue2 =int( my_textfield2.get())
    sum =textfieldvalue+textfieldvalue2
    result_label.configure(text="Result = "+str(sum))


# there is no parenthesis while calling function it means it will only call when the button is clicked
my_button = ttk.Button(master=window,text="Add",command=my_button_handler)
my_button.grid(row=2,column=1 ,pady=10,sticky="w")
my_button




result_label = ttk.Label(master=window,text="Result =",font=("Arial",16))
result_label.grid(row=3,column=0)
# we can import font class
# so font = font.FONt(size=25)
result_label = ttk.Label(master=window,text="result =",font=("Arial",16))
result_label.grid(row=3,column=0)


window.mainloop()
# any code below will not execute until the main window is closed
# print("hello")




