#!/usr/bin/python

import time
import mySqlDBInterface
from datetime import timedelta, date
from datetime import datetime
import datetime
import pandas  #pentru data_range
from dateutil import parser #pentru coversie str->datetime

def getFromDB() :
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
	return [tasks,timetable,schedule]
	# print type(tasks[1][4])
# imi returneaza din baza de date tasks, timetable,
# schedule in format de matrice ca lista de liste

def offset() :
	cfg_start_date_file = open("./cfg/start_date.cfg","r")
	start_date = cfg_start_date_file.read()
	#start_date = datetime.strptime(start_date,'%Y-%m-%d')
	start_date = parser.parse(start_date)
	#am convertit in date_time
	parity = start_date.isocalendar()[1] % 2
	# in start_date.isocalendar()[1] se gaseste numarul 
	# saptamanii din an
	# parity este 0 pentru para, 1 impara

	#Daca incep cu saptamana para (masura de la an)
	#atunci pentru a corela saptamana para (masurata de la an)
	#cu saptamana impara (ca doar incepe cu 1, de la anul
	# universitar) este necesar sa transform pe cea impara
	# in para, adica sa scad -1. offset=-1
	#Daca au aceiasi paritate atunci offsetul este 0
	return parity

# offsetu imi egalizeaza saptamana calendaristica cu saptamana
# univeristara. Offsetul se adauga la paritatea saptamanii
# calendaristice pentru a o transforma in paritatea saptamanii
# univeristare
# Functia imi returneaza offsetul(0 sau 1)

def decideDateParity(date) :
	# convertesc pe date care acum e str la datetime
	date = parser.parse(date)
	parity = date.isocalendar()[1] % 2 + offset()
	#din experienta trebuie reversat 1 sa devina 0 si 0 1
	# de ce dracu' nu stiu...
	parity^=1  # xor cu 1
	return parity
# Imi decide ce fel de paritate are saptamana (paritate ca saptamana
# unversitara)

def addFromTimetableToSchedule(timetable) :
	# planificator pe 90 de zile
	# dar ce fac daca am si date trecute?! neindeplinite
	current_date = datetime.datetime.now()
	end_date = current_date + datetime.timedelta(days=90)
	#DEBUG: current_date si end_date par ok
	for date in pandas.date_range(current_date,end_date) :
		# pentru fiecare data de acum pana la urmatoarele 90 de zile
		# vad ce zi e sa stiu cum adaug in program.
		# Functia trebuie sa primeasca date ca string,
		# deci le convertesc:
		day_week=date.weekday()
		day_week=str(day_week)
		#DEBUG: day_week evolueaza corect
		date = str(date)[:10]
		#DEBUG: date evolueaza ok
		mySqlDBInterface.addTaskToScheduleForDayWeek(date,day_week)
		#date si day_week sunt trimise ca stringuri
	return 0   #?TO DO
# functia imi adauga din timetable in schedule
# adica imi scheduleaza timetabelu
# nu intoarce nimic, doar modifica baza de date

def removeFromListWhatIsNotDatetime(deadlines) :
	for deadline in deadlines :
		if isinstance(deadline,datetime.date) :
			continue
		else :
			deadlines.remove(deadline)
	# retine si asta
	if not isinstance(deadlines[len(deadlines)-1],datetime.date) :
		deadlines.remove(deadlines[len(deadlines)-1])
	# removez ce a fost introdus gol, ultima nu stiu de ce nu a vrut
	return deadlines
# imi scoate dintr-o lista tot ce nu este de tipul
# datetime.date.
# Primeste lista ca parametru si o intoarce fara orice altceva
# inafara de datetime.date
# USELESS

def removeFromListWhatIsNotString(priorities) :
	for priority in priorities :
		if isinstance(priority,string) :
			continue
		else :
			priorities.remove(priority)
	if not isinstance(priorities[len(priorities)-1],string) :
		priorities.remove(priorities[len(priorities)-1])
	return priorities
# analog functiei de mai sus, dar cu string, nu datetime
# USELESS

def removeFromListWhatHasNoDeadlineOrPriority(tasks) :
	for task in tasks :
		if ( isinstance(task[2],str) or 
			isinstance(task[4],datetime.date) ) :
			continue
		else :
			tasks.remove(task)
	# if ((not isinstance(tasks[len(tasks)-1][2],str)) or
	# 	(not isinstance(tasks[len(tasks)-1][4],datetime.date)) ) :
	# 	tasks.remove(tasks[len(tasks)-1])
	return tasks
# DEBUG: It works just fine
# imi elimina din lista de taskuri pe cele pentru care nu exista
# date despre deadline sau despre prioritate
# TO DO: fa prioritate by default 0, iar deadline=90zile

def addFromTasksToSchedule(tasks) :
	# print tasks
	# deadlines = [ deadline[4] for deadline in tasks ]
	# deadlines = removeFromListWhatIsNotDatetime(deadlines)
	# priorities = [ priority[2] for priority in tasks ]
	# priorities = removeFromListWhatIsNotString(priorities)
	# #TO DO: trebuie ordonata lista
	tasks = removeFromListWhatHasNoDeadlineOrPriority(tasks)
	# am scapat de taskurile neconforme
	return 0
# analog addFromTimetableToSchedule

def initSchedule () :
	mySqlDBInterface.deleteAllEntriesInTabel("schedule")
	[tasks,timetable,schedule]=getFromDB()
	# DEBUG:pana aici functioneaza perfect
	addFromTimetableToSchedule(timetable)
	[tasks,timetable,schedule]=getFromDB()
	
	addFromTasksToSchedule(tasks)


	# e nevoie sa recitesc pt ca s-a modificat schedule
	
	# DEBUG:pare ca merge pana aici
	# print schedule
	# schedule = addFromTasksToSchedule(tasks,schedule)			#TO DO
	return 0
# imi creeeaza scheduleul, pe baza Timetable si Tasks
