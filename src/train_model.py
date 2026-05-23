import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

CLEAN_DATA_PATH = "data/processed/vehicle_emissions_clean.csv"
MODEL_PATH = "models/co2_emissions_model.pkl"
REPORT_PATH = "reports/model_report.txt"

data = pd.read_csv(CLEAN_DATA_PATH)

X = data.drop("CO2_Emissions", axis=1)
y = data["CO2_Emissions"]

numeric_features = X.select_dtypes(include=["int64", "float64"]).columns
categorical_features = X.select_dtypes(include=["object"]).columns

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

joblib.dump(model, MODEL_PATH)

with open(REPORT_PATH, "w") as file:
    file.write("Vehicle Emissions Regression Model Report\n")
    file.write("=" * 45)
    file.write("\n")
    file.write(f"Mean Absolute Error: {mae:.2f}\n")
    file.write(f"Mean Squared Error: {mse:.2f}\n")
    file.write(f"R2 Score: {r2:.4f}\n")

print("Model training complete.")
print(f"Model saved to {MODEL_PATH}")
print(f"Report saved to {REPORT_PATH}")