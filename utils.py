import time

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_of_week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
days_dictionary = {'Mo':0, 'Tu':1, 'We':2, 'Th':3, 'Fr':4, 'Sa':5, 'Su':6}

def hour_to_24(hour, am_pm):
    '''
    (int,str) -> str
    Given hour from am/pm format hour:minute a/p
    returns integer number of hours in 24 hours format'''
    if (am_pm == 'p' and hour < 12) or (am_pm == 'a' and hour == 12):
        hour = hour + 12
    return hour

def time_am_pm (hour, minute):
    '''
    (int, int) -> (string)
    :param hour: hour in 24 hour format
    :param minute: minutes
    :return: string hh:mm am/pm
    '''

    am_pm_hour = str(hour)
    am_pm = 'am'
    if hour > 12:
        hour = hour -12
        am_pm_hour = str(hour)
        am_pm = 'pm'
    if hour == 12:
        am_pm = 'pm'

    formatted_min = str(minute).zfill(2)

    return am_pm_hour+":" + formatted_min +" "+am_pm

def update_clock(window,time_label):
    now = time.strftime("%H:%M:%S")
    time_label.configure(text=now)
    window.after(1000, update_clock(window,time_label))