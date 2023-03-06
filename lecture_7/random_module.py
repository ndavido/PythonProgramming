#! /usr/bin/python3
import random

a = random.random()
print(a)

b = random.randint(-3,3)
print(b)

c = random.uniform(-3,0)
print(c)

# random with list comprehension

d = [random.random() for _ in range(10)]
print(d)