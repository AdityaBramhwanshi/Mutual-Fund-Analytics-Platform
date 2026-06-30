import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

df = df.drop_duplicates()

df["month"] = pd.to_datetime(df["month"])

df.to_csv(
    "data/processed/04_monthly_sip_inflows_cleaned.csv",
    index=False
)

print("04_monthly_sip_inflows cleaned successfully.")