#! /usr/bin/python3
import time

start_time = time.time()
print(start_time)

end_time = time.time()
print(end_time)

time_it_takes = start_time - end_time
print(time_it_takes)

time_now = time.time()
print(time_now)
print(time.ctime(time_now))

for y in range(10):
    print(str(y))
    time.sleep(1)
    
time_human_readable = "Wed Mar 30 09:56:12 2022"
time_struct = time.strptime(time_human_readable,"%a %b %d %H:%M:%S %Y")