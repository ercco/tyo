import datetime

def get_formatted_time(datetime_object):
    return datetime_object.strftime('%Y-%m-%dT%H:%M:%S')

def get_time_object(formatted_time):
    return datetime.datetime.strptime(formatted_time,'%Y-%m-%dT%H:%M:%S')

def write_to_file(datetime_object,event_type):
    formatted_time = get_formatted_time(datetime_object)
    with open(formatted_time[0:7]+'.txt','a') as f:
        if event_type == 'start':
            f.write('A\t'+formatted_time+'\n')
        elif event_type == 'stop':
            f.write('O\t'+formatted_time+'\n')

def start():
    start_time = datetime.datetime.now()
    write_to_file(start_time,'start')

def stop():
    stop_time = datetime.datetime.now()
    write_to_file(stop_time,'stop')
