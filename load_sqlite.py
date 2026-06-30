import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

print("=" * 70)
print("LOADING CLEANED DATASETS INTO SQLITE DATABASE")
print("=" * 70)

datasets = {
    "fund_master": "data/processed/01_fund_master_cleaned.csv",
    "nav_history": "data/processed/02_nav_history_cleaned.csv",
    "aum_by_fund_house": "data/processed/03_aum_by_fund_house_cleaned.csv",
    "monthly_sip_inflows": "data/processed/04_monthly_sip_inflows_cleaned.csv",
    "category_inflows": "data/processed/05_category_inflows_cleaned.csv",
    "industry_folio_count": "data/processed/06_industry_folio_count_cleaned.csv",
    "scheme_performance": "data/processed/07_scheme_performance_cleaned.csv",
    "investor_transactions": "data/processed/08_investor_transactions_cleaned.csv",
    "portfolio_holdings": "data/processed/09_portfolio_holdings_cleaned.csv",
    "benchmark_indices": "data/processed/10_benchmark_indices_cleaned.csv"
}

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name:<30} Loaded | Rows: {len(df)}")

print("\n" + "=" * 70)
print("SQLite Database Created Successfully!")
print("Database Name : bluestock_mf.db")
print("=" * 70)