import time

def set_timer(a):
    while a:
        mins,secs = divmod(a,60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        a -=1
    print("Time Up!")

a = int(input("Set time : "))
set_timer(a)