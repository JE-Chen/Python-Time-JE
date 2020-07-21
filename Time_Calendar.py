import calendar
import time

class Time_Calendar():

    def __init__(self):
        pass

    def Get_Year_Calendar(self):
        return calendar.calendar(int(time.strftime("%Y")))

    def Get_Month_Calendar(self):
        return calendar.month(int(time.strftime("%Y")),int(time.strftime("%m")))

    def Is_Leap(self,Year):
        return calendar.isleap(Year)

    def Leaps(self,Year1,Year2):
        return calendar.leapdays(Year1,Year2)