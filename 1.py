#!/usr/bin/python

# structura fisierului este 3 butoane intr-un widget
# butoanele de mutat pe zile in alt widget
# widgetul cu zile pus sub ala cu 3 butoane
# un text boox mai jos unde se afiseaza date

import Tkinter
from Tkinter import *
import tkMessageBox

def nextDay():
	print "next day"
	return 0

def prevDay():
	return 0

def addTask():
	# tkMessageBox.showinfo("Pop box","Ceva ceva tot e")
	add_task_window=Tkinter.Tk()
	# label=Tkinter.Message(add_task_window,)
	add_task_window.geometry("300x300+50+50")
	add_task_window.title("Add new task")
	instructions=Tkinter.Message(add_task_window,text="Introduce info about task:",
		width=250)
	task_name=StringVar()
	print task_name
	task_name_insert_place=Tkinter.Message(add_task_window,
		text="Introdu nume",width=250, relief=SUNKEN)
	task_name.set("""Insert task name here""")
	instructions.pack()
	task_name_insert_place.pack()
	print task_name
	add_task_window.mainloop()
	return 0
	#DE CE? DE CE NU MERGE?

def removeTask():
	return 0

def postponeTask():
	return 0

top=Tkinter.Tk()
button_frame_global=Tkinter.Frame(top)
button_frame_line1=Tkinter.Frame(button_frame_global)
button_frame_line2=Tkinter.Frame(button_frame_global)
but1=Tkinter.Button(button_frame_line2,text="<<day",command=prevDay)
but2=Tkinter.Button(button_frame_line2,text="day>>",command=nextDay)
but3=Tkinter.Button(button_frame_line1,text="Add task",command=addTask)
but4=Tkinter.Button(button_frame_line1,text="Remove task",command=removeTask)
but5=Tkinter.Button(button_frame_line1,text="Postpone task",command=postponeTask)
# text = Tkinter.Text(top)
# text.insert (END,"Mesaj")
# msg_to_display=StringVar()
# label=Tkinter.Message(top,textvariable=msg_to_display,
# 	width=1000)
# msg_to_display.set("""asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdadasda
# 	asdasdasdasdasdasdasdasda""")
text_schedule=Tkinter.Message(top,text="Mesaj de afisat",width=620)
top.geometry("640x480+1+1")
top.title("Time and money management software")
but1.pack(side=LEFT)
but2.pack(side=RIGHT)
but3.pack(side=LEFT);
but4.pack(side=LEFT)
but5.pack(side=RIGHT)
button_frame_line1.pack(side=TOP)
button_frame_line2.pack(side=BOTTOM)
button_frame_global.pack()
text_schedule.pack()
top.mainloop()