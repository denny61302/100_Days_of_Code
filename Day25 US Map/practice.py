# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
#
# print(temperatures)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

len_gray = len(data[data["Primary Fur Color"] == "Gray"])
len_black = len(data[data["Primary Fur Color"] == "Black"])
len_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [len_gray, len_black, len_cinnamon]
}

df = pandas.DataFrame(data_dict)
df.to_csv("output.csv")

