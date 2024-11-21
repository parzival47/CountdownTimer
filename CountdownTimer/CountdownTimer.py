import time

def countdown(t):
    """
    Countdown Timer
    """
    while t:
        # Divmod takes only two arguments so
        # you'll need to do this for each time
        # Sunit you need to add
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        timer = '{:02d}:{:02d}:{:02d}:{:02d}'.format(days, hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        print(t)
        t -= 1

    print('Time is Over!!')

t = input("Enter the time:  ")

countdown(int(t))