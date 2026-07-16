import pandas as pd

performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")

fund_master = pd.read_csv("data/processed/01_fund_master_cleaned.csv")

df = performance.merge(
    fund_master[
        [
            "amfi_code",
            "risk_category"
        ]
    ],
    on="amfi_code"
)

def recommend_funds(risk):

    result = (

        df[
            df["risk_category"]
        .str.lower()
        ==
        risk.lower()
        ]

        .sort_values(
            "sharpe_ratio",
            ascending=False
        )

        .head(3)

    )

    return result[
        [
            "scheme_name",
            "sharpe_ratio",
            "return_3yr_pct",
            "expense_ratio_pct"
        ]
    ]

if __name__ == "__main__":

    risk = input("Enter Risk (Low/Moderate/Very High): ")

    print(recommend_funds(risk))