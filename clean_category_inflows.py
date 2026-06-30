import pandas as pd

df = pd.read_csv("data/raw/05_category_inflows.csv")

df = df.drop_duplicates()

df["month"] = pd.to_datetime(df["month"])

object_columns = df.select_dtypes(include="object").columns
df[object_columns] = df[object_columns].apply(lambda col: col.str.strip())

df.to_csv(
    "data/processed/05_category_inflows_cleaned.csv",
    index=False
)

print("05_category_inflows cleaned successfully.")