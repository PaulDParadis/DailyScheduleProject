# A prototype for an electronic scheduler
li_ne = "DAILY SCHEDULE"
cent_line = li_ne.center(30)
print(cent_line)
def time_and_date():
    day = input("Day: ")
    date = input(str("Date: "))
    time = input(str("Time: "))
    
time_and_date()

print("Add an activity. When finished, type 'next' and press enter.")

def new_act():
    new_act = input("Add activity: ")
    activity_time = input("Duration: ")
    
new_act()
while True:
    act_new = input("Add another activity? 'y' to add, 'next' to start: ")
    if act_new == 'y':
        new_act()
    elif act_new == 'next':
        print("First activity start: ")
        break
