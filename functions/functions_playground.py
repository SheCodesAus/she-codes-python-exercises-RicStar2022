
# #Definition 
# def hello():
#     print("hello world")
#     return "don't get it"


# # #Calling the function
# result = hello()
# print(result)

# #Demonstrate a function
# def create_greeting(name):
#     greeting = f"Hello, {name}!"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Ivy"))
# print(create_greeting("Remus"))

# def sum(number1, number2):
#     result = number1 * number2
#     return result

# print(sum(5, 5))

#Createanotherfunctionthattakesanintegerasaparameterandreturnsthatintegermultiplied by 3.1


# def triple(number):
#     return 3 * number

# print(triple(10))

def convert_cm_to_inch(length_cm):
    length_in_inches = length_cm / 2.54
    return length_in_inches

print(convert_cm_to_inch(20))