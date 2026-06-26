import pandas as pd

# Load Fund Master dataset
fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

# Unique Fund Houses
print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

# Unique Categories
print("\nUnique Categories:")
print(fund_master["category"].unique())

# Unique Sub-Categories
print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

# Unique Risk Categories
print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

# Sample AMFI Scheme Codes
print("\nSample AMFI Scheme Codes:")
print(fund_master["amfi_code"].head(10))