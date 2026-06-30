import pandas as pd

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

df = df.drop_duplicates()

df["date"] = pd.to_datetime(df["date"])

object_columns = df.select_dtypes(include="object").columns
df[object_columns] = df[object_columns].apply(lambda col: col.str.strip())

df.to_csv(
    "data/processed/03_aum_by_fund_house_cleaned.csv",
    index=False
)

print("03_aum_by_fund_house cleaned successfully.")