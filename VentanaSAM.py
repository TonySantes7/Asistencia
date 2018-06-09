# Santes Mejia Antonio
print "...Tecnicas de programacion.."

import tkinter

from tkinter import messagebox

top=tkinter.Tk()
def helloCallBack():
    messagebox.showinfo("Hola Python1","Hola Santes")

B=tkinter.Button(top,text="Hello",command=helloCallBack)
B.pack()
B.place(x=35, y=50)

top.mainloop()

