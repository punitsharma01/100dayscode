import csv
# with open("weather_data.csv", mode="r") as csvfile:
#     data = csvfile.readlines()
#     for item in data:
#         print(item)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])