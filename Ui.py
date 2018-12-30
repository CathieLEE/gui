from tkinter import *
from tkinter import messagebox

def check_in():
    name=var_name.get()
    password=var_password.get()
    if name=='1':
        if password=='0':
            messagebox.showinfo(title='登陆',message='登陆成功！')



window = Tk()
window.title('登陆界面')
window.geometry('400x200')
frm= Frame(window)
frm_empty= Frame(frm)
frm_empty.pack(side= TOP,pady= 15)
frm_name= Frame(frm)
label_name= Label(frm_name,text='用户名:')
label_name.pack(side=LEFT,fill=BOTH)
var_name = StringVar()
entry_name = Entry(frm_name,textvariable = var_name)
entry_name.pack(side=LEFT)
frm_name.pack(pady= 20)
frm_pass= Frame(frm)
label_pass = Label(frm_pass,text = '密码：')
label_pass.pack(side=LEFT)
var_password= StringVar()
entry_pass = Entry(frm_pass,textvariable = var_password)
entry_pass.pack(side= LEFT)
frm_pass.pack(expand=1,fill=Y)
bt_enter= Button(frm,text='登陆',command = check_in)
bt_enter.pack(side=BOTTOM,pady=10)
frm.pack()
window.mainloop()
