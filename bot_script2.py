import time
import pyautogui as pg
def tinsec(hr,mn,s):
    sec=time.time()
    sec+=hr*3600
    sec+=mn*60
    sec+=s
    return sec
def hello(hr,mn,sec):
    dest=tinsec(hr,mn,sec)
    while(dest-time.time()>2):
        print(dest-time.time())
    else:
        dest2=time.time()        
        while(time.time()-dest2<10):
            pg.moveTo(x=622,y=839, duration=1)
            pg.click(interval=0.1)
ask_time=tuple(map(float,input("Enter Time Left:").split(" ")))
hello(ask_time[0],ask_time[1],ask_time[2])
