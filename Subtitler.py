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
        self.master.resizable(0, 0)
        self.master.attributes('-topmost', 1)
        self.createWindgets()
        self.flag = True
        # self.transparent = False
        self.top = self.master.winfo_toplevel()

    def overturn(self):
        self.top.update_idletasks()
        self.top.overrideredirect(self.flag)
        self.flag ^= True
        if not self.flag:
            self.lock_img = PhotoImage(file='./lock.png')
            self.flagButton['image'] = self.lock_img
        else:
            self.flagButton['image'] = self.unlock_img

    def createWindgets(self):
        self.unlock_img = PhotoImage(file='./unlock.png')
        self.flagButton = Button(self.master, image=self.unlock_img, bg='black', command=self.overturn)

        self.flagButton.place(relx=0.03, rely=0.03, relwidth=0.02, relheight=0.3)


class Application_ui(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Youku Subtitler v0.2')
        self.master.geometry('420x222')
        self.master.resizable(0, 0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.Text1Var = StringVar(value='subtitle.srt')  # 文件名字  例子：test.srt 文件放到本目录下
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

        self.Command1 = Button(self.top, text='前一秒', command=self.back_onesec)
        self.Command1.place(relx=0.381, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='后一秒', command=self.forward_onesec)
        self.Command1.place(relx=0.705, rely=0.541, relwidth=0.25, relheight=0.185)

        self.Command1 = Button(self.top, text='从指定时间成字幕', command=self.manual_start)
        self.Command1.place(relx=0.381, rely=0.288, relwidth=0.25, relheight=0.185)

        self.Text2 = Entry(self.top)
        self.Text2.place(relx=0.658, rely=0.324, relwidth=0.07, relheight=0.117)

        self.Text3 = Entry(self.top)
        self.Text3.place(relx=0.764, rely=0.324, relwidth=0.07, relheight=0.117)

        self.Text4 = Entry(self.top)
        self.Text4.place(relx=0.857, rely=0.324, relwidth=0.07, relheight=0.113)

        self.Command3 = Button(self.top, text='倍速设置', command=self.speed_change)
        self.Command3.place(relx=0.057, rely=0.793, relwidth=0.25, relheight=0.185)

        self.Label3 = Label(self.top, text='支持1 1.25 2倍速', fg='#8080FF')
        self.Label3.place(relx=0.324, rely=0.829, relwidth=0.307, relheight=0.077)

        self.Label4 = Label(self.top, text='现在是1倍速', fg='#FF8000')
        self.Label4.place(relx=0.324, rely=0.901, relwidth=0.307, relheight=0.077)

        self.Label8 = Label(self.top, text='：')
        self.Label8.place(relx=0.741, rely=0.324, relwidth=0.023, relheight=0.113)

        self.Label2 = Label(self.top, text='：')
        self.Label2.place(relx=0.834, rely=0.324, relwidth=0.023, relheight=0.113)

        self.Label5 = Label(self.top, text='时')
        self.Label5.place(relx=0.658, rely=0.24, relwidth=0.098, relheight=0.077)

        self.Label6 = Label(self.top, text='分')
        self.Label6.place(relx=0.764, rely=0.24, relwidth=0.098, relheight=0.077)

        self.Label7 = Label(self.top, text='秒')
        self.Label7.place(relx=0.857, rely=0.24, relwidth=0.098, relheight=0.077)

        self.Command4 = Button(self.top, text='反馈bug', command=self.report_bug)
        self.Command4.place(relx=0.705, rely=0.793, relwidth=0.25, relheight=0.185)


class Application(Application_ui):
    # 这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.Subtitle = False

        self.time_sub_sequence = {}

        self.dump_list = []

        self.speed_list = [1, 1.25, 2]
        self.current_speed = 1
        self.speed_flag = 0

    def callback(self):
        pass

    def start_with_s(self, s=0):
        self.current_time = s
        print(self.current_time)
        for times in range(self.long - s):
            if not self.Subtitle:
                break
            c_subtitle = ''
            for ele in self.time_sub_sequence[self.current_time]:
                c_subtitle += ele + ''
            self.SLabel['text'] = c_subtitle
            self.SLabel.update()
            self.CTLabel['text'] = '当前时间：%02d:%02d:%02d'%(self.current_time//3600, self.current_time//60%60, self.current_time%60)
            self.CTLabel.update()
            time.sleep(round(1 / self.current_speed, 1))
            self.current_time += 1

    def draw_subtitle(self, i=0):
        if not self.Subtitle:
            self.Subtitle = True
            self.subtitle = CreatSubtitile()
            self.subtitle.master.title('Subtitle')
            self.subtitle.master.resizable(0, 0)
            self.subtitle.master.protocol("WM_DELETE_WINDOW", self.callback)

            self.SLabel = Label(self.subtitle.master, text='')
            self.SLabel.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

            self.CTLabel = Label(self.subtitle.master, text='当前时间：')
            self.CTLabel.place(relx=0, rely=0.34, relwidth=0.15, relheight=0.3)

            self.start_with_s(i)

            if self.Subtitle:
                self.subtitle.master.mainloop()

    def close_subtitle(self):
        if self.Subtitle:
            self.subtitle.master.destroy()
            self.subtitle = None
            self.Subtitle = False

    def dump_subtitle(self):
        try:
            with open("./{}".format(self.Text1.get()), 'r', encoding='gbk') as file:
                a = file.readlines()
                print(a)
                for line in a:
                    strip_line = line.strip("\n")
                    if strip_line:
                        self.dump_list.append(strip_line)
                print(self.dump_list)
        except FileNotFoundError:
            pass

        for line in self.dump_list[::-1]:
            if not '-->' in line:
                continue
            t_long = [int(x) for x in (line.split(' --> ')[1].split(',')[0].split(':'))]
            self.long = t_long[0] * 3600 + t_long[1] * 60 + t_long[2]
            for i in range(self.long):
                self.time_sub_sequence[i] = ''
            break

        temp = []
        for line in self.dump_list:
            if not line.isdigit():
                temp.append(line)
            elif line.isdigit() and temp:
                t = temp[0].split(' --> ')
                t_start, t_end = [int(x) for x in (t[0].split(',')[0].split(':'))], [int(y) for y in (t[1].split(',')[0].split(':'))]
                t_start_s = t_start[0] * 3600 + t_start[1] * 60 + t_start[2]
                t_end_s = t_end[0] * 3600 + t_end[1] * 60 + t_end[2]
                for t in range(t_start_s, t_end_s + 1):
                    self.time_sub_sequence[t] = temp[1:]
                temp = []
        print(self.time_sub_sequence)

    def manual_start(self):
        t_value = True
        try:
            hour = int(self.Text2.get()) * 3600 if self.Text2.get() else 0
            minute = int(self.Text3.get()) * 60 if self.Text3.get() else 0
            second = int(self.Text4.get()) if self.Text4.get() else 0
        except ValueError:
            t_value = False
        print(t_value)
        if t_value and not self.Subtitle:
            self.draw_subtitle(hour + minute + second)

    def speed_change(self):
        self.speed_flag += 1
        self.current_speed = self.speed_list[self.speed_flag % len(self.speed_list)]
        self.Label4['text'] = '现在是{}倍速'.format(self.speed_list[self.speed_flag % len(self.speed_list)])
        self.Label4.update()

    def back_onesec(self):
        if self.Subtitle:
            self.current_time -= 1

    def forward_onesec(self):
        if self.Subtitle:
            self.current_time += 1

    def report_bug(self):
        from webbrowser import open_new
        open_new("mailto:codingdogzxg@gmail.com")


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()

