#FOR LOOPS Excerise Q1 -- CORRECT

#Ask the user for a number. Use a for loop to print the times tables for that number.

# your_number = int(input("Enter the number you wish to multiply: "))

# for i in range(1, your_number+1):
#     print(f"{your_number} * {i} = {your_number * i} ")

# while (your_number < 10):
#     your_number *= 1
#     print(your_number)
   
#FOR LOOPS EXCERISE Q3--) Given a list, use a for loop to sum all the numbers in the list. -- CORRECT
# total = 0
# #random_number = [3, 5, 9, 1]
# #random_number = [-3, -5, 9, 1]
# random_number = []

# for num in random_number:
#     total += num

# print(total)


#Excerise 4

# mailing_list = [
# ["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"],
# ]

# for items in mailing_list:
#     print(mailing_list range(0,1) + ": " + mailing_list[0][1])

#WHILE LOOPS EXERCISE Q1 -- Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.

# input_number = input("Enter a number: ")
# completed_list = []
# # print(input_number)
# # print(completed_list)

# while input_number != "":
#     completed_list.append(int(input_number))
#     input_number = input("Enter a number: ")

# print(completed_list)
# print(sum(completed_list))

#WHILE LOOPS EXCERISE Q2 -- Ask the user to enter a number. Print all the odd numbers between 0 and that number (inclusive).

user_num = int(input("Enter a number: "))


# input_answer = int(len(input_number))

while user_num <= 20:
    if user_num %2 != 0 :
        print(user_num)
    user_num = user_num+1


#WHILE LOOPS EXERCISE Q3 -- Select a number. Ask the user to enter a number, output whether their number is less than or greater than the selected number. Repeat this process until the user guesses the correct number.

# correct_num = 25
# user_guess = int(input("Enter a number: "))

# while user_guess != correct_num:
#     if user_guess < correct_num:
#         print("Too low!")
#         user_guess=int(input("Enter another number: "))
#     elif user_guess > correct_num:
#         print("Too high!")
#     user_guess=int(input("Enter another number: "))
#     # elif user_guess == correct_num:
# print("Your are correct! Great work!!")


