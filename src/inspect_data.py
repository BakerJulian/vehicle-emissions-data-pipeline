import pandas as pd

RAW_DATA_PATH = "data/raw/vehicle_emissions.csv"

data = pd.read_csv(RAW_DATA_PATH)

print("First 5 rows:")
print(data.head())

print("\nDataset info:")
data.info()

print("\nColumn names:")
print(data.columns)