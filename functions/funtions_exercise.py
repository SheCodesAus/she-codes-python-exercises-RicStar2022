
# Functions Exercise Q1 -- Write a function that takes a temperature in fahrenheitand returns the temperature in celsius

# def convert_temp_in_f(temp_c):
#     temp_f = (temp_c - 32) * (5/9)
#     return temp_f

# print(convert_temp_in_f(350))

# Functions Exercise Q2 -- Writeafunctionthatacceptsoneparameter(aninteger)andreturnsTruewhenthatparameterisoddandFalse when that parameter is even

# user_input = input("enter a number")

# def is_it_odd(user_input):
#     if int(user_input) %2 != 0:
#         return True
#     else:
#         return False  

# print(is_it_odd(user_input))

# Functions Exercise Q3 -- Write a function that returns the mean of a listof numbers.

def find_average(total_numbers):
    count = len(total_numbers)
    sum_list = sum(total_numbers)
    return sum_list/count

print(find_average([4,3,2,6]))