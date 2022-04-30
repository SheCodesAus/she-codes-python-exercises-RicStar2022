#Data Types - Strings, Integer, Floats, Boolean

#b1 = True
#b2 = False
#print(type(b1))

# knows_password = False
# knows_username = True
# login = knows_password and knows_username
#print(type(login))
#print(login)
# print (not knows_password)
#Boolean Operators - NOT, AND, OR

# recover = knows_password or knows_username


from lib2to3.pgen2.token import EQUAL
from operator import is_
from tempfile import tempdir


is_raining = False
is_cold = True

# print(type(is_raining))
# print(type(is_cold))
# print(not is_raining)
# print(is_raining and is_cold)
# print (is_raining and not is_cold)

# print(is_raining) #False
# print(not is_raining or is_cold) #True
# print(is_raining or is_cold) #True
# print(is_raining and not is_cold) #False
# print(is_raining or not is_cold) #Fasle
# print(not is_raining and not is_cold)#False
# print(not(is_raining and is_cold))#True

# Comparison Operates
## == Equal
# != Not EQUAL
# > Greater than
# < Less than
# >= Greater than or equal
# <= Less than or equal

temperature = 32
# print(temperature < 18)
wind_chill = 10
# # print(wind_chill > 4)
# # print(temperature - wind_chill < 16)

# name = "Hayley"
# print(name == "Hayley")
# #print(name != "Hayley")

## If Statements
is_raining = True

# IF
#if is_raining:
    #print("Take an umbrella")

# if and else
if is_raining:
    print("Take an umbrella")
else:
    print("Do not take an umbrella")

#if, elif, else

if temperature - wind_chill <16 :
    print("Take a jumper.")
elif temperature - wind_chill > 30:
    print("Euck, it's hot today, stay home.")
else:
    print("Wow! What a lovely day!")

# Nested if statements
if temperature - wind_chill < 16 and is_raining:
    print("Just stay home.")
else:
    if is_raining:
        print("You'll need an umbrella today.")
    if temperature - wind_chill < 16:
        print("You'll need a jumper today.")