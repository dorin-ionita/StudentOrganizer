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

def initSchedule () :
	[tasks,timetable,schedule] = getFromDB()
	mySqlDBInterface.deleteAllEntriesInTabel("schedule")
	[tasks,timetable,schedule]=getFromDB()
	# pana aici functioneaza perfect
	addFromTimetableToSchedule(timetable)
	[tasks,timetable,schedule]=getFromDB()
	# print schedule
	# schedule = addFromTasksToSchedule(tasks,schedule)			#TO DO
	return 0
# imi creeeaza scheduleul, pe baza Timetable si Tasks
