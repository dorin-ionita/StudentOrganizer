#!/usr/bin/python

import time
import mySqlDBInterface
from datetime import timedelta, date

def getFromDB(tasks,timetable,schedule):
	tasks = mySqlDBInterface.getTasksFromDB()
	timetable = mySqlDBInterface.getTimetableFromDB()
	schedule = mySqlDBInterface.getScheduleFromDB()
	# print tasks[0][0] # de exemplu aceasta comanda imi afiseaza
	# 				  # prima celula din tabel
	# Sunt puse sub forma unei matrice.
	# Cel mai pe romaneste zis: tabelul e trasnpus in matrice, iar
	# matricea arata la fel ca tabelul, dar nu are capul sau
	# iar numaratoare in matrice incepe de la 0,0 (stanga sus)
	
	# print schedule # daca schedule este gol tupletul asta este gol, 
	# 			   # sau lista..ce mama ei o fi
	
	# Momentan sunt tuple. Le vreau liste, sa le pot edita
	tasks = [list(x) for x in tasks]
	timetable = [list(x) for x in timetable]
	schedule = [list(x) for x in schedule]
	
	# print type(tasks)
	# print tasks[1][4]
	# # tasks [1][4] este de tip datetime.date, adica asta e tipul datei
	# # din baza de date, tipul in python
	# print tasks
	# print '\n'
	# print timetable
	# print type(timetable[0][2])
	return (tasks,timetable,schedule)
	# print type(tasks[1][4])
# imi returneaza din baza de date tasks, timetable,
# schedule in format de matrice ca lista de liste

def existsTaskinSchedule(task,schedule):
	list=[tsk for tsk in schedule[][4]==task]
	if len(list)!=0:
		return 1
	else:
		return 0
	return 0
# imi returneaza daca taskul a fost schedulat
# (daca se afla in tabela schedule)

def dateRange (start_date, end_date):
	for n in range(int((end_date - start_date).days)):
		yield start_date + timedelta(n)
# imi creeaza un Range de date intre start_date
# si end_date cu incrementare de 1 zi

def timeRange (start_time,end_time):
	for n in range(int((end_time - start_time).hour)):
		yield start_time + timedelta(n)
# imi creeaza un Range de timp intre start_date
# si end_date cu incrementare de 1 ora


def scheduleTimetable(timetable,schedule):
	current_day = time.strftime("%d-%m-%s")
	for task in timetable:
		if existsTaskinSchedule(task[4],schedule):
			continue
		else:
			for date in dateRange(current_day,"2017-12-31"):
				if date.weekday()==task[1]:
					addScheduleInDB(len(timetable)+1,date,
						task[2],task[3],task[4],0)
					getFromDB(task,timetable,schedule)
					#adaugat ca nepostponable
			# mySqlDBInterface.addScheduleInDB(len(timetable)+1,datetime,
			# 	)
		# else:
		# 	for date in dateRange(current_day,"2017-12-31"):
		# 		for hour in timeRange("00.00","23.00"):
		# 			if timeAndDateBusy(date,hour,schedule)!=0 :
		# 				mySqlDBInterface.addScheduleInDB(len(timetable),datetime,
		# 					hour,task[])
# presupunand ca tabela schedule este goala
# (adica nu se vor face alte verificari)
# imi este introdus orarul pana la sfarsitul anului
# in aceasta tabela (este schedulat orarul,
# inclusiv programul de somn)

def scheduleTasks (tasks,schedule):
	current_day = time.strftime("%d-%m-%s")
	for task in tasks:
		if existsTaskinSchedule(task[1],schedule):
			continue
		else:
			for date in dateRange(current_day,"2017-12-31"):
				for hour in timeRange("11.00","23.00"):
					if timeAndDateBusy(date,hour,schedule)==0 :
						mySqlDBInterface.addScheduleInDB(len(timetable)+1,date,
							task[2],task[3],task[4],0)
						getFromDB(task,timetable,schedule)
# daca taskul nu exista in schedul este
# schedulat pe prima pozitie libera 
# (postponabale=0, nu se verifica prioritatea)