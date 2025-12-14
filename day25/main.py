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

series = data["condition"]
# print(series)
average_temperature = round(sum(data["temp"])/len(data["temp"]),2)
print(average_temperature)
# print(data["temp"].mean())

# print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday = data[data["day"] == "Monday"] # this and above lines are same
print(monday)
temp_on_monday = monday.temp[0]
temp_in_f = temp_on_monday * 9/5 + 32
print(f"Temperature on monday: {temp_in_f} Degrees Foreignheight ")

# create dataframe
data_dict = {
    "students" : ["Punit", "Raju", "Rohan"],
    "marks" : [80, 90, 70]
}
data = pandas.DataFrame(data_dict)
print(data)
# data.to_csv("student_data.csv")