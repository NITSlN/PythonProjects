import time

def countdown():
    t = int(input('Enter the time : '))
    while t>0:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("\r",timer, end="" )
        time.sleep(1)
        t-=1

    print('\nWoah! times up')


countdown()
