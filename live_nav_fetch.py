import pandas as pd
import requests

BASE_URL = "https://api.mfapi.in/mf/"

schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, amfi_code in schemes.items():

    url = BASE_URL + str(amfi_code)

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{scheme_name}_live_nav.csv",
            index=False
        )

        print(f"{scheme_name} downloaded successfully.")

    else:

        print(f"Failed to fetch {scheme_name}")