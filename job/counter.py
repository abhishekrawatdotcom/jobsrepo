import time
from tkinter import *


root = Tk()

root.geometry('800x500')
root.configure(background='black')
root.resizable(0,0)
root.overrideredirect(1)

def sttt():
    s = time.strftime("%S")
    label.configure(text=s)
    label.after(200,sttt)

label = Label(root,font=("ds-digital",50,"bold"),bg="black",fg="red",bd=50)
label.grid(row=0,column=1)
sttt()
print("done")
root.mainloop()


