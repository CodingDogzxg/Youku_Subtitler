#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *
import time


class CreatSubtitile(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.master = Toplevel()
        self.master.grid()
        self.master.geometry("800x50")
        self.createWindgets()
        self.flag = True
        # self.transparent = False
        self.top = self.master.winfo_toplevel()

    def overturn(self):
        self.top.update_idletasks()
        self.top.overrideredirect(self.flag)
        self.flag ^= True
        if not self.flag:
            self.lock_img = PhotoImage(file='lock.png')
            self.flagButton['image'] = self.lock_img
        else:
            self.flagButton['image'] = self.unlock_img

    def createWindgets(self):
        self.unlock_img = PhotoImage(file='unlock.png')
        self.flagButton = Button(self.master, image=self.unlock_img, bg='black', command=self.overturn)

        self.flagButton.place(relx=0.03, rely=0.03, relwidth=0.02, relheight=0.3)


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Youku Subtitler v0.1')
        self.master.geometry('420x222')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Text1Var = StringVar(value='文件名字  例子：test.srt 文件放到本目录下')
        self.Text1 = Entry(self.top, fg='#FF0000', textvariable=self.Text1Var)
        self.Text1.place(relx=0.038, rely=0.108, relwidth=0.8, relheight=0.113)

        self.DumpSubtitle = Button(self.top, text='读取文件', command=self.dump_subtitle)
        self.DumpSubtitle.place(relx=0.85, rely=0.108, relwidth=0.13, relheight=0.113)

        self.Command1 = Button(self.top, text='从头生成字幕', command=self.draw_subtitle)
        self.Command1.place(relx=0.057, rely=0.288, relwidth=0.25, relheight=0.185)

        self.Label1 = Label(self.top, text='这里是字幕文件的文件名：')
        self.Label1.place(relx=0.038, rely=0.032, relwidth=0.34, relheight=0.077)

        self.Command2 = Button(self.top, text='关闭字幕', command=self.close_subtitle)
        self.Command2.place(relx=0.057, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='前一句')
        self.Command1.place(relx=0.381, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='后一句')
        self.Command1.place(relx=0.705, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='从指定位置成字幕')
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
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Subtitle = False
        self.time_list = []
        self.subtitle_list = []
        self.b = []

    def callback(self):
        pass

    def draw_subtitle(self):
        if not self.Subtitle:
            self.Subtitle = True
            self.subtitle = CreatSubtitile()
            self.subtitle.master.title('Subtitle')
            self.subtitle.master.resizable(0, 0)
            self.subtitle.master.protocol("WM_DELETE_WINDOW", self.callback)

            self.SLabel = Label(self.subtitle.master, text='')
            self.SLabel.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

            temp = []
            s_t = 0
            for line in self.b:
                if not line.isdigit():
                    temp.append(line)
                elif line.isdigit() and temp:
                    # if int(temp[0].split(" --> ")[1].replace(":", "").split(",")[0]) > s_t:
                    #     time.sleep(int(temp[0].split(" --> ")[1].replace(":", "").split(",")[0]) - s_t)
                    #     s_t += int(temp[0].split(" --> ")[1].replace(":", "").split(",")[0])

                    t = temp[0].split(' --> ')
                    t_start, t_end = t[0].split(',')[0].split(':'), t[1].split(',')[0].split(':')
                    t_start_s = int(t_start[0]) * 3600 + int(t_start[1]) * 60 + int(t_start[2])
                    t_end_s = int(t_end[0]) * 3600 + int(t_end[1]) * 60 + int(t_end[2])

                    if t_start_s > s_t:
                        time.sleep(t_start_s - s_t)
                        s_t += t_start_s - s_t

                    self.SLabel['text'] = '{}'.format(temp[1:])
                    self.SLabel.update()
                    print(temp[1:])
                    # time.sleep(int(temp[0].split(" --> ")[1].replace(":", "").split(",")[0]) - int(temp[0].split(" --> ")[0].replace(":", "").split(",")[0]))

                    time.sleep(t_end_s - t_start_s)
                    temp = []

            self.subtitle.master.mainloop()

    def close_subtitle(self):
        if self.Subtitle:
            self.subtitle.master.destroy()
            self.subtitle = None
            self.Subtitle = False

    def dump_subtitle(self):
        try:
            with open("{}".format(self.Text1.get()), 'r') as file:
                a = file.readlines()
                print(a)
                for line in a:
                    strip_line = line.strip("\n")
                    if strip_line:
                        self.b.append(strip_line)
                print(self.b)
        except FileNotFoundError:
            pass


    def Command3_Cmd(self, event=None):
        print(self.subtitle.master)

    def Command4_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass



if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

