# this will find out if all Tech Acad branches are open at the current time

# import modules
import pytz as tz
import datetime as dt
from datetime import *

# store the TA branches in a certain timezone

time_now = dt.datetime.now().time().strftime('%H:%M')

# local time NY
tech_new_york = tz.timezone('America/New_York')
time_ny = dt.datetime.now(tz=tech_new_york).time()
# local time Portland
tech_acad_portland = tz.timezone('US/Pacific')
time_portland = dt.datetime.now(tz=tech_acad_portland).time()
# local time london
tech_acad_london = tz.timezone('Europe/London')
time_london = dt.datetime.now(tz=tech_acad_london).time()

# open/close hours
time_open = dt.time(9)
time_close = dt.time(19)

def branches_open():
    print('Local time where Justin is: ', time_now)
    if time_ny > time_open and time_ny < time_close:
        print('NY branch is open for business!')
    else:
        print('New York is closed right now, sorry!')
    if time_portland > time_open and time_portland < time_close:
        print('Portland branch is open for business!')
    else:
        print('Portland branch is close right now')
    if time_london > time_open and time_london < time_close:
        print('London Branch is open for business')
    else:
        print('London Branch is closed right now, sorry!')
    



if __name__=='__main__':
    branches_open()








