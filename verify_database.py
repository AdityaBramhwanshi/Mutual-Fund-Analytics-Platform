import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

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

print("=" * 85)
print("VERIFYING ROW COUNTS")
print("=" * 85)

all_match = True

for table_name, csv_path in datasets.items():

    csv_df = pd.read_csv(csv_path)
    csv_rows = len(csv_df)

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM {table_name}",
        engine
    )["total"][0]

    status = "MATCH" if csv_rows == db_rows else "MISMATCH"

    if status == "MISMATCH":
        all_match = False

    print(f"{table_name:<30} CSV: {csv_rows:<8} DB: {db_rows:<8} {status}")

print("=" * 85)

if all_match:
    print("SUCCESS: All row counts match.")
else:
    print("WARNING: Some row counts do not match.")