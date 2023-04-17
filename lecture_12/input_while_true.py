#! /usr/bin/python3

def ask_number_from_user():
    while True:
        try:
            num = int(input("Give a number as digit, example 3: "))
            return num
        except ValueError as err:
            pass
            