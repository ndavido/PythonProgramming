#! /usr/bin/python3
'''
while True:
    try:
        answer = input("give a number: ")
        int_answer = int(answer)
        calculation = int_answer*3
        print(calculation)
    except:
        print("you did not give a valid number")
'''   

while True:
    try:
        answer = input("give a number: ")
        int_answer = int(answer)
        calculation = int_answer*3
        print(calculation)
    except ValueError as err:
        print(f'{type(err).__name__} was raised: {err}')
        print("you did not give a valid number")