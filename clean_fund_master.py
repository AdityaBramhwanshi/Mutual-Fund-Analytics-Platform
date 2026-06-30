import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

# Remove duplicates
df = df.drop_duplicates()

# Remove extra spaces from text columns
object_columns = df.select_dtypes(include="object").columns
df[object_columns] = df[object_columns].apply(lambda col: col.str.strip())

# Convert launch date
df["launch_date"] = pd.to_datetime(df["launch_date"])

# Save
df.to_csv(
    "data/processed/01_fund_master_cleaned.csv",
    index=False
)

print("01_fund_master cleaned successfully.")