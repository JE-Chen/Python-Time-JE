import datetime

from Models.Time_Calendar import Time_Calendar
from Models.Time_difference import Time_difference

class Time_Core():

    def __init__(self):
        try:
            self.Time_Calendar=Time_Calendar()
            self.Time_difference=Time_difference()
        except Exception as Errr :
            print(Errr)
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')