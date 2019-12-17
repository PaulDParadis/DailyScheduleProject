from datetime import datetime
title = 'daily schedule'
fat_title = title.center(40).upper()
print(fat_title)

'''set date of schedule'''
def set_date():
    day = input("Day: ")
    date = str.format(input("Date: "))
    time = str.format(input("Time: "))
    DayDatTim = (day +" /"+ date +" /"+ time)
    ChronList = DayDatTim.center(45)
    print(ChronList)
set_date()

'''function for obtaining scheduling input'''
def time_input():
    HOURS = int(input('Hours: '))
    MINUTES = int(input('Minutes: '))
    SECONDS = int(input('Seconds: '))
def get_act():
    act_new = input("Activity name: ")
    time_input()
get_act()

def more_act():
    get_new = input("Type 'a' to add new activity or 'n' to start list: ")
    if get_new == 'a':
        get_act()
        more_act()
    elif get_new == 'n':
        print("Type 's' to start timer for list: ")


                                                        1,1           Top

