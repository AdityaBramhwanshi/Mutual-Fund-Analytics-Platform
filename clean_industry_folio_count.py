import pandas as pd

df = pd.read_csv("data/raw/06_industry_folio_count.csv")

df = df.drop_duplicates()

df["month"] = pd.to_datetime(df["month"])

df.to_csv(
    "data/processed/06_industry_folio_count_cleaned.csv",
    index=False
)

print("06_industry_folio_count cleaned successfully.")