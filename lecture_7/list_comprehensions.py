#! /usr/bin/python3

# new_list = [expression for number in iterable]

new_list = [x for x in range(10)]
print(new_list)

new_list2 = [x**2 for x in range(10)]
print(new_list2)

# new_list = [expression for number in iterable condition]
new_list3 = [x for x in range(100) if x % 3 == 0]
print(new_list3)

# with else
new_list4 = [x if x % 3 == 0 else 'x' for x in range(100)]
print(new_list4)

# if more than 22 and less than 88
new_list5 = [x for x in range(100) if x % 3 == 0 and x > 22 and x < 88]
print(new_list5)

new_list6 = [x for x in range(100) if 22 < x < 88 and x % 3 == 0 ]
print(new_list6)

mod_list1 = [x**3 for x in new_list]
print(mod_list1)

# mod_list2 where we have a list of tuples where tuples have number and **2 of number and **3

mod_list2 = [{x, x**2, x**3} for x in new_list]
print(mod_list2)

list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

flat_list = [x for sublist in [list1,list2,list3] for x in sublist]
print(flat_list)