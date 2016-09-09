#!/usr/bin/python

import Tkinter
top=Tkinter.Tk()
but1=Tkinter.Button(top,text="Time management")
but2=Tkinter.Button(top,text="Money management")
top.geometry("640x480+1+1");
top.title("Time and money management software")
but1.pack()
but2.pack()
top.mainloop()