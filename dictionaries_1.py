# Question 1
ford = {
  "model": "taunus",
  "engine": 1.5,
  "weight": 1000,
  "top_speed": 180
}

toyota = {
  "model": "corolla",
  "engine": 1.2,
  "weight": 800,
  "top_speed": 140
}

mazda = {
  "model": "rx3",
  "engine": 1.3,
  "weight": 900,
  "top_speed": 220
}

# Question 2
cars = {
  "ford": ford,
  "toyota": toyota,
  "mazda": mazda
}

# Question 3
# def dictator(list1, list2):
#     result = {}
#     for i in range(min(len(list1), len(list2))):
#         key = list1[i]
#         value = list2[i]
#         result[key] = value
#     return result

# Question 4
# def dictator(list1, list2):
#     result = {}
#     for i in range(len(list1)):
#         if i < len(list2):
#             result[list1[i]] = list2[i]
#         else:
#             result[list1[i]] = None
#     return result

list1 = ['d', 'd', 'g']
list2 = [6, 3]

# print(dictator(list1, list2))

# Question 5
def dictator(list1, list2):
    result = {}
    for i in range(len(list1)):
        if i < len(list2):
            key = list1[i]
            value = list2[i]
        else:
            key = list1[i]
            value = None
        if key in result:
            j = 1
            while f"{key}_{j}" in result:
                j += 1

            key = f"{key}_{j}"
        result[key] = value
    return result

print(dictator(list1, list2))

# Question 6
import numpy as np
np_num = np.array([1,], dtype=np.uint16)

# Question 7
def dictster(list1, list2):
    if len(list1) >= len(list2):
        keys = list1
        values = list2
    else:
        keys = list2
        values = list1
    result = {}
    for i in range(len(keys)):
        if i < len(values):
            result[keys[i]] = values[i]
        else:
            result[keys[i]] = 0
    return result

list1 = ['d', 'e', 'f']
list2 = [7,8]
print(dictster(list1, list2))

list1 = ['d']
list2 = [7,8, 9]
print(dictster(list1, list2))

# Question 8
def dict_nester(dict_list):
    result = {}
    for i in range(len(dict_list)):
        result[i] = dict_list[i]
    return result

# Question 9
2^(16-1) - 1 | -(2^(16-1))
print(2^(16-1) - 1)