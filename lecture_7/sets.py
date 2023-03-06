#! /usr/bin/python3

first_set = {1,2,3,4}
print(first_set)
print(type(first_set))

# second_set = set(1,2,3,4)
# TypeError: set expected at most 1 argument, got 4

second_set = set([1,2,3,4])
# maybe even better:
second_set = set((1,2,3,4))

third_set = set((1,1,1,1))
print(third_set)

print(len(third_set))
print(len(first_set))

a_list = [1,2,3,4,4,4,4,4]
print(a_list)

set_from_a_list = set(a_list)
print(set_from_a_list)
back_to_list = list(set_from_a_list)
print(back_to_list)

