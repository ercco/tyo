import datetime
import sys

def get_formatted_time(datetime_object):
    return datetime_object.strftime('%Y-%m-%dT%H:%M:%S')

def get_time_object(formatted_time):
    return datetime.datetime.strptime(formatted_time,'%Y-%m-%dT%H:%M:%S')

def write_to_file(datetime_object,event_type,tag='',additional_info=''):
    formatted_time = get_formatted_time(datetime_object)
    with open(formatted_time[0:7]+'.txt','a') as f:
        if event_type == 'start':
            f.write('\t'.join(filter(None,['A',formatted_time,tag,additional_info]))+'\n')
        elif event_type == 'stop':
            f.write('\t'.join(filter(None,['O',formatted_time,tag,additional_info]))+'\n')

def start(tag='',additional_info=''):
    start_time = datetime.datetime.now()
    write_to_file(start_time,'start',tag,additional_info)

def stop(tag='',additional_info=''):
    stop_time = datetime.datetime.now()
    write_to_file(stop_time,'stop',tag,additional_info)

if __name__ == '__main__':
    data = [sys.argv[1]]
    if len(sys.argv) == 2:
        data.append('')
        data.append('')
    elif len(sys.argv) == 3:
        data.append(sys.argv[2])
        data.append('')
    elif len(sys.argv) == 4:
        data.append(sys.argv[2])
        data.append(sys.argv[3])
    if sys.argv[1] == 'start':
        start(data[1],data[2])
    elif sys.argv[1] == 'stop':
        stop(data[1],data[2])
