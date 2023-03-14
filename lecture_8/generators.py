#! /usr/bin/python3

def numbers_for_ever():
    next_number = 0
    while True:
        yield next_number
        next_number += 1
        
print(numbers_for_ever())

generator_numbers_for_ever = numbers_for_ever()
print("--------------")
print(next(generator_numbers_for_ever))
print(next(generator_numbers_for_ever))
print(next(generator_numbers_for_ever))


# How to over heat your pc .exe
# for i in generator_numbers_for_ever:
#     print(i, end =" ")

generator_numbers_for_ever.close()

generator_numbers_for_ever = numbers_for_ever()
print("--------------")
print(next(generator_numbers_for_ever))
print(generator_numbers_for_ever)

def yield_something_for_limited_times():
    yield "first_string"
    yield "second_string"
    yield "third_string"
    yield "fourth_string"
    
string_gen = yield_something_for_limited_times()
print("--------------")
print(next(string_gen))
print(next(string_gen))
print(next(string_gen))
print(next(string_gen))
# print(next(string_gen))
print("--------------")
print(next(yield_something_for_limited_times()))
print(next(yield_something_for_limited_times()))
print(next(yield_something_for_limited_times()))
print(next(yield_something_for_limited_times()))
print(next(yield_something_for_limited_times()))
print(next(yield_something_for_limited_times()))

print("--------------")

def repeating_sequence():
    while True:
        yield "first thing"
        yield "second thing"
        

repeating_generator = repeating_sequence()

print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))
print(next(repeating_generator))

print("--------------")

def numbers_for_ever_with_arg(num):
    next_number = 0
    while True:
        yield next_number + num
        next_number += 1
        
generator_for_ever_with_arg = numbers_for_ever_with_arg(0)
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
generator_for_ever_with_arg = numbers_for_ever_with_arg(100)
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
print(next(generator_for_ever_with_arg))
