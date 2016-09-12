#!/usr/bin/python

import graphicInterface
import mySqlDBInterface
import time

print(datetime.datetime.now())
print(type(datetime.datetime.now()))

current_date=time.strftime("%Y-%m-%d")
print type(time.strftime("%Y-%m-%d"))

#DOAR PENTRU TEST:
schedule=mySqlDBInterface.getTimetableFromDB()
graphicInterface.showMainWindow(current_date,schedule)

#OFICIAL:
# schedule = mySqlDBInterface.getScheduleForDate(current_date)
# graphicInterface.showMainWindow(current_date,schedule)
