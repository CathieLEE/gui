from tkinter import *
import time
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
        return
        if name == 'wangliang' and secret == '123456':
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误', message='账号或密码错误！')





class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('数据库管理程序')
        self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)  # 创建不同Frame
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack()  # 默认显示数据录入界面
        menubar = Menu(self.root)
        menubar.add_command(label='数据录入', command=self.inputData)
        menubar.add_command(label='查询', command=self.queryData)
        menubar.add_command(label='统计', command=self.countData)
        menubar.add_command(label='关于', command=self.aboutDisp)
        self.root['menu'] = menubar  # 设置菜单栏

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()





class InputFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.journal_no = StringVar()
        self.journal_id= StringVar()
        self.edi_no = StringVar()
        self.journal_type = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='期刊编号: ').grid(row=1, stick=W, pady=10)
        entry1=Entry(self, textvariable=self.journal_no).grid(row=1, column=1, stick=E)
        Label(self, text='期刊名称: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.journal_id).grid(row=2, column=1, stick=E)
        Label(self, text='主编编号: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.edi_no).grid(row=3, column=1, stick=E)
        Label(self, text='期刊类型: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.journal_type).grid(row=4, column=1, stick=E)
        Button(self, text='录入',command = self.inputcheck).grid(row=6, column=1, stick=E, pady=10)

    def inputcheck(self):
        j_no= self.journal_no.get()
        j_name=self.journal_id.get()
        j_edi_no= self.edi_no.get()
        j_type= self.journal_type.get()
        showinfo(title='成功', message= '录入成功')
        self.journal_id.set('')
        self.journal_type.set('')
        self.edi_no.set('')
        self.journal_no.set('')




class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.journal_no = StringVar()
        self.journal_id = StringVar()
        self.edi_no = StringVar()
        self.edi_name= StringVar()
        self.journal_type = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='期刊编号: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.journal_no).grid(row=1, column=1, stick=E)
        Label(self, text='期刊名称: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.journal_id).grid(row=2, column=1, stick=E)
        '''
        Label(self, text='主编编号: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.edi_name).grid(row=3, column=1, stick=E)
        Label(self, text='主编姓名').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.edi_no).grid(row=4, column=1, stick=E)
        Label(self, text='期刊类型: ').grid(row=5, stick=W, pady=10)
        Entry(self, textvariable=self.journal_type).grid(row=5, column=1, stick=E)
        '''
        Button(self, text='查询').grid(row=7, column=1, stick=E, pady=10)

    #def search(self):





class CountFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='统计界面').pack()


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='关于界面').pack()


root = Tk()
root.title('数据库管理程序登陆界面')
LoginPage(root)
root.mainloop()

