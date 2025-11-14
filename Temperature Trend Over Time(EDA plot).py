import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")
data['Date'] = pd.to_datetime(data['Date'])

plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Temperature'], marker='o')
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
