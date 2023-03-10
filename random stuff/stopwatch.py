from datetime import datetime
import time as t

# Variables
seconds = 0
minutes = 0
hours = 0
day = 0
months = 0
year = 0


while True:

    t.sleep(1)
    seconds += 1
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if seconds == 60:
        minutes += 1
        seconds = 0

    if minutes == 60:
        hours += 1
        minutes = 0
        seconds = 0

    if hours == 24:
        day += 1
        hours = 0
        minutes = 0
        seconds = 0

    if day == 30:
        months += 1
        day = 0
        hours = 0
        minutes = 0
        seconds = 0

    if months == 12:
        year += 1
        months = 0
        day = 0
        hours = 0
        minutes = 0
        seconds = 0

    # printedText = str(hours) + 'h ' + str(minutes) + 'm ' + str(seconds) + 's have passed'
    # printedText =

    print('\r %s years %s months %s days %s hours %s minutes %s seconds have passed      Current Time is %s ' % (year, months, day, hours, minutes, seconds, current_time), end = '')

