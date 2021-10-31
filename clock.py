from tkinter import *
from tkinter.ttk import *
from time import *
import random


root = Tk()
root.configure(background = 'black')
root.geometry("380x120+0+0")
root.overrideredirect(1)

def time():
    timer = strftime('%I:%M:%S %p')
    date = strftime('%d/%B/%Y')

    string = f"{date} \n{timer}"

    label.config(text = string)
    label.after(1000,time)

cols = ['white', 'green', 'magenta', 'blue', 'yellow', 'red', 'orange', 'cyan' , 'pink','light green']
rand_color = random.choice(cols)
label = Label(root, font=("ds-digital", 40), background = "black", foreground = rand_color)
label.pack(anchor='center')
time()

root.mainloop()