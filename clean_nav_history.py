import pandas as pd

# Load dataset
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
nav_history["date"] = pd.to_datetime(nav_history["date"])

# Sort data
nav_history = nav_history.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicate rows
nav_history = nav_history.drop_duplicates()

# Forward fill missing NAV values
nav_history["nav"] = (
    nav_history
    .groupby("amfi_code")["nav"]
    .ffill()
)

# Keep only valid NAV values
nav_history = nav_history[
    nav_history["nav"] > 0
]

# Save cleaned dataset
nav_history.to_csv(
    "data/processed/02_nav_history_cleaned.csv",
    index=False
)

print("=" * 60)
print("NAV HISTORY CLEANING COMPLETED")
print("=" * 60)

print(f"Rows: {len(nav_history)}")
print(f"Columns: {len(nav_history.columns)}")
print("\nCleaned file saved to:")
print("data/processed/02_nav_history_cleaned.csv")