import pandas as pd


data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")

print(data.isnull().sum())

#in this data no one column have null value.....
