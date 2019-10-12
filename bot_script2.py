import time
import pyautogui as pg

def tinsec(hr,mn,s):
    sec=time.time()
    sec+=hr*3600
    sec+=mn*60
    sec+=s
    return sec

def get_website():
    print("Website List:\n1)Flipkart\n2)Amazon\n3)Terminte")
    ch=int(input("Enter Choice:"))
    if(ch==1):
        ask_website='flipkart.com'
    elif(ch==2):
        pg.alert(text='Service Not Available Yet !', title='Error', button='OK')
        get_website()
    elif(ch==3):
        pass
    else:
        print("Website still not available:")
        get_website()
    return ask_website

def hello():
    pg.alert(text='Time Lef Must be greater than 5s', title='Time Left Warning', button='OK')
    try:
        ask_website=get_website()
    except UnboundLocalError:
        return
    ask_product=input("Enter product (For best results enter exact name):")
    ask_time=tuple(map(float,input("Enter Time Left:").split(" ")))
    dest=tinsec(ask_time[0],ask_time[1],ask_time[2])
    while(dest-time.time()>5):
        print(dest-time.time())
    else:
        pg.moveTo(x=276, y=1073, duration=0.5)
        pg.doubleClick()
        pg.typewrite('google chrome')
        pg.moveTo(x=259,y=381,duration=0.5)
        pg.click()
        pg.moveTo(x=1640,y=152,duration=0.5)
        pg.doubleClick()
        #pg.press('Enter')
        pg.moveTo(x=379, y=62, duration=0.5)
        pg.click()
        pg.typewrite(ask_website)
        pg.press('enter')
        pg.moveTo(x=631, y=126,duration=1.5)
        pg.click()
        pg.typewrite(ask_product)
        pg.press('enter')
        if(ask_website=='flipkart.com'):
            pg.moveTo(x=546, y=529, duration=0.5)
            pg.click()
            pg.moveTo(x=710, y=741, duration=0.5)
            pg.doubleClick()
            dest2=time.time()        
            while(time.time()-dest2<5):
                pg.moveTo(x=622,y=839, duration=1)
                pg.click(interval=0.1)
        elif(ask_website=='amazon.in'):
            pg.moveTo(x=546, y=529,duration=0.5)
            pg.click()
        #pg.moveTo(x=710, y=741, duration=0.5)
        #pg.doubleClick()
        #dest2=time.time()        
        #while(time.time()-dest2<5):
            #pg.moveTo(x=622,y=839, duration=1)
            #pg.click(interval=0.1)


hello()
