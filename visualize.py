import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")
corr = data.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Weather Data Correlation Heatmap")
plt.show()
