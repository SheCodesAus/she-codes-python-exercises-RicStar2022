#Excerise 1 -- correct

# moths_in_house = False
# mitch_is_home = True

# #if moths_in_house:
#     print("Get the moths!")
# else: 
#     print("No threats detected")

#Excerise 2 -- Correct
# if mitch_is_home and moths_in_house:
#     print("Hooman! Help me get the moths!")
# elif moths_in_house:
#     print("Meooooooowwwww! Hisssssss!")
# elif mitch_is_home:
#     print("Climb on Mitch")
# else:
#     print("No threats detected.")

#Exercise 3 -- not sure how to do this one.

# light_colour = input()
# car_detected = False

# if light_colour == "red":
# print(f"Do nothing.")

#Exercise 4 -- Correct
# user_height= input(f" Enter your height, please")
# req_height = 120

# if int(user_height) >= int(req_height):
#     print(f"hop on!")
# else:
#     print(f" Sorry, not today, :(")

#Exercise 5

username = input("Please enter your username")
password = input("Please enter your password")


login = username and password

if login is True:
    print("Correct!")
else:
    print("Incorrect!")