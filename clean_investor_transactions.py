import pandas as pd

# -------------------------------
# Load Dataset
# -------------------------------
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 70)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 70)

# -------------------------------
# Convert Transaction Date
# -------------------------------
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# -------------------------------
# Standardize Transaction Type
# -------------------------------
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
    .str.title()
)

valid_transaction_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_transactions = transactions[
    ~transactions["transaction_type"].isin(valid_transaction_types)
]

print(f"\nInvalid Transaction Types : {len(invalid_transactions)}")

# Convert Sip back to SIP as required
transactions["transaction_type"] = transactions["transaction_type"].replace({
    "Sip": "SIP"
})

# -------------------------------
# Validate Amount
# -------------------------------
transactions = transactions[
    transactions["amount_inr"] > 0
]

# -------------------------------
# Validate KYC Status
# -------------------------------
transactions["kyc_status"] = (
    transactions["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

invalid_kyc = transactions[
    ~transactions["kyc_status"].isin(valid_kyc)
]

print(f"Invalid KYC Status Values : {len(invalid_kyc)}")

# -------------------------------
# Remove Duplicate Rows
# -------------------------------
transactions = transactions.drop_duplicates()

# -------------------------------
# Save Clean Dataset
# -------------------------------
transactions.to_csv(
    "data/processed/08_investor_transactions_cleaned.csv",
    index=False
)

print("\nCleaning Completed Successfully.")

print(f"Rows : {len(transactions)}")
print(f"Columns : {len(transactions.columns)}")

print("\nSaved File :")
print("data/processed/08_investor_transactions_cleaned.csv")