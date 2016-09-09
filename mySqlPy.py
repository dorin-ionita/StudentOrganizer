#!/usr/bin/python

import MySQLdb

# baza de date: studentorganizer
# localhost, root, ionita
# baza de date contine:
# 1.tabela tasks
# 	contine taskurile neschedulite
# 	0. ID int
# 	1. NAME char
# 	2. PRIORITY int
# 	3. TIME_REQ float
# 	4. DEADLINE datetime.date
# 2.tabela timetable
# 	contine orarul si taskurile repetitive
# 	(de genul somn)
# 	0. ID int
# 	1. DAY char
# 	2. START_HOUR ?
# 	3. END_HOUR ?
# 	4. NAME char
# 	5. PARITY int
# 3.tabela schedule
# 	contine programul asa cum a fost facut de programul
# 	de aici voi pune in GUI
# 	0. ID int
# 	1. DATE datetime.date
# 	2. START_HOUR Time/datetime.timedelta
# 	3. END_HOUR Time/datetime.timedelta
# 	4. NAME char
# 	5. POSTPON int

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