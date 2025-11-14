import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")
plt.figure(figsize=(7,5))
plt.scatter(data["Humidity"], data["Temperature"])
plt.title("Temperature vs Humidity")
plt.xlabel("Humidity (%)")
plt.ylabel("Temperature (°C)")
plt.show()
