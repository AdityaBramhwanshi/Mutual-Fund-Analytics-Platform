import pandas as pd

# ---------------------------------
# Load Dataset
# ---------------------------------
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 70)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 70)

# ---------------------------------
# Validate Return Columns
# ---------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

for column in return_columns:
    performance[column] = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

# ---------------------------------
# Check for Missing Numeric Values
# ---------------------------------

missing_returns = performance[return_columns].isnull().sum()

print("\nMissing Values in Return Columns:")
print(missing_returns)

# ---------------------------------
# Flag Expense Ratio Anomalies
# ---------------------------------

expense_anomalies = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies Found:", len(expense_anomalies))

if len(expense_anomalies) > 0:
    print(expense_anomalies[
        ["scheme_name", "expense_ratio_pct"]
    ])

# ---------------------------------
# Remove Duplicate Rows
# ---------------------------------

performance = performance.drop_duplicates()

# ---------------------------------
# Save Clean Dataset
# ---------------------------------

performance.to_csv(
    "data/processed/07_scheme_performance_cleaned.csv",
    index=False
)

print("\nCleaning Completed Successfully.")

print(f"Rows : {len(performance)}")
print(f"Columns : {len(performance.columns)}")

print("\nSaved File :")
print("data/processed/07_scheme_performance_cleaned.csv")