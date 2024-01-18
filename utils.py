import pytz
from datetime import datetime, timedelta

def datetimeAwareEastern(year, month, day, hour=0, minute=0, sec=0):
    us_eastern = pytz.timezone('US/Eastern')
    t = datetime(year, month, day, hour, minute, sec)
    t = us_eastern.localize(t)
    return t

def datetimeAwareUTC(year, month, day, hour=0, minute=0, sec=0):
    utc = pytz.utc
    t = datetime(year, month, day, hour, minute, sec)
    t = utc.localize(t)
    return t

def toEasternAware(dt):
    return dt.astimezone(pytz.timezone('America/New_York'))

def formatHHMM(dt):
    return dt.strftime('%H:%M')

def formatMonthHHMM(dt):
    return dt.strftime('%m-%d %H:%M')
