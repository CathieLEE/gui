# -*- coding: cp936 -*-
from tkinter import *
root = Tk()
root.title("hello world")
root.geometry('300x200')

Label(root, text='校训', font=('Arial', 20)).pack()

frm = Frame(root)
#left
frm_L = Frame(frm)
Label(frm_L, text='厚德', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='博学', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

#right
frm_R = Frame(frm)
Label(frm_R, text='敬业', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='乐群', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()