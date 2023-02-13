#! /usr/bin/python3

def useless_function(value1=2, value2=1):
    answer = value1 - value2*value2
    return answer

print("this is from file function_no_name_is.py")
print(useless_function(4,5))
print(useless_function())
print("this is from file function_no_name_is.py")
print(__name__)