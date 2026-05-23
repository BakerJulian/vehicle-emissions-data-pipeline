import pandas as pd
import joblib

MODEL_PATH = "models/co2_emissions_model.pkl"
CLEAN_DATA_PATH = "data/processed/vehicle_emissions_clean.csv"

model = joblib.load(MODEL_PATH)

data = pd.read_csv(CLEAN_DATA_PATH)

example = data.drop("CO2_Emissions", axis=1).head(1)

prediction = model.predict(example)

print("Example input:")
print(example)

print(f"\nPredicted CO2 Emissions: {prediction[0]:.2f}")