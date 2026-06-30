import pandas as pd

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

df = df.drop_duplicates()

df["portfolio_date"] = pd.to_datetime(df["portfolio_date"])

object_columns = df.select_dtypes(include="object").columns
df[object_columns] = df[object_columns].apply(lambda col: col.str.strip())

df.to_csv(
    "data/processed/09_portfolio_holdings_cleaned.csv",
    index=False
)

print("09_portfolio_holdings cleaned successfully.")