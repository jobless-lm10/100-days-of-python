# with open("weather-data.csv") as data_file:
#     weather = data_file.readlines()
# print(weather)


# with csv package
# import csv
#
# temperatures = []
# with open("weather-data.csv") as data_file:
#     weather = csv.reader(data_file)
#     for day in weather:
#         if day[1].lower() != "temp":
#             temperatures.append(int(day[1]))
#     print(temperatures)


# with pandas package
import pandas

weather = pandas.read_csv("weather-data.csv")
# print(weather["temp"])
print(weather.temp)

data_dict = weather.to_dict()
print(data_dict)

temp_list = weather.temp.to_list()
print(temp_list)

print(weather[weather.day == "Monday"])

print(weather[weather.temp == weather.temp.max()])
