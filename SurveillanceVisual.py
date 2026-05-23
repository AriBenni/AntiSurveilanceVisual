import math
import random

## Change your list of locations here!

location = ["Tustin", "Irvine", "Anaheim", "Costa Mesa", "Los Angeles", "Merced", "UC Irvine", "Santa Cruz", "Santa Ana", "Orange", "Fullerton", "Westminster", "Norwalk", "Downey", "Inglewood","North Tustin","East Los Angeles","Compton","Carson","Long Beach"]

## Don't touch anything under this unless you know what you're doing
## -----------------------------------------------------------------------------------

status = ["entered", "exited"]
prev = -1
hour = 0
minute = 0
iter = 0

def timet(hour,minute,iter):
    if iter == 0:
        iter =+1
        if hour <= 20:
            hour += random.randint(1,3)
        elif hour >= 21:
            hour = random.randint(0, 4)

        if minute <= 45:
            minute += random.randint(1,14)
        elif minute >= 46:
            minute = random.randint(0, 23)
    elif iter != 0:
        iter = 0
        if minute < 45:
            minute += random.randint(3,14)
        elif minute >= 46:
            if hour == 23: # rollover
                hour = 0
            else: hour += 1
            minute = random.randint(0,6)

    return (hour,minute)

name = input("Please enter the name/identifier of the 'target': ")
repeats = int(input("Please enter the number of iterations: "))

for i in range(repeats):
    locnum = random.randint(0, len(location)-1)
    hour, minute = timet(hour, minute,1)

    if prev == locnum: # Prevents location repeat
        if locnum >= (len(location)/2):
            locnum = locnum - random.randint(1, int(len(location)/2))
        else:
            locnum = locnum + random.randint(1, int(len(location)/2))
    stat = 0

    print("[",f"{hour:02d}",":",f"{minute:02d}","]",end=" ",sep='')
    print(name,"has", status[stat], location[locnum],end=" ")
    stat = 1

    hour, minute = timet(hour,minute,0)
    print("[",f"{hour:02d}",":",f"{minute:02d}","]",end=" ",sep='')
    print(name,"has", status[stat], location[locnum],end=" ")
    prev = locnum

