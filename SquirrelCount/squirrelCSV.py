import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {

    "Fur Color": ["Gray","Cinnamon", "Black"],
    "Count": [grey_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_count.csv")

