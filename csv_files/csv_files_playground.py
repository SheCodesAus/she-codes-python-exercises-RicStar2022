# import csv


# # with open("./csv_files/2016_pilbara.csv") as csv_file:
# #     reader  = csv.reader(csv_file)
# #     for line in reader:
# #         print(line)

# population = []

# with open("./csv_files/2016_pilbara.csv", encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         population.append(line)

# print(population)
# print()

# for age_group in population:
#     print (f"{age_group[0]} {age_group[1]}")

# #writing to csv file
# with open("population.csv", mode="w", encoding="utf-8") as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=",")

#     for age_group in population:
#         csv_writer.writerow([age_group[1], age_group[0]])

#Find the minimum value

numbers = [4,7,10,1,2]
min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print(min_value)
