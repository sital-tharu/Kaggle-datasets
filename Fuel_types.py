import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset 
data = pd.read_csv("cardata.csv")

# Count the occurrences of each fue; type
fuel_counts = data["Fuel_Type"].value_counts
print(fuel_counts)