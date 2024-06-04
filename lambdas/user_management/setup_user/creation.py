import boto3
import re
from datetime import datetime, date, timedelta
from calendar import monthrange
from logging import getLogger, ERROR

logger = getLogger()
logger.setLevel(ERROR)

def dt_frmt_verify(date_str: str, allow_higher_date: bool = False) -> False or datetime:

    logger.info(f"dt_frmt_verify(): date_str = {date_str}, allow_higher_date = {allow_higher_date}")

    dt_frmt = r'[0-9]{2}-[0-9]{2}-[0-9]{4}'
    regex_search = re.findall(dt_frmt, date_str)
    if regex_search == []:
        logger.error('Error occured: datetime not in MM-DD-YYYY format')
        return False

    split_value_keys = ['month', 'day', 'year']
    split_values = {key: int(value) for key, value in zip(split_value_keys, date_str.split('-'))}

    month = split_values['month']
    year = split_values['year']
    day = split_values['day']

    if month > 12: 
        logger.error("Invalid Data: Month does not exist %s" % str(month))
        return False
    if allow_higher_date != True:
        if year > datetime.now().year: 
            logger.error("Invalid Data: Year is greater than current year %s" % str(month))
            return False
    
    first_day = date(year, month, 1)
    last_date_in_month = first_day + timedelta(days = (monthrange(year, month)[1]) - 1)
    last_day = last_date_in_month.day
    if day > last_day: 
        return False
    
    date_value = datetime.strptime(date_str, '%m-%d-%Y')
    if allow_higher_date != True: 
        if date_value < datetime.now():
            return datetime.strptime(date_str, '%m-%d-%Y')
    logger.error('Error: submited date is greater than current date')
    return False

def create_user(username: str, birthdate: str, email: str, password: str): 

    birthdate = dt_frmt_verify(birthdate)
    if type(birthdate) != datetime: 
        return
    
    

    return