#!/usr/bin/python

import graphicInterface
import mySqlDBInterface
import scheduler
import time
import datetime

# #fisierul de configuratie:
# cfg_file = open ("./cfg/database_authentication.cfg","r")
# host=cfg_file.read(14)
# host=host[5:]				 #sa tai host=din fata
# cfg_file.read(1) 			 #pentru \n
# username=cfg_file.read(13)
# username=username[9:]
# cfg_file.read(1)
# password=cfg_file.read(15)
# password=password[9:]
# cfg_file.close()
# print host
# print username
# print password

current_date_raw = datetime.datetime.now() 
#este de tip datetime.datetime
current_date_string=str(current_date_raw)[0:10]
#am obtinut data de care am nevoie

scheduler.initSchedule()
#am initiat schedule

#DOAR PENTRU TEST:
schedule=mySqlDBInterface.getTasksFromDB()
graphicInterface.showMainWindow(current_date_string,
	current_date_raw,schedule)

#OFICIAL:
# schedule = mySqlDBInterface.getScheduleForDate(current_date_string)
# graphicInterface.showMainWindow(current_date_string,
#	current_date_raw,schedule)