## Strings

# # print(type(name))
# # print(type(height))
# # print(type(weight))

# day = "Saturday"
# month = "May"
# print(type(day and month))
# message = f"Today is {day} in {month}!"
# print(message)
# # message2 = "Today is " + day
# # print(message2)

#user input
## Collect user input
##Store and use user input

name = input("What is your name? ")
hobby = input("Do you have a favourite hobby? ")
print(f"This is {name}, likes {hobby}.")
age = input(f"Hi {name}, how old are you? ")
years_until_100 = 100 - int(age)
print(f"Wow, {name}! You'll be 100 in {years_until_100} years!")
