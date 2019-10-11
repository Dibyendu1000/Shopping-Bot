import time
import pyautogui as pg
def tinsec(hr,mn):
    sec=time.time()
    #sec+=hr*3600
    sec+=mn*60
    return sec
def hello(hr,mn):
    dest=tinsec(hr,mn)
    while(dest-time.time()>2):
        print(dest-time.time())
    else:
        dest2=time.time()        
        while(time.time()-dest2<4):
            pg.moveTo(x=622,y=839, duration=1)
            pg.click(interval=0.1)
        
hello(0,0.10)
