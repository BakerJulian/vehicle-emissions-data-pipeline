import pandas as pd

RAW_DATA_PATH = "data/raw/vehicle_emissions.csv"
CLEAN_DATA_PATH = "data/processed/vehicle_emissions_clean.csv"


def clean_vehicle_data():
    data = pd.read_csv(RAW_DATA_PATH)

    # Clean column names so they are easier to use in Python
    data.columns = data.columns.str.strip().str.replace(" ", "_")

    # Remove duplicated rows
    data = data.drop_duplicates()

    # Remove rows where the target value is missing
    data = data.dropna(subset=["CO2_Emissions"])

    # Save cleaned dataset
    data.to_csv(CLEAN_DATA_PATH, index=False)

    print(f"Cleaned data saved to {CLEAN_DATA_PATH}")
    print(f"Rows: {data.shape[0]}")
    print(f"Columns: {data.shape[1]}")


if __name__ == "__main__":
    clean_vehicle_data()