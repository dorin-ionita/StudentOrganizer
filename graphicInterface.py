#!/usr/bin/python

# structura fisierului este 3 butoane intr-un widget
# butoanele de mutat pe zile in alt widget
# widgetul cu zile pus sub ala cu 3 butoane
# un text boox mai jos unde se afiseaza date

import Tkinter
from Tkinter import *
import tkMessageBox
import Tix
import time
import datetime
import mySqlDBInterface
import scheduler

def nextDay(raw_data,window):
	#raw data e data in format datetime.datetime
	#string data e data convertita la string (doar data)
	#-de aia am sliceul de la 0 la 10
	raw_data += datetime.timedelta(days=1)
	string_data=str(raw_data)[0:10]
	schedule=mySqlDBInterface.getScheduleForDate(string_data)
	window.destroy()
	showMainWindow(string_data,raw_data,schedule)
	return 0
# Se va afisa ce este schedulat pentru ziua urmatoare,
# daca este schedulat ceva.
# Se distruge vechea fereastra principala si se creeaza
# una noua cu aceste date.

def prevDay(raw_data,window):
	current_date_raw = datetime.datetime.now()
	if current_date_raw > raw_data :
		return 0
	else :
		raw_data -= datetime.timedelta(days=1)
		string_data = str(raw_data)[:10]
		schedule = mySqlDBInterface.getScheduleForDate(string_data)
		window.destroy()
		showMainWindow(string_data,raw_data,schedule)
		return 0
	return 0
# Se va afisa ce este schedulat pentru ziua anterioara,
# daca este schedulat ceva.

def getAddTaskEntries(line1_entry,line2_entry,
	line3_entry,line4_entry,add_task_window):
	task_name = line1_entry.get()
	priority = line2_entry.get()
	time_req = line3_entry.get()
	deadline = line4_entry.get()
	mySqlDBInterface.addTask(task_name,priority,
		time_req,deadline)
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
# in stringuri.
# Functia returneaza in ordine stringurile
# name, priority, time_req, deadline.
# De asemenea, se adauga in baza de date printr-un
# apel al unei functii din mySqlDBInterface

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

def getModifyTaskEntries(line1_entry_left,line2_entry_left,
	line3_entry_left,line1_entry_right,line2_entry_right,
	line3_entry_right,line4_entry_right,modify_task_window):
	task_to_modify_name=line1_entry_left.get()
	task_to_modify_date=line2_entry_left.get()
	task_to_modify_hour=line3_entry_left.get()
	modified_name=line1_entry_right.get()
	modified_priority=line2_entry_right.get()
	modified_time_req=line3_entry_right.get()
	modified_deadline=line4_entry_right.get()
	mySqlDBInterface.modifyTask(task_to_modify_name,
		task_to_modify_date,task_to_modify_hour,
		modified_name,modified_priority,
		modified_time_req,modified_deadline)
	confirmation_msg=tkMessageBox.showinfo("Info Received",
		"The information you introduced about the task was received.")
	modify_task_window.destroy()
	return [task_to_modify_name, task_to_modify_date, task_to_modify_hour,
			modified_name, modified_priority, modified_time_req,
			modified_deadline]
# Se preiau stringurile introduse in fereastra
# modify entry

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
# in stanga se va primii taskul de modificat
# iar in dreapta modificarile taskului
# TO DO: adaugata functionalitate (dar in scheduler nu aici)
# 		care sa imi ia campurile goale introduse ca fiind
#		campuri ce nu se doresc modificate 

def refresh(window,data_for_schedule,schedule_list):
	window.destroy()
	#instructiunea urmatoare trebuie modificata in versiunea
	#finala, sa nu ia din tasks, sa ia din schedule
	scheduler.initSchedule()
	schedule_list=mySqlDBInterface.getTasksFromDB()
	showMainWindow(str(data_for_schedule)[:10],
		data_for_schedule,schedule_list)
	# primele 10 caractere din data e ce ma intereseaza
	# (data propriuzisa)
	return 0
# implementeaza butonul de refresh
# distruge fereastra principala si recreeaza alta
# eventual cu alt schedule:D 

def showMainWindow(data_for_schedule,data_for_schedule_raw,
	schedule_list):
	# print type(data_for_schedule)
	# print type(data_for_schedule_raw)
	# print type(schedule_list)
	# print "\n"
	top=Tkinter.Tk()
	top.geometry("500x480+1+1")
	top.title("Time and money management software")
	top.resizable(0,0)
	# top.configure(background='white')

	vertical_frame=Tkinter.Frame(top)

	button_frame_global=Tkinter.Frame(vertical_frame)
	button_frame_line1=Tkinter.Frame(button_frame_global)
	button_frame_line2=Tkinter.Frame(button_frame_global)
	but1=Tkinter.Button(button_frame_line2,text="<<day",
		command= lambda: prevDay(data_for_schedule_raw,top))
	but2=Tkinter.Button(button_frame_line2,text="day>>",
		command= lambda: nextDay(data_for_schedule_raw,top))
	but3=Tkinter.Button(button_frame_line1,text="Add task",
		command=addTask)
	but4=Tkinter.Button(button_frame_line1,text="Remove task",
		command=removeTask)
	but5=Tkinter.Button(button_frame_line1,text="Postpone task",
		command=postponeTask)
	but6=Tkinter.Button(button_frame_line1,text="Modify task",
		command=modifyTask)
	but7=Tkinter.Button(button_frame_line2,text="Refresh",
		command = lambda: refresh(top,data_for_schedule_raw,schedule_list))

	title_text="The schedule for: "+data_for_schedule
	schedule_title=Tkinter.Message(vertical_frame,text=title_text,
		width=620)

	schedule_frame=Tkinter.Frame(vertical_frame,
		borderwidth=2,relief=SUNKEN)
	i=0
	for task in schedule_list:
		j=0
		for detail in task:
			Tkinter.Label(schedule_frame,text='%s'%(detail),
				borderwidth=10).grid(row=i,column=j)
			j=j+1
		i=i+1
	but1.pack(side=LEFT)
	but7.pack(side=LEFT)
	but2.pack(side=RIGHT)
	but3.pack(side=LEFT)
	but4.pack(side=LEFT)
	but5.pack(side=RIGHT)
	but6.pack(side=RIGHT)

	schedule_frame.pack(side=BOTTOM)
	# scrollbar.config(command=schedule_frame.yview)
	button_frame_line1.pack(side=TOP)
	schedule_title.pack(side=BOTTOM)
	button_frame_line2.pack(side=BOTTOM)
	button_frame_global.pack(side=BOTTOM)

	vertical_frame.pack()
	top.mainloop()
# afiseaza tot ce tine de fereastra principala