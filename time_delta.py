''' Here I continue to solve the chellenges by HackerRank
TODO "Time Delta"
'''

import sys
# import datetime
from datetime import datetime, timedelta

def month_str_to_number(str):
    if str == 'Jan':
        return 1
    elif str == 'Feb':
        return 2

    elif str == 'Mar':
        return 3

    elif str == 'Apr':
        return 4

    elif str == 'May':
        return 5

    elif str == 'Jun':
        return 6

    elif str == 'Jul':
        return 7

    elif str == 'Aug':
        return 8

    elif str == 'Sep':
        return 9

    elif str == 'Oct':
        return 10

    elif str == 'Nov':
        return 11

    elif str == 'Dec':
        return 12

    else:
        print('Error in month: ', str)
    return 0

def time_zone_to_min(str):
    # print(str)
    time_zone_polus = str[0:1]
    time_zone_h = str[1:3]
    time_zone_min = str[3:]
    time_zone_h = int(time_zone_h)
    time_zone_min = int(time_zone_min)
    if time_zone_polus == '+':
        time_zone_h = 0 - time_zone_h
        time_zone_min = 0 - time_zone_min
    time_zone = time_zone_h*60 + time_zone_min
    # print(time_zone_polus, time_zone_h, ':', time_zone_min)
    # print('time_zone =', time_zone)
    return time_zone

def str_to_datetime(tt):
    _, day1, month1, year1, time1, time_zone1 = tt.split(' ')
    h, min, sec = time1.split(':')
    # print(h, min, sec)
    month1 = month_str_to_number(month1)
    time1 = datetime(int(year1), int(month1), int(day1), int(h), int(min), int(sec))

    return time1

def time_delta(t1, t2):
    time1 = str_to_datetime(t1)
    time2 = str_to_datetime(t2)

    _, _, _, _, _, time_zone1 = t1.split(' ')
    _, _, _, _, _, time_zone2 = t2.split(' ')
    time_zone_min_1 = time_zone_to_min(time_zone1)
    time_zone_min_2 = time_zone_to_min(time_zone2)

    time1 += timedelta(minutes=time_zone_min_1)
    time2 += timedelta(minutes=time_zone_min_2)
    # print(time1)
    # print(time2)

    if time1 > time2:
        delta = time1.timestamp() - time2.timestamp()
        # print(int(delta))
        return int(delta)
    else:
        delta = time2.timestamp() - time1.timestamp()
        # print(int(delta))
        return int(delta)

    # return delta.seconds
    # return delta

if __name__ == "__main__":
    # t = int(input().strip())
    # for a0 in range(t):
        # t1 = input().strip()
        # t2 = input().strip()
    for _ in range(1):
        # t1 = 'Sat 02 May 2015 19:54:36 +0530'
        # t2 = 'Fri 01 May 2015 13:54:36 -0000'

        t1 = 'Sun 10 May 2015 13:54:36 -0700'
        t2 = 'Sun 10 May 2015 13:54:36 -0000'

        delta = time_delta(t1, t2)
        print(delta)