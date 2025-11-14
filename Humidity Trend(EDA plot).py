import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Humidity'], marker='o', color='blue')
plt.title("Humidity Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.show()
