import datetime
from dateutil.relativedelta import *

def check_age(birthday):
    try:
        given_dob = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        raise ValueError ("Exception - incorrect format")
    age = relativedelta(now, given_dob).years

    if age < 16:
        return f"ACCESS DENIED! You are {age}, but need to be 16 to access."
    else:
        return f"ACCESS GRANTED! You are {age}."