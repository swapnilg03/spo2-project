import time  
from threading import Timer  
def display(msg):  
    print(msg + ' ' + time.strftime('%H:%M:%S'))
def run_once():  
    display('run_once:')  
    t=Timer(1,display,['Timeout:']) 
    t=Timer() 
    t.start()#Here run is called  
    run_once()  
     ##Runs immediately and once  
    print('Waiting.....')
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):
            self.function(*self.args,**self.kwargs)  
            print(' ')
timer = RepeatTimer(1,display,['Repeating'])  
timer.start() #recalling run  
print('Threading started')  
time.sleep(50)#It gets suspended for the given number of seconds  
print('Threading finishing')  
timer.cancel()

