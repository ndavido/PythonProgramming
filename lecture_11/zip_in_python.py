#! /usr/bin/pyhton3

from itertools import zip_longest


list1 = [1,2,3,4]
list2= ["yksi", "kaksi", "kolme", "nelja"]

for zipped in zip(list1,list2):
    print(zipped)
    print(type(zipped))

combined_list = zip(list1,list2)
print(combined_list)
print(list(combined_list))

combined_list = list(zip(list1,list2))
print(combined_list)

list3 = [5,6,7,9]

list123 = list(zip(list1, list2, list3))
print(list3)

list4 = [1,2]
list5 = [1,2,3]
list45 = list(zip(list4,list5))
print(list45)

list45_long = list(zip_longest(list4,list5))
print(list45_long)

list45_long_fillvalue = list(zip_longest(list4,list5,fillvalue=0))
print(list45_long_fillvalue)

for a,b in zip(list1, list2):
    print(a,b)

for zipped in zip(list1, list2):
    print(*zipped)
    
import sys
print(sys.version_info)
print(type(sys.version_info[1]))
print(type(sys.version_info))
print((sys.version_info.minor))