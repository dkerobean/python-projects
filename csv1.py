# with open('weather_data1.csv') as file:
#     content = file.readlines()
#     print(content)


# import csv
# temperatures = []
#
# with open('weather_data1.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "Temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv('weather_data1.csv')
# temperatures = data['Temp']
# # temp_list = temperatures.tolist()
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(temperatures.max())
# highest_temp = max(data.Temp)
# print(data[data.Temp == highest_temp])
#
# Monday = (data[data.Temp == "Monday"])

#create dataframe

