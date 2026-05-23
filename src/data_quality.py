import pandas as pd

CLEAN_DATA_PATH = "data/processed/vehicle_emissions_clean.csv"
REPORT_PATH = "reports/data_quality_report.txt"


def run_quality_checks():
    data = pd.read_csv(CLEAN_DATA_PATH)

    report = []

    report.append("Vehicle Emissions Data Quality Report")
    report.append("=" * 45)
    report.append(f"Rows: {data.shape[0]}")
    report.append(f"Columns: {data.shape[1]}")
    report.append("")

    report.append("Missing values by column:")
    report.append(str(data.isnull().sum()))
    report.append("")

    report.append(f"Duplicate rows: {data.duplicated().sum()}")
    report.append("")

    if "CO2_Emissions" in data.columns:
        report.append("CO2 emissions summary:")
        report.append(str(data["CO2_Emissions"].describe()))

    with open(REPORT_PATH, "w") as file:
        file.write("\n".join(report))

    print(f"Data quality report saved to {REPORT_PATH}")


if __name__ == "__main__":
    run_quality_checks()