import time
import datetime
import threading
from  threading import Timer
from apscheduler.schedulers.background import BackgroundScheduler

'''
轉義符對應意義如下

%a 本地簡化星期名稱

%A 本地完整星期名稱

%b 本地簡化的月份名稱

%B 本地完整的月份名稱

%c 本地相應的日期表示和時間表示

%d 月內中的一天（0-31）

%H 24小時制小時數（0-23）

%I 12小時制小時數（01-12）

%j 年內的一天（001-366）

%m 月份（01-12）

%M 分鐘數（00=59）

%p 本地A.M.或P.M.的等價符

%S 秒（00-59）

%U 一年中的星期數（00-53）星期天為星期的開始

%w 星期（0-6），星期天為星期的開始

%W 一年中的星期數（00-53）星期一為星期的開始

%x 本地相應的日期表示

%X 本地相應的時間表示

%y 兩位數的年份表示（00-99）

%Y 四位數的年份表示（000-9999）

%Z 當前時區的名稱

%% %號本身
'''


class Time_difference(threading.Thread):

    def __init__(self):
        super().__init__()
        self.scheduler=BackgroundScheduler()
        self.Work=True
        self.Now_Time=datetime.datetime.now()
        self.Sleep_Time=10
        self.setDaemon(True)

    def Set_Sleep_Time(self,Sleep_Time):
        self.Sleep_Time=Sleep_Time

# ----------------------------------------------------------------------------------------------

    #run 一個方法 直到旗標更改
    def Just_Delay_And_Job(self,Object,Delay_Time,Stop_Flag):
        self.run(Object,Delay_Time,Stop_Flag)


    def run(self,Object,Delay_Time,Stop_Flag) -> None:
            while(Stop_Flag):
                Object()
                time.sleep(Delay_Time)

# ----------------------------------------------------------------------------------------------

    #得到當前日期
    def Get_Now(self):
        return time.strftime("%c")

    #得到本地當前日期
    def Get_Now_Local(self):
        return time.strftime("%x")

    #得到當前年
    def Get_Now_Year(self):
        return time.strftime("%Y")

    #得到當前月份
    def Get_Now_Mon(self):
        return time.strftime("%m")

    #得到當前是第幾天
    def Get_Now_Day(self):
        return time.strftime("%d")

    #得到當前小時
    def Get_Now_Hour(self):
        return time.strftime("%H")

    #得到當前分鐘
    def Get_Now_Min(self):
        return time.strftime("%M")

    #得到當前秒數
    def Get_Now_Sec(self):
        return time.strftime("%S")
# ----------------------------------------------------------------------------------------------
    # 獲取Reduce_Day天前的日期
    def Get_Time_difference_Day_Reduce(self,Reduce_Day):
        today = datetime.datetime.now()
        Difference_Hour = datetime.timedelta(days=Reduce_Day)
        Time_difference = today + Difference_Hour
        return Time_difference


    # 獲取Reduce_Hour小時前的日期
    def Get_Time_difference_Hour_Reduce(self,Reduce_Hour):
        Now_Hour = datetime.datetime.now()
        Difference_Hour = datetime.timedelta(hours=Reduce_Hour)
        Time_difference = Now_Hour - Difference_Hour
        return Time_difference


    # 獲取Reduce_Second秒前的日期
    def Get_Time_difference_Seconds_Reduce(self,Reduce_Second):
        sec = datetime.datetime.now()
        difference_day = datetime.timedelta(seconds=Reduce_Second)
        Time_difference = sec - difference_day
        return Time_difference


    # 獲取Add_day天後的日期
    def Get_Time_difference_Day_Add(self,Add_Day):
        today = datetime.datetime.now()
        Difference_Hour = datetime.timedelta(days=Add_Day)
        Time_difference = today + Difference_Hour
        return Time_difference

    # 獲取Add_hour小時後的日期
    def Get_Time_difference_Hour_Add(self,Add_Hour):
        Now_Hour = datetime.datetime.now()
        Difference_Hour = datetime.timedelta(hours=Add_Hour)
        Time_difference = Now_Hour + Difference_Hour
        return Time_difference

    # 獲取Add_Second秒後的日期
    def Get_Time_difference_Seconds_Add(self,Add_Second):
        sec = datetime.datetime.now()
        difference_day = datetime.timedelta(seconds=Add_Second)
        Time_difference = sec + difference_day
        return Time_difference

# ----------------------------------------------------------------------------------------------
    def Sleep(self,Sleep_Time):
        time.sleep(Sleep_Time)
# ----------------------------------------------------------------------------------------------
    def System_Run_Time(self):
        return time.perf_counter()

    def Thread_Run_Time(self):
        return time.process_time()
# ----------------------------------------------------------------------------------------------
    def Delay_Do(self,Time,Function):
        Go = threading.Timer(Time,Function)
        Go.start()
# ----------------------------------------------------------------------------------------------
    '''
    BlockingScheduler: 調用start函數後會阻塞當前線程。當調度器是你應用中唯一要運行的東西時（如上例）使用。
    BackgroundScheduler: 調用start後主線程不會阻塞。當你不運行任何其他框架時使用，並希望調度器在你應用的後台執行。
    '''
    def Loop_Work_Seconds(self,Seconds,Event,Mode='interval'):
        self.scheduler.add_job(Event,Mode,seconds=Seconds)
        self.scheduler.start()

    def Loop_Work_Minute(self,Minute,Event,Mode='interval'):
        self.scheduler.add_job(Event,Mode,minute=Minute)
        self.scheduler.start()

    def Loop_Work_Hour(self,Hour,Event,Mode='interval'):
        self.scheduler.add_job(Event,Mode,hour=Hour)
        self.scheduler.start()
# ----------------------------------------------------------------------------------------------
    def Job_Fuction(self):
        print(datetime.datetime.now())

    def Do_Time_Job(self,Job_Fuction,*args):
        month = '1-12'
        day_of_week = '0-6'
        day = '1-31'
        hour = '0-23'
        minute = 30
        if(len(args)>=1):
            month=args[0]
            if (len(args) >= 2):
                day_of_week=args[1]
                if (len(args) >= 3):
                    day=args[2]
                    if (len(args) >= 4):
                        hour=args[3]
                        if (len(args) >= 5):
                            minute = args[4]
        sched = BackgroundScheduler()
        print(datetime.datetime.now())
        print('Doing Job',Job_Fuction)
        sched.add_job(Job_Fuction, 'cron', month=month,day_of_week=day_of_week, day=day, hour=hour,minute=minute)
        sched.start()






