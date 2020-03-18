import datetime


def now_time():
    now = datetime.datetime.now()
    return f"{now.year}{str(now.month).zfill(2)}{str(now.day).zfill(2)}"
