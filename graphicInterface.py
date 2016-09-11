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
# Se va afisa ce este schedulat pentru ziua urmatoare,
# daca este schedulat ceva.

def prevDay():
	return 0
# Se va afisa ce este schedulat pentru ziua anterioara,
# daca este schedulat ceva.

def getAddTaskEntries(line1_entry,line2_entry,
	line3_entry,line4_entry,add_task_window):
	print line1_entry.get()
	task_name=line1_entry.get()
	priority=line2_entry.get()
	time_req=line3_entry.get()
	deadline=line4_entry.get()
	# print [task_name, priority, time_req, deadline]
	confirmation_msg = tkMessageBox.showinfo("Info Received",
		"The information you introduced about the task was received.")
	add_task_window.destroy()
	return [task_name, priority, time_req, deadline]
#functia primeste Entrierile din addTask la apasarea
#butonului ok si imi intoarce ce stringuri au fost
#introduse prin ele, sub forma unei liste
#numele elementelor din lista sunt sugestive
#la final apare un mesaj care explica ca s-au primit
#informatile iar fereastra de introducere se distruge

def addTask():
	# tkMessageBox.showinfo("Pop box","Ceva ceva tot e")
	add_task_window=Tkinter.Tk()
	# label=Tkinter.Message(add_task_window,)
	add_task_window.geometry("300x125+50+50")
	add_task_window.title("Add new task")

	vertical_frame=Tkinter.Frame(add_task_window)
	horizontal_frame_1=Tkinter.Frame(vertical_frame)
	horizontal_frame_2=Tkinter.Frame(vertical_frame)
	horizontal_frame_3=Tkinter.Frame(vertical_frame)
	horizontal_frame_4=Tkinter.Frame(vertical_frame)
	horizontal_frame_5=Tkinter.Frame(vertical_frame)
	horizontal_frame_6=Tkinter.Frame(vertical_frame)

	instructions=Tkinter.Message(horizontal_frame_1,
		text="Introduce info about task:",width=250)
	instructions.pack()

	line1_text=Tkinter.Label(horizontal_frame_2,text="Task name")
	line1_text.pack(side=LEFT,fill="x")
	line1_entry=Tkinter.Entry(horizontal_frame_2)
	line1_entry.pack(side=RIGHT)
	line2_text=Tkinter.Label(horizontal_frame_3,text="Priority")
	line2_entry=Tkinter.Entry(horizontal_frame_3)
	line2_text.pack(side=LEFT,fill="x")
	line2_entry.pack(side=RIGHT)
	line3_text=Tkinter.Label(horizontal_frame_4,
		text="Time required(hours)")
	line3_entry=Tkinter.Entry(horizontal_frame_4)
	line3_text.pack(side=LEFT,fill="x")
	line3_entry.pack(side=RIGHT)
	line4_text=Tkinter.Label(horizontal_frame_5,text="Deadline")
	line4_entry=Tkinter.Entry(horizontal_frame_5)
	line4_text.pack(side=LEFT,fill="x")
	line4_entry.pack(side=RIGHT)

	ok_button = Tkinter.Button(horizontal_frame_6,text="OK",
		command = lambda: getAddTaskEntries(line1_entry,
			line2_entry,line3_entry,line4_entry,add_task_window))
	# it works! retine faza cu lambda
	ok_button.pack()

	horizontal_frame_6.pack(side=BOTTOM)
	horizontal_frame_5.pack(side=BOTTOM)
	horizontal_frame_4.pack(side=BOTTOM)
	horizontal_frame_3.pack(side=BOTTOM)
	horizontal_frame_2.pack(side=BOTTOM)
	horizontal_frame_1.pack(side=BOTTOM)

	vertical_frame.pack()

	add_task_window.mainloop()
	return 0
# Se va afisa o fereastra ce contine campuri
# pentru introducerea de NAME, PRIORITY, TIME_REQ,
# DEADLINE, si butoane ok ce trimit raspunsurile
# in stringuri
# Functia returneaza in ordine stringurile
# name, priority, time_req, deadline

def getRemoveTaskEntries(line1_entry,line2_entry,
	line3_entry,remove_task_window):
	task_name=line1_entry.get()
	date=line2_entry.get()
	hour=line3_entry.get()
	confirmation_msg = tkMessageBox.showinfo("Info Received",
		"The information you introduced about the task was received.")
	remove_task_window.destroy()
	return [task_name, date, hour]
#functia primeste Entrierile din removeTask la apasarea
#butonului ok si imi intoarce ce stringuri au fost
#introduse prin ele, sub forma unei liste
#numele elementelor din lista sunt sugestive
#la final apare un mesaj care explica ca s-au primit
#informatile iar fereastra de introducere se distruge

def removeTask():
	remove_task_window=Tkinter.Tk()
	remove_task_window.geometry("300x125+50+50")
	remove_task_window.title("Remove task")

	vertical_frame=Tkinter.Frame(remove_task_window)
	horizontal_frame_1=Tkinter.Frame(vertical_frame)
	horizontal_frame_2=Tkinter.Frame(vertical_frame)
	horizontal_frame_3=Tkinter.Frame(vertical_frame)
	horizontal_frame_4=Tkinter.Frame(vertical_frame)
	horizontal_frame_5=Tkinter.Frame(vertical_frame)

	instructions=Tkinter.Message(horizontal_frame_1,
		text="""Introduce the task you want to remove""",
		width=500)
	instructions.pack()

	line1_text=Tkinter.Label(horizontal_frame_2,text="Task name")
	line1_text.pack(side=LEFT,fill="x")
	line1_entry=Tkinter.Entry(horizontal_frame_2)
	line1_entry.pack(side=RIGHT)
	line2_text=Tkinter.Label(horizontal_frame_3,text="Date (Optional)")
	line2_entry=Tkinter.Entry(horizontal_frame_3)
	line2_text.pack(side=LEFT,fill="x")
	line2_entry.pack(side=RIGHT)
	line3_text=Tkinter.Label(horizontal_frame_4,text="Hour (Optional)")
	line3_entry=Tkinter.Entry(horizontal_frame_4)
	line3_text.pack(side=LEFT,fill="x")
	line3_entry.pack(side=RIGHT)

	ok_button = Tkinter.Button(horizontal_frame_5,text="OK",
		command = lambda: getRemoveTaskEntries(line1_entry,
		line2_entry,line3_entry,remove_task_window))
	ok_button.pack()

	horizontal_frame_5.pack(side=BOTTOM)
	horizontal_frame_4.pack(side=BOTTOM)
	horizontal_frame_3.pack(side=BOTTOM)
	horizontal_frame_2.pack(side=BOTTOM)
	horizontal_frame_1.pack(side=BOTTOM)

	vertical_frame.pack()

	remove_task_window.mainloop()
	return 0
#imi va scoate un task din schedule (dupa nume)
# eventual si dupa data/ora pentru chestii repetitive

def getPostponeTaskEntries(line1_entry,line2_entry,
	line3_entry,postpone_task_window):
	task_name=line1_entry.get()
	date=line2_entry.get()
	hour=line3_entry.get()
	confirmation_msg = tkMessageBox.showinfo("Info Received",
		"The information you introduced about the task was received.")
	postpone_task_window.destroy()
	return [task_name, date, hour]
#functia primeste Entrierile din postponeTask la apasarea
#butonului ok si imi intoarce ce stringuri au fost
#introduse prin ele, sub forma unei liste
#numele elementelor din lista sunt sugestive
#la final apare un mesaj care explica ca s-au primit
#informatile iar fereastra de introducere se distruge

def postponeTask():
	postpone_task_window=Tkinter.Tk()
	postpone_task_window.geometry("300x125+50+50")
	postpone_task_window.title("Postpone task")

	vertical_frame=Tkinter.Frame(postpone_task_window)
	horizontal_frame_1=Tkinter.Frame(vertical_frame)
	horizontal_frame_2=Tkinter.Frame(vertical_frame)
	horizontal_frame_3=Tkinter.Frame(vertical_frame)
	horizontal_frame_4=Tkinter.Frame(vertical_frame)
	horizontal_frame_5=Tkinter.Frame(vertical_frame)

	instructions=Tkinter.Message(horizontal_frame_1,
		text="""Introduce the task you want to postpone""",
		width=500)
	instructions.pack()

	line1_text=Tkinter.Label(horizontal_frame_2,text="Task name")
	line1_text.pack(side=LEFT,fill="x")
	line1_entry=Tkinter.Entry(horizontal_frame_2)
	line1_entry.pack(side=RIGHT)
	line2_text=Tkinter.Label(horizontal_frame_3,text="Date (Optional)")
	line2_entry=Tkinter.Entry(horizontal_frame_3)
	line2_text.pack(side=LEFT,fill="x")
	line2_entry.pack(side=RIGHT)
	line3_text=Tkinter.Label(horizontal_frame_4,text="Hour (Optional)")
	line3_entry=Tkinter.Entry(horizontal_frame_4)
	line3_text.pack(side=LEFT,fill="x")
	line3_entry.pack(side=RIGHT)

	ok_button = Tkinter.Button(horizontal_frame_5,text="OK",
		command = lambda: getPostponeTaskEntries(line1_entry,
		line2_entry,line3_entry,postpone_task_window))
	ok_button.pack()

	horizontal_frame_5.pack(side=BOTTOM)
	horizontal_frame_4.pack(side=BOTTOM)
	horizontal_frame_3.pack(side=BOTTOM)
	horizontal_frame_2.pack(side=BOTTOM)
	horizontal_frame_1.pack(side=BOTTOM)

	vertical_frame.pack()

	#TO DO: adauga daca a fost cu succes sau nu postponarea
	postpone_task_window.mainloop()
	return 0
#imi postponeaza un task dupa nume
#eventual si dupa data si ora

def getModifyTaskEntries(line1_entry_left,
		line2_entry_left,line3_entry_left,line1_entry_right,
		line2_entry_right,line3_entry_right,line4_entry_right,
		modify_task_window):
	task_to_modify_name=line1_entry_left.get()
	task_to_modify_date=line2_entry_left.get()
	task_to_modify_hour=line3_entry_left.get()
	modified_name=line1_entry_right.get()
	modified_priority=line2_entry_right.get()
	modified_time_req=line3_entry_right.get()
	modified_deadline=line4_entry_right.get()
	confirmation_msg=tkMessageBox.showinfo("Info Received",
		"The information you introduced about the task was received.")
	modify_task_window.destroy()
	return [task_to_modify_name, task_to_modify_date, task_to_modify_hour,
			modified_name, modified_priority, modified_time_req,
			modified_deadline]

def modifyTask():
	modify_task_window=Tkinter.Tk()
	modify_task_window.geometry("600x125+50+50")
	modify_task_window.title("Postpone task")

	global_frame=Tkinter.Frame(modify_task_window)
	vertical_frame_left=Tkinter.Frame(global_frame)
	horizontal_frame_1_left=Tkinter.Frame(vertical_frame_left)
	horizontal_frame_2_left=Tkinter.Frame(vertical_frame_left)
	horizontal_frame_3_left=Tkinter.Frame(vertical_frame_left)
	horizontal_frame_4_left=Tkinter.Frame(vertical_frame_left)
	horizontal_frame_5_left=Tkinter.Frame(vertical_frame_left)
	vertical_frame_right=Tkinter.Frame(global_frame)
	horizontal_frame_1_right=Tkinter.Frame(vertical_frame_right)
	horizontal_frame_2_right=Tkinter.Frame(vertical_frame_right)
	horizontal_frame_3_right=Tkinter.Frame(vertical_frame_right)
	horizontal_frame_4_right=Tkinter.Frame(vertical_frame_right)
	horizontal_frame_5_right=Tkinter.Frame(vertical_frame_right)
	horizontal_frame_6_right=Tkinter.Frame(vertical_frame_right)

	instructions_left=Tkinter.Message(horizontal_frame_1_left,
		text="""Introduce the task you want to modify""",
		width=500)
	instructions_left.pack()
	line1_text_left=Tkinter.Label(horizontal_frame_2_left,text="Task name")
	line1_text_left.pack(side=LEFT,fill="x")
	line1_entry_left=Tkinter.Entry(horizontal_frame_2_left)
	line1_entry_left.pack(side=RIGHT)
	line2_text_left=Tkinter.Label(horizontal_frame_3_left,text="Date (Optional)")
	line2_entry_left=Tkinter.Entry(horizontal_frame_3_left)
	line2_text_left.pack(side=LEFT,fill="x")
	line2_entry_left.pack(side=RIGHT)
	line3_text_left=Tkinter.Label(horizontal_frame_4_left,text="Hour (Optional)")
	line3_entry_left=Tkinter.Entry(horizontal_frame_4_left)
	line3_text_left.pack(side=LEFT,fill="x")
	line3_entry_left.pack(side=RIGHT)

	instructions_right=Tkinter.Message(horizontal_frame_1_right,
		text="""Introduce the new info about the task.""",
		width=500)
	instructions_right.pack()
	line1_text_right=Tkinter.Label(horizontal_frame_2_right,text="Task name")
	line1_text_right.pack(side=LEFT,fill="x")
	line1_entry_right=Tkinter.Entry(horizontal_frame_2_right)
	line1_entry_right.pack(side=RIGHT)
	line2_text_right=Tkinter.Label(horizontal_frame_3_right,text="Priority")
	line2_entry_right=Tkinter.Entry(horizontal_frame_3_right)
	line2_text_right.pack(side=LEFT,fill="x")
	line2_entry_right.pack(side=RIGHT)
	line3_text_right=Tkinter.Label(horizontal_frame_4_right,
		text="Time required(hours)")
	line3_entry_right=Tkinter.Entry(horizontal_frame_4_right)
	line3_text_right.pack(side=LEFT,fill="x")
	line3_entry_right.pack(side=RIGHT)
	line4_text_right=Tkinter.Label(horizontal_frame_5_right,text="Deadline")
	line4_entry_right=Tkinter.Entry(horizontal_frame_5_right)
	line4_text_right.pack(side=LEFT,fill="x")
	line4_entry_right.pack(side=RIGHT)

	ok_button = Tkinter.Button(horizontal_frame_5_left,text="OK",
		command = lambda: getModifyTaskEntries(line1_entry_left,
		line2_entry_left,line3_entry_left,line1_entry_right,
		line2_entry_right,line3_entry_right,line4_entry_right,
		modify_task_window))
	ok_button.pack()

	horizontal_frame_5_left.pack(side=BOTTOM)
	horizontal_frame_4_left.pack(side=BOTTOM)
	horizontal_frame_3_left.pack(side=BOTTOM)
	horizontal_frame_2_left.pack(side=BOTTOM)
	horizontal_frame_1_left.pack(side=BOTTOM)
	horizontal_frame_6_right.pack(side=BOTTOM)
	horizontal_frame_5_right.pack(side=BOTTOM)
	horizontal_frame_4_right.pack(side=BOTTOM)
	horizontal_frame_3_right.pack(side=BOTTOM)
	horizontal_frame_2_right.pack(side=BOTTOM)
	horizontal_frame_1_right.pack(side=BOTTOM)

	vertical_frame_right.pack(side=RIGHT)
	vertical_frame_left.pack(side=LEFT)
	global_frame.pack()

	#TO DO: adauga daca a fost cu succes sau nu postponarea
	modify_task_window.mainloop()
	return 0
# imi modifica un task dupa nume

top=Tkinter.Tk()
button_frame_global=Tkinter.Frame(top)
button_frame_line1=Tkinter.Frame(button_frame_global)
button_frame_line2=Tkinter.Frame(button_frame_global)
but1=Tkinter.Button(button_frame_line2,text="<<day",command=prevDay)
but2=Tkinter.Button(button_frame_line2,text="day>>",command=nextDay)
but3=Tkinter.Button(button_frame_line1,text="Add task",command=addTask)
but4=Tkinter.Button(button_frame_line1,text="Remove task",command=removeTask)
but5=Tkinter.Button(button_frame_line1,text="Postpone task",command=postponeTask)
but6=Tkinter.Button(button_frame_line1,text="Modify task",command=modifyTask)
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
but3.pack(side=LEFT)
but4.pack(side=LEFT)
but5.pack(side=RIGHT)
but6.pack(side=RIGHT)
button_frame_line1.pack(side=TOP)
button_frame_line2.pack(side=BOTTOM)
button_frame_global.pack()
text_schedule.pack()
top.mainloop()