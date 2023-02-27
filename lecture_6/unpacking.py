#! /usr/bin/python3

tuple_of_values = (1,2,3,4,5)

one, two , three, four, five = tuple_of_values

print(one)
print(two)
print(three)
print(four)
print(five)

# one, two, three, four = tuple_of_values
# ValueError: too many values to unpack (expected 4)
 
one, two, three, *rest = tuple_of_values

print(one)
print(two)
print(three)
print(rest)
print(type(rest))

# * in function definition

def show_cities(*args):
    print(f'what is the type of this *args thing: {type(args)}')
    for city in args:
        print(city)
    
show_cities("rome")
print("------------")
show_cities("rome", "paris")
print("------------")



def show_cities(*args):
    print(f'what is the type of this *args thing: {type(args)}')
    print(*args)
    
show_cities("rome")
print("------------")
show_cities("rome", "paris")
print("------------")

# def show_cities(args):
#     print(f'what is the type of this *args thing: {type(args)}')
#     for city in args:
#         print(city)
    
# show_cities("rome")
# print("------------")
# show_cities("rome", "paris")
# print("------------")

def show_cities_2(first_city, *args):
    print(f'what is the type of this *args thing: {type(args)}')
    print(f"the first city is : {first_city}")
    for city in args:
        print(city)

show_cities_2("rome")
print("------------")
show_cities_2("rome", "paris")
print("------------")
show_cities_2("rome", "paris", "pori")
print("------------")

######

dict1 = {1:"v1",2:"v2",3:"v3"}
dict2 = {4:"v4",5:"v5",6:"v6"}

# dict3 = dict1 + dict2
# TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

dict3 = {**dict1,**dict2}
print(dict3)

dict4 = dict1
print(dict1 is dict4)

dict5 = {**dict1}

print(dict1 is dict5)
print(dict1 == dict5)

def average_house_value(**kwargs):
    print(f'the type of **kwargs is: {type(kwargs)}')
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

average_house_value(pori = 100_000,
                    turku = 200_000,
                    helsinki = 400_000)

def example(first, *args, second="second", **kwargs):
    print(f'what is the type of this **args thing: {type(args)}')
    print(f'the type of **kwargs is: {type(kwargs)}')
    print(f"the first is : {first}")
    for value in args:
        print(value)
    print(f"the second is : {second}")
    for key, value in kwargs.items():
        print(f"key: {key}, value: {value}")

print("-----------")
example("at least we need this")
print("-----------")
example("at least we need this", "this is new one")

example("at least we need this", 
        "this is new one",
        second = "new second",
        val1 = 1,
        val2 = 2,
        val3 = 3)
