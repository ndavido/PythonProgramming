#! /usr/bin/python3

def calculator(operation, num1, num2):
    if operation == "add":
        answer = num1 + num2
    elif operation ==  "multiply":
        answer = num1 * num2
    else:
        answer = ""
    return answer