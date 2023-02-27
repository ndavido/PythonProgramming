#! /usr/bin/pyhton3
filename = "our_first_text_file.txt"

file_handler = open(filename, "w")

file_handler.write("hello world, to file!")
file_handler.close()

print(file_handler.closed)

file_handler = open(filename, "w")

file_handler.write("second time, second line")
print(file_handler.closed)
file_handler.close()

file_handler = open(filename, "a")
file_handler.write("\nsecond time, second line")
file_handler.close()

file_handler = open(filename, 'r')
file_content = file_handler.read()
print(type(file_content))
print(file_content)
file_handler.close()

file_handler = open(filename, 'r')
line_from_file = file_handler.readline()
print(type(line_from_file))
print(line_from_file)
file_handler.close()

with open(filename) as file:
    content_of_the_file = file.read()
    print(content_of_the_file)
    print(file.closed)
print(file.closed)

with open(filename) as filez:
    for line in filez:
        print("for")
        print(line)

import os

if os.path.exists('skynet.txt'):
    os.remove('skynet.txt')
else:
    print('No such file in directory')

