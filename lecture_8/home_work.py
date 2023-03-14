#Q1
import time

time_clear_form = time.ctime(saved_time)

#Q2
import time

time_struct = time.strptime(time_human_readable, "%a %b %d %H:%M:%S %Y")

unix_time = float(time.mktime(time_struct))
#Q3
def strings_from_list():
    yield "This will be the first of many."
    yield "Now we get to the second phase of the things."
    yield "We are at middle point already."
    yield "I don't have that much more to say, sorry."
    yield "This will be the last entry, I hope this was enough for you."
    while True:
        yield None
#Q4
def powers_of_number(base=0):
    p = 0
    while True:
        yield (base ** 0, (base + p) ** 1, (base + p) ** 2, (base + p) ** 3)
        p += 1

#Q5
def next_fibonacci():
    previous = 0
    current = 1
    while True:
        yield previous
        current_value = current
        current = previous + current
        previous = current_value
        
        
#Q1
def next_fibonacci(start=0):
    previous = 0
    current = 1
    if start > 0:
        while previous < start:
            current_value = current
            current = previous + current
            previous = current_value
    yield previous
    while True:
        current_value = current
        current = previous + current
        previous = current_value
        yield previous

#Q2
def numbers_names_cities(names, salary, city, num_times):
    index = 0
    breaker = 1
    while True:
        yield names[index % len(names)]
        if breaker == num_times:
            break
        else:
            breaker += 1
        yield salary[index % len(salary)]
        if breaker == num_times:
            break
        else:
            breaker += 1
        yield city[index % len(city)]
        if breaker == num_times:
            break
        else:
            breaker += 1
        index += 1
    
#Q3
def abc_numbers():
    num = 0
    while True:
        yield "a"
        yield "b"
        yield "c"
        yield num
        if num == 0:
            num = 1
        else:
            num = num * 2

#Q4
def chars_in_line(filename):
    with open(filename) as file:
        for line in file:
            chars = len(line)
            yield chars

#Q5
def text_crawler(filename, string_arg):
    with open(filename) as file:
        for line in file:
            if string_arg in line:
                yield line
            else:
                yield None
        