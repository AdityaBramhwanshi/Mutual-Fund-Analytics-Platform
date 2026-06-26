import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI Codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing Codes
missing_codes = fund_codes - nav_codes

print("=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

print(f"Total Fund Master Codes : {len(fund_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")
print(f"Missing Codes           : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\nAll AMFI Codes are present in NAV History.")
else:
    print("\nMissing AMFI Codes:")
    print(sorted(missing_codes))