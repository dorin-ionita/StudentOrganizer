#!/usr/bin/python

import MySQLdb

def getTasksFromDB():
	#Aceasta functie imi returneaza taskurile
	#din baza de date
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()

	#trebuie tratat separat fiecare tabel.
	#Pentru inceput presupun ca tabelele exista
	#si ca au structura ceruta, voi modifica 
	#mai apoi sa se creeze de aici.
	#Observatie:DB nu se poate creea de aici
	
	#1.tabelul tasks

	cursor.execute("SELECT * FROM tasks")
	tasks = cursor.fetchall ()
	# for task in tasks:
	# 	#parcurg fiecare rand
	# 	print task[0], "\n"	#ID			int
	# 	print task[1], "\n"	#NAME		char
	# 	print task[2], "\n"	#PRIORITY	int
	# 	print task[3], "\n"	#TIME_REQ	float
	# 	print task[4], "\n"	#DEADLINE	datetime.date
	db.close()
	return tasks
	#se da 0L daca nu merge

def getTimetableFromDB():
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM timetable")
	timetable = cursor.fetchall()
	# for day in timetable:
	# 	print day[0], "\n" #ID			int
	# 	print day[1], "\n" #DAY 		char
	# 	print day[2], "\n" #START_HOUR	?
	# 	print day[3], "\n" #END_HOUR	?
	# 	print day[4], "\n" #NAME		char
	# 	print day[5], "\n" #PARITY		int
	db.close()
	return timetable

def getScheduleFromDB():
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM schedule")			
	schedule = cursor.fetchall ()
	# for task in schedule:
	# 	print task[0], "\n" #ID			int
	# 	print task[1], "\n" #DATE 		datetime.date
	# 	print task[2], "\n" #START_HOUR	?
	# 	print task[3], "\n" #END_HOUR	?
	# 	print task[4], "\n" #NAME		char
	# 	print task[5], "\n" #POSTPON 	int
	db.close()
	return schedule

def getScheduleForDate(date):
	db = MySQLdb.connect("localhost","root",
		"ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("""SELECT * FROM schedule
		WHERE DATE='%s'"""%date)
	# CE HAL DE SINTAXA! keep this one in mind
	# HOW THE FUCK IS IT EVEN POSSIBLE TO WORK?!
	print "Debug 3.2"
	schedule = cursor.fetchall()
	db.close()
	return schedule

#functile ce pot modifica in baza de date sunt:
#changeScheduleInDB (modifica o linie)--!! adauga si la celelalte tabele
def changeScheduleInDB(ID,DATE,START_HOUR,END_HOUR,NAME,POSTPONABLE):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	#cum sa updatez dateul si orele?
	DATE=str(DATE)
	START_HOUR=str(START_HOUR)
	END_HOUR=str(END_HOUR)
	cursor.execute("""UPDATE schedule
					SET NAME=%s POSTPONABLE=%d
					DATE=%s START_HOUR=%s END_HOUR=%s 
					WHERE ID=%d """,
					NAME,POSTPONABLE,ID,DATE,START_HOUR,END_HOUR)
	db.commit()
	db.close()

def delScheduleInDB(ID): #sterge pe bune!
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("""DELETE FROM schedule
					WHERE ID=%D""",ID)
	db.commit()
	db.close()

def addScheduleInDB(ID,DATE,START_HOUR,END_HOUR,NAME,POSTPONABLE):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	DATE=str(DATE)
	START_HOUR=str(START_HOUR)
	END_HOUR=str(END_HOUR)
	cursor.execute("""INSERT INTO schedule
					VALUES (%d,%s,%s,%s,%s,%d)""",
					ID,DATE,START_HOUR,END_HOUR,NAME,POSTPONABLE)
	db.commit()
	db.close()


def changeTaskInDB(ID,NAME,PRIORITY,TIME_REQ,DEADLINE):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	#cum sa updatez dateul si orele?
	DEADLINE=str(DEADLINE)
	cursor.execute("""UPDATE tasks
					SET NAME=%s PRIORITY=%d TIME_REQ=%f DEADLINE=%s
					WHERE ID=%d """,
					NAME,PRIORITY,TIME_REQ,DEADLINE,ID)
	db.commit()
	db.close()

def delTaskInDB(ID):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("""DELETE FROM tasks
					WHERE ID=%D""",ID)
	db.commit()
	db.close()

def addTaskInDB(ID,NAME,PRIORITY,TIME_REQ,DEADLINE):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	DEADLINE=str(DEADLINE)
	cursor.execute("""INSERT INTO tasks
					VALUES (%d,%s,%d,%f,%s)""",
					ID,NAME,PRIORITY,TIME_REQ,DEADLINE)
	db.commit()
	db.close()


def changeTimetableInDB(ID,DAY,START_HOUR,END_HOUR,NAME,PARITY):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	#cum sa updatez dateul si orele?
	START_HOUR=str(START_HOUR)
	END_HOUR=str(END_HOUR)
	cursor.execute("""UPDATE timetable
					SET ID=%d DAY=%s START_HOUR=%s END_HOUR=%s
						NAME=%s PARITY=%d
					WHERE ID=%d """,
					ID, DAY, START_HOUR, END_HOUR, NAME, PARITY)
	db.commit()
	db.close()

def delTimetableInDB(ID):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	cursor.execute("""DELETE FROM timetable
					WHERE ID=%D""",ID)
	db.commit()
	db.close()

def addTimetableInDB(ID,DAY,START_HOUR,END_HOUR,NAME,PARITY):
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	START_HOUR=str(START_HOUR)
	END_HOUR=str(END_HOUR)
	cursor.execute("""INSERT INTO timetable
					VALUES (%d,%s,%s,%s,%s,%d)""",
					ID,DAY,START_HOUR,END_HOUR,NAME,PARITY)
	db.commit()
	db.close()

#NIMIC DE AICI NU A FOST TESTAT!

########################################################################

def addTask(task_name,priority,time_req,deadline) :
	db = MySQLdb.connect("localhost",
		"root","ionita","studentorganizer")
	cursor = db.cursor()
	task_name=str(task_name)
	priority=str(priority)
	time_req=str(time_req)
	deadline=str(deadline)
	cursor.execute("""SELECT * FROM tasks""")
	tasks=cursor.fetchall()
	tasks=int(len(tasks))+1
	cursor.execute("""INSERT INTO tasks
					VALUES ('%s','%s','%s','%s','%s')"""
					%(tasks,task_name,priority,time_req,deadline))
	db.commit()
	db.close()
	return 0
	#note. it worked just fain
# functia ce va fi apelata la apasarea OK din butonul addTask

def modifyTask (task_to_modify_name,task_to_modify_date,
	task_to_modify_hour,
	modified_name,modified_priority,modified_time_req,
	modified_deadline) :
	db = MySQLdb.connect("localhost","root","ionita",
		"studentorganizer")
	cursor = db.cursor()
	task_to_modify_name = str(task_to_modify_name)
	task_to_modify_date = str(task_to_modify_date)
	task_to_modify_hour = str(task_to_modify_hour)
	# date si hour nu au importanta :D
	modified_name = str(modified_name)
	modified_priority = str(modified_priority)
	modified_time_req = str(modified_time_req)
	modified_deadline = str(modified_deadline)
	if modified_name :
		cursor.execute("""UPDATE tasks SET NAME='%s'
						WHERE NAME='%s'"""
						%(modified_name,task_to_modify_name))
	if modified_priority :
		cursor.execute("""UPDATE tasks SET PRIORITY='%s'
						WHERE NAME='%s'"""
						%(modified_priority,task_to_modify_name))
	if modified_time_req :
		cursor.execute("""UPDATE tasks SET TIME_REQ='%s'
						WHERE NAME='%s'"""
						%(modified_time_req,task_to_modify_name))
	if modified_deadline :
		cursor.execute("""UPDATE tasks SET DEADLINE='%s'
						WHERE NAME='%s'"""
						%(modified_deadline,task_to_modify_name))
	db.commit()
	db.close()
	return 0
	#note. pare sa mearga
# functia ce va fi apelata la apasarea OK din butonul modifyTask