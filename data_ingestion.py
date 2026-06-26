import pandas as pd

DATA_PATH = "data/raw/"

datasets = {
    "Fund Master": "01_fund_master.csv",
    "NAV History": "02_nav_history.csv",
    "AUM by Fund House": "03_aum_by_fund_house.csv",
    "Monthly SIP Inflows": "04_monthly_sip_inflows.csv",
    "Category Inflows": "05_category_inflows.csv",
    "Industry Folio Count": "06_industry_folio_count.csv",
    "Scheme Performance": "07_scheme_performance.csv",
    "Investor Transactions": "08_investor_transactions.csv",
    "Portfolio Holdings": "09_portfolio_holdings.csv",
    "Benchmark Indices": "10_benchmark_indices.csv"
}

for name, file in datasets.items():

    print("=" * 70)
    print(f"Dataset: {name}")
    print("=" * 70)

    df = pd.read_csv(DATA_PATH + file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\n")

    