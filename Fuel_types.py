import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset 
data = pd.read_csv("cardata.csv")

# Count the occurrences of each fue; type
fuel_counts = data["Fuel_Type"].value_counts()

#ploting the data
plt.figure(figsize=(10,6))
fuel_counts.plot(kind="bar", color=["blue","green", "red"])
plt.xlabel("FUEL TYPE")
plt.ylabel("NUMBER OF CARS")
plt.title("DISTRIBUTUION OF DIFFERENT FUEL TYPES")
plt.show()