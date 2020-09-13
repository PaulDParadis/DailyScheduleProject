## Daily Schedule Project
#
#A timer program to track daily tasks.
#
#A work in progress.
#
### Goals
#
#- Set tasks that you will work on.
#- Start the timer for the tasks.
#- Take notes on what you have done at the end of the timer.
#
### License
#
#This project is licensed under the GPL-2.0-or-later license.

from datetime import timedelta
from time import sleep

def convertseconds(time_in_seconds):
    """Convert seconds to H:M:S"""
    return str(timedelta(seconds=time_in_seconds))

def timer_input():
    HOURS = int(input('Hours: '))
    MINUTES = int(input('Minutes: '))
    SECONDS = int(input('Seconds: '))

TIMER = * 60 * 60 + MINUTES * 60 + SECONDS
print(convertseconds(TIMER))

def count_down():
    while TIMER > 0:
        TIMER = TIMER - 1
        sleep(1)
        print(convertseconds(TIMER), end = "\r"
    if TIMER == 0:
        print('Out of time!')

def get_act():
    act_new = input("Activity name: "0
    time_input()

get_act()

def more_act():
    get_new = input("Type 'a' to add new activity or 'n' to start list: ")    
    if get_new == 'a':
        get_act()
        more_act()
                                                        1,6           Top

