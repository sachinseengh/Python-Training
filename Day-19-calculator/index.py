
import tkinter as tk
from tkinter import ttk

# TK is the main window
window=tk.Tk()
# window.geometry("800x700+100+100")
window.minsize(width=500,height=500)
window.resizable(0,0)

window.title("GUI")

buttons =[
    '7','8','9','+',
    '4','5','6','-',
    '1','2','3','*',
    '0','c','.','/',
    '='
          ]



input_value=tk.StringVar()

def handle_keypress(key):
    
    if(key=='='):
        result=eval(input_value.get())
        input_value.set(result)
    elif(key=="c"):
        result='0'
        input_value.set(result)
        
    
    else:
        result=input_value.get()+key
        input_value.set(result)




window.rowconfigure((0,1,2,3,4,5),weight=1)
window.columnconfigure((0,1,2,3),weight=1)

input = ttk.Entry(master=window,justify='right',textvariable=input_value,font=25)
input.grid(row=0,column=0,columnspan=4,sticky="nesw")

row =1
col =0

for i in range(len(buttons)):
    
    
    if(buttons[i]=="="):
        button= ttk.Button(master=window,text=buttons[i],command=lambda x= buttons[i]:handle_keypress(x))
        button.grid(row=row,column=col,columnspan=4,sticky="nesw")
    else:
        button=ttk.Button(master=window,text=buttons[i],command=lambda x= buttons[i]:handle_keypress(x))
        button.grid(row=row,column=col,sticky="nesw")
    
    
    
    
    
    
    # button = ttk.Button(master=window,text=buttons[i])
    # button.grid(row=row,column=col)
    col= col+1
    if(col>3):
        row=row+1
        col=0








window.mainloop()