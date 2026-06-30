import pandas as pd

df = pd.read_csv("data/raw/10_benchmark_indices.csv")

df = df.drop_duplicates()

df["date"] = pd.to_datetime(df["date"])

object_columns = df.select_dtypes(include="object").columns
df[object_columns] = df[object_columns].apply(lambda col: col.str.strip())

df.to_csv(
    "data/processed/10_benchmark_indices_cleaned.csv",
    index=False
)

print("10_benchmark_indices cleaned successfully.")