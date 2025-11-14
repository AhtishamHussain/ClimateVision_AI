import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



data = pd.read_csv("C:\\Users\\shami\\OneDrive\\Desktop\\weather_data.csv")

X = data[["Humidity", "Pressure", "WindSpeed", "Rainfall"]]
y = data["Temperature"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

plt.figure(figsize=(8,5))
plt.plot(predictions, label="Predicted", marker='o')
plt.plot(y_test.values, label="Actual", marker='o')
plt.title("Actual vs Predicted Temperature")
plt.xlabel("Data Points")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.grid(True)
plt.show()
