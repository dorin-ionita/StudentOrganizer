#!/usr/bin/python

import graphicInterface
import mySqlDBInterface
import time
import datetime

current_date_raw = datetime.datetime.now() 
#este de tip datetime.datetime
current_date_string=str(current_date_raw)[0:10]

#DOAR PENTRU TEST:
schedule=mySqlDBInterface.getTasksFromDB()
graphicInterface.showMainWindow(current_date_string,
	current_date_raw,schedule)

#OFICIAL:
# schedule = mySqlDBInterface.getScheduleForDate(current_date_string)
# graphicInterface.showMainWindow(current_date_string,
#	current_date_raw,schedule)