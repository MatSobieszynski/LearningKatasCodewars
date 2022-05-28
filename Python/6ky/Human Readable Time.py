'''Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.'''

from time import time


def make_readable(seconds):
    time=""
    h=seconds//3600
    z=(seconds-h*3600)//60
    secs=seconds-z*60-h*3600
    print(h,z,secs)
    if h<10:
        time=time+"0"+str(h)+":"
    else:
        time=time+str(h)+":"

    if z<10:
        time=time+"0"+str(z)+":"
    else:
        time=time+str(z)+":"

    if secs<10:
        time=time+"0"
        time=time+str(secs)
    else:
        time=time+str(secs)


    return(time)

make_readable(111119)