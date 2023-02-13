import copy
#pragma region EXCERCISE 1
rental_prices = (31, 24.4, 12, 15, 19, 38)
rental_prices_list = list(rental_prices)

print(rental_prices)
print(rental_prices_list)
#pragma endregion

#pragma region EXCERCISE 2
rental_prices = [31, 24.4, 12, 15, 19, 38]
rental_prices_tuple = tuple(rental_prices)

print(rental_prices)
print(rental_prices_tuple)
#pragma endregion

#pragma region EXCERCISE 3
def divider(number1, number2):
    division = number1 / number2
    floor_division = number1 // number2
    modulo = number1 % number2
    return division, floor_division, modulo

result = divider(5, 2)
print(result)
#pragma endregion

#pragma region EXERCISE 4
next_weeks_lotterys_winning_numbers = [1, 2, 3, 4, 5]

wrong_number_for_next_weeks_lottery = next_weeks_lotterys_winning_numbers.copy()

print(next_weeks_lotterys_winning_numbers)
print(wrong_number_for_next_weeks_lottery)

wrong_number_for_next_weeks_lottery[0] = 3
print(wrong_number_for_next_weeks_lottery)
#pragma endregion

#pragma region EXCERCISE 5
def tuples2d_to_2dlists(tuple_of_tuples):
    return [list(x) for x in tuple_of_tuples]

tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
result = tuples2d_to_2dlists(tuple_of_tuples)
print(result) 
#pragma endregion

#pragma region EXERCISE 6
def realizator(list_of_lists):
    real_lists = []
    for i in range(len(list_of_lists)):
        real_lists.append([x.real for x in list_of_lists[i]])
    return tuple(real_lists)

list_of_lists = [[1+2j, 2+3j, 3+4j, 4+5j, 5+6j], [2+3j, 3+4j, 4+5j, 5+6j, 6+7j]]
result = realizator(list_of_lists)
print(result) 
#pragma endregion

#pragma region EXERCISE 7
def tuplenator (list_):
    return (len(list_), sum(list_), *list_)

my_list = [1, 2, 3, 4, 5]
result = tuplenator(my_list)
print(result)
print(my_list)
#pragma endregion

#pragma region EXERCISE 8
def fibonacci(n):
    fib_series = [0,1]
    for i in range(2,n+1):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series

def list_mutator(arr):
    arr_copy = arr.copy()
    fib_series = fibonacci(len(arr_copy))
    for i in range(len(arr_copy)):
        if i in fib_series:
            arr_copy[i] = 1
    return arr_copy

original_list = [1, 2, 3, 4, 5, 6, 7, 8]
result = list_mutator(original_list)
print(result)
#pragma endregion

#pragma region EXERCISE 9
def complex_to_list(tuple_of_complex):
    result = []
    for c in tuple_of_complex:
        result.append([c.real, c.imag, c])
    return result

tuple_of_complex = (1+2j, 2+3j, 3+4j, 4+5j, 5+6j)
result = complex_to_list(tuple_of_complex)
print(result)
#pragma endregion

#pragma region EXERCISE 10
def coefficients_to_complex(real_tuple, imag_tuple):
    return tuple(real + imag*1j for real,imag in zip(real_tuple,imag_tuple))

real_coefficients = (1, 2, 3)
imag_coefficients = (2, 3, 4)
result = coefficients_to_complex(real_coefficients, imag_coefficients)
print(result)
print(type(result[0]))
#pragma endregion