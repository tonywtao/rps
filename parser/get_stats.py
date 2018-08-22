'''
    Jonathan Sawali 

    -   install python3
    -   install pandas (pip3 install pandas)
    -   install numpy (pip3 install numpy)
    
    execute by running this command: python3 get_stats.py sample_log.txt
    
'''


import pandas as pd 
import numpy as np
import sys 
import re
import datetime

t = re.compile(r'(\d{2}:\d{2}:\d{2})')
s = re.compile(r'(\d*\.\d+|\d+)')

def extractTime(str):
    match = t.search(str)
    return match.group(0)

def extractBytes(str):
    match = s.search(str)
    return match.group(0)

def getNum(word):
    return word.split(':')

def main():
    filename = sys.argv[1]

    #load text file
    data = pd.read_csv(filename, header=None)
    data.rename(columns={0:'entry'}, inplace=True)

    data = data[data['entry'].str.contains('not active')==False]

    data = pd.DataFrame(data.entry.str.split('Old').tolist(), columns=['time', 'bytes'])
    
    #apply regex function to get time
    data['time'] = data['time'].apply(extractTime).astype('str')
    
    data['time'] = pd.to_datetime(data['time'], format='%H:%M:%S').dt.time
    data['time'] = data['time'].astype('str')
    

    df_time = pd.DataFrame(data['time'].apply(getNum).tolist(), columns=['h', 'm', 's']).astype('float32')
    
    df_time['h'] = df_time['h']*3600
    df_time['m'] = df_time['m']*60

    df_time['seconds'] = df_time['h'] + df_time['m'] + df_time['s']
    
    
    #calculate time mean   
    time_mean = df_time['seconds'].mean()

    byte_size = pd.DataFrame(data.bytes.str.split('New').tolist(), columns=['old', 'new'])
    byte_size['old'] = byte_size['old'].apply(extractBytes).astype('float32')
    byte_size['new'] = byte_size['new'].apply(extractBytes).astype('float32')
    
    print('Average time: ', str(datetime.timedelta(seconds=int(time_mean))), '\n')

    print('Average speed (old): ', byte_size['old'].mean(), 'MBps') 
    print('Max speed (old): ', byte_size['old'].max(), 'Mbps')
    print('Min speed (old): ', byte_size['old'].min(), 'Mbps\n')

    print('Average speed (new): ', byte_size['new'].mean(), 'MBps') 
    print('Max speed (new): ', byte_size['new'].max(), 'Mbps')
    print('Min speed (new): ', byte_size['new'].min(), 'Mbps\n')

if __name__== "__main__":
    main()
