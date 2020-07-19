import datetime

def get_formatted_time():
    return datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def get_time_object(formatted_time):
    return datetime.datetime.strptime(formatted_time,'%Y-%m-%dT%H:%M:%S')
