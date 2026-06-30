import pandas as pd

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("\n" + "=" * 80)
    print(file)
    print("=" * 80)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:", df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())