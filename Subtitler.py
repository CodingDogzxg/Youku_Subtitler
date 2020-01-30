#!/usr/bin/env python
#-*- coding:utf-8 -*-

from tkinter import *


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('420x222')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Text1Var = StringVar(value='相对路径就可以 文件放到相同目录下')
        self.Text1 = Entry(self.top, fg='#FF0000', textvariable=self.Text1Var)
        self.Text1.place(relx=0.038, rely=0.108, relwidth=0.917, relheight=0.113)

        self.Command1 = Button(self.top, text='从头生成字幕', command=self.Command1_Cmd)
        self.Command1.place(relx=0.057, rely=0.288, relwidth=0.25, relheight=0.185)

        self.Label1 = Label(self.top, text='这里是字幕文件路径：')
        self.Label1.place(relx=0.038, rely=0.032, relwidth=0.288, relheight=0.077)

        self.Command1 = Button(self.top, text='前一句', command=self.Command1_Cmd)
        self.Command1.place(relx=0.057, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='后一句', command=self.Command1_Cmd)
        self.Command1.place(relx=0.381, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command2 = Button(self.top, text='关闭字幕', command=self.Command2_Cmd)
        self.Command2.place(relx=0.705, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='从指定位置成字幕', command=self.Command1_Cmd)
        self.Command1.place(relx=0.381, rely=0.288, relwidth=0.25, relheight=0.185)

        self.Text2Var = StringVar(value='')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var)
        self.Text2.place(relx=0.724, rely=0.324, relwidth=0.098, relheight=0.117)

        self.Text3Var = StringVar(value='')
        self.Text3 = Entry(self.top, textvariable=self.Text3Var)
        self.Text3.place(relx=0.857, rely=0.324, relwidth=0.098, relheight=0.113)

        self.Label2 = Label(self.top, text='：')
        self.Label2.place(relx=0.819, rely=0.324, relwidth=0.04, relheight=0.113)

        self.Command3 = Button(self.top, text='倍速设置', command=self.Command3_Cmd)
        self.Command3.place(relx=0.057, rely=0.793, relwidth=0.25, relheight=0.185)

        self.Label3 = Label(self.top, text='支持1 1.25 1.5 2倍速', fg='#8080FF')
        self.Label3.place(relx=0.324, rely=0.829, relwidth=0.307, relheight=0.077)

        self.Label4 = Label(self.top, text='现在是1倍速', fg='#FF8000')
        self.Label4.place(relx=0.324, rely=0.901, relwidth=0.307, relheight=0.077)

        self.Label5 = Label(self.top, text='分')
        self.Label5.place(relx=0.724, rely=0.24, relwidth=0.079, relheight=0.077)

        self.Label6 = Label(self.top, text='秒')
        self.Label6.place(relx=0.857, rely=0.24, relwidth=0.098, relheight=0.077)

        self.Command4 = Button(self.top, text='反馈bug', command=self.Command4_Cmd)
        self.Command4.place(relx=0.705, rely=0.793, relwidth=0.25, relheight=0.185)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command2_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command1_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command3_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
