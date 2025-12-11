import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")

fur_color = squirrel_data["Primary Fur Color"]
# print(fur_color[200:205])
red_color = squirrel_data[squirrel_data["Primary Fur Color"] != "Gray"]
colors = ["Gray", "Cinnamon", "Black"]
# print(red_color["Primary Fur Color"][2])
# print(len(red_color["Primary Fur Color"]))
# print(squirrel_data.iloc[2])

count_fur_colors = {}
for color in colors:
    count_fur_colors[color] = len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
print(count_fur_colors)
fur_color_dict = {
    "Fur Color" : list(count_fur_colors.keys()),
    "Count" : list(count_fur_colors.values())
}
print(fur_color_dict)

fur_colors_data = pandas.DataFrame(fur_color_dict)
print(fur_colors_data)
fur_colors_data.to_csv("fur_colors_count.csv")