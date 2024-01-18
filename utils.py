import pytz
from datetime import datetime, timedelta

def toNewYorkTime(dt):
    return dt.astimezone(pytz.timezone('America/New_York'))


def HHMM(dt):
    return dt.strftime('%H:%M')

def dayHHMM(dt):
    return dt.strftime('%m-%d %H:%M')
