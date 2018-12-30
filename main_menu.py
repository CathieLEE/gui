from tkinter import *
from tkinter import messagebox

###########登陆界面
from tkinter import *
from tkinter.messagebox import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (300, 180))  # 设置窗口大小
        self.username = StringVar()
        self.password = StringVar()
        self.createPage()

    def createPage(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        self.page.destroy()
        MainPage(self.root)
        return 0
        if name == 'wangliang' and secret == '123456':
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')


#########################主界面
class MainPage(object):
    def __init__(self,master=None):
        self.root=master
        self.root.geometry('800x600')
        self.createPage()

    def createPage(self):
            main_menu = Menu(self.root)
            search_menu = Menu(main_menu, tearoff=FALSE)
            search_menu.add_command(label='期刊信息')
            search_menu.add_command(label='读者信息')
            search_menu.add_command(label='主编信息')
            main_menu.add_cascade(label='信息查询', menu=search_menu)
            #查询
            add_menu = Menu(main_menu, tearoff=FALSE)
            add_menu.add_command(label='期刊信息')
            add_menu.add_command(label='读者信息')
            add_menu.add_command(label='期刊主编')
            main_menu.add_cascade(label='添加', menu=add_menu)
            #添加
            cancle_menu = Menu(main_menu, tearoff=FALSE)
            cancle_menu.add_command(label='期刊信息')
            cancle_menu.add_command(label='读者信息')
            cancle_menu.add_command(label='主编信息')
            main_menu.add_cascade(label='删除', menu=cancle_menu)
            ##删除菜单
            modify_menu = Menu(main_menu, tearoff=FALSE)
            modify_menu.add_command(label='期刊信息')
            modify_menu.add_command(label='读者信息')
            modify_menu.add_command(label='主编信息')
            main_menu.add_cascade(label='修改', menu=modify_menu)
            ##修改菜单
            main_menu.add_command(label='读者借阅')
            # 借阅
            self.root['menu'] = main_menu  # 设置菜单栏





'''
    def createPage(self):
        self.page= Frame(self.root)
        self.page.pack()
        Menu_bar=Menu(self.page).pack()
        search_menu = Menu(main_menu, tearoff=FALSE)
        search_menu.add_command(label='期刊信息')
        search_menu.add_command(label='读者信息')
        search_menu.add_command(label='主编信息')
        Menu_bar.add_cascade(label='查询', menu=search_menu)
'''



root = Tk()
root.title('小程序')
LoginPage(root)
root.mainloop()

'''
main_window = Tk()
main_window.title('期刊数据库管理程序')
main_window.geometry('800x600')
frame_menu= Frame(main_window,)
Button(frame_menu,text = '添加',width= 10).grid(row=0,column= 0)
Button(frame_menu,text = '删除',width= 10).grid(row=0,column= 1)
Button(frame_menu,text = '修改',width= 10).grid(row=0,column= 2)
Button(frame_menu,text = '查询',width= 10).grid(row=0,column= 3)
Menubutton(frame_menu,text = 'text',width= 10).grid(row=0,column=4)
Label(frame_menu,text="身份：目录主编").grid(row=0,column=6)
frame_menu.pack(fill=X)

main_menu= Menu(main_window)
search_menu= Menu(main_menu,tearoff= FALSE)
search_menu.add_command(label='期刊信息')
search_menu.add_command(label='读者信息')
search_menu.add_command(label='主编信息')
main_menu.add_cascade(label= '查询',menu= search_menu)
##查询菜单
add_menu= Menu(main_menu,tearoff= FALSE)
add_menu.add_command(label='期刊信息')
add_menu.add_command(label='读者信息')
add_menu.add_command(label='期刊主编')
main_menu.add_cascade(label='添加',menu= add_menu)
main_menu.add_command(label='读者借阅')
##添加菜单
cancle_menu=Menu(main_menu,tearoff=FALSE)
cancle_menu.add_command(label='期刊信息')
cancle_menu.add_command(label='读者信息')
cancle_menu.add_command(label='主编信息')
main_menu.add_cascade(label='删除',menu= cancle_menu)
##删除菜单
modify_menu=Menu(main_menu,tearoff=FALSE)
modify_menu.add_command(label='期刊信息')
modify_menu.add_command(label='读者信息')
modify_menu.add_command(label='主编信息')
main_menu.add_cascade(label='修改',menu= modify_menu)
##修改菜单
main_window.config(menu= main_menu)
##主菜单
main_window.mainloop()
'''
