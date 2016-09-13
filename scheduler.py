#!/usr/bin/python

import time
import mySqlDBInterface
from datetime import timedelta, date
import datetime

def getFromDB():
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

def initSchedule () :
	[tasks,timetable,schedule] = getFromDB()
	mySqlDBInterface.deleteAllEntriesInTabel("schedule")
	return 0
