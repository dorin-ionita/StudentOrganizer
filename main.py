#!/usr/bin/python

import graphicInterface
import mySqlDBInterface

x=mySqlDBInterface.getTimetableFromDB()

print x

graphicInterface.showMainWindow("2016-11-15",x)