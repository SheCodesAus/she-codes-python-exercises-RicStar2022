#CSV FILES EXCERISE Q1 -- Write a program that reads incolours_20_simple.csvand output the colour data

# This is correct and gives correct output

# import csv

# colour = []

# with open("./csv_files/colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour.append(line)

# for format_column in colour:
#     print (f"{format_column[1]} {format_column[2]} {format_column[4]}")

#CSV FILES EXERCISE Q2 Write a program that reads in colours_20_simple.csv and out puts the colour data in order English,Hex then RGB --- CORRECT

# import csv

# colour = []

# with open("./csv_files/colours_20_simple.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour.append(line)

# for format_column in colour:
#     print (f"{format_column[2]}, Hex:{format_column[1]}, RGB:{format_column[0]}")

# print(colour)

# # CSV FILES EXERCISE Q3 Write a program that reads in colours_20.csv and out puts the colour data in order English,Hex then RGB -- CORRECT

# import csv

# colour = []

# with open("./csv_files/colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colour.append(line)

# for format_column in colour:
#     print (f"{format_column[4]} {format_column[2]} {format_column[2]}")

# print(colour)

# #CSV FILES EXCERISE Q4 -- Using the same colour csv files ,write a program that out puts the number of times each of the following colours appear in the English Name: red, green, blue, yellow

# #is_header = False #global variable


# import csv
# from operator import itemgetter

# list_words = ['red', 'green', 'blue', 'yellow']
# red_total = 0
# green_total = 0
# blue_total  = 0
# yellow_total = 0

# with open("./csv_files/colours_20.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         # for item in line[4]:
#         if list_words[0] in line[4].lower():
#             red_total += 1
#         if list_words[1] in line[4].lower():
#             green_total += 1
#         if list_words[2] in line[4].lower():
#             blue_total += 1
#         if list_words[3] in line[4].lower():
#             yellow_total += 1


# print(f'Red: {red_total}')
# print(f'Green: {green_total}')
# print(f'Blue: {blue_total}')
# print(f'yellow: {yellow_total}')

# #CSV FILES EXCERISE Q5 -- galaxies.py contains data about 82 different galaxies and their velocities(km/sec).Using this data, out put the galaxy with the slowest velocity, and the galaxy with the highest velocity

import csv
import sys  

# galaxy_list = []

with open("./csv_files/galaxies.csv", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        line.sort_values()
        print(line)