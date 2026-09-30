import os
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine
import wbgapi as wb


def run_etl():
    print("1. Fetching Ghana macroeconomic data from the World Bank API (2009–2025)...")

    indicators = {
        "FP.CPI.TOTL.ZG": "inflation_rate",
        "NY.GDP.MKTP.KD.ZG": "gdp_growth",
        "PA.NUS.FCRF": "usd_ghs_rate",
        "SL.UEM.TOTL.ZS": "unemployment_rate",
    }

    indicator_list = list(indicators.keys())

    # Fetch Ghana data for 2009 through 2025.
    df = wb.data.DataFrame(
        indicator_list,
        economy="GHA",
        time=range(2009, 2026),
    )

    # Transpose and clean index/columns.
    df = df.T
    df.index = df.index.str.replace("YR", "").astype(int)
    df.index.name = "year"
    df = df.rename(columns=indicators)

    # Ensure chronological order before calculating percentage change.
    df = df.sort_index(ascending=True)

    # Calculate year-over-year USD/GHS exchange-rate change.
    df["cedi_depreciation_pct"] = df["usd_ghs_rate"].pct_change() * 100

    # Convert year back to a regular column.
    df = df.reset_index()

    print("2. Connecting to MySQL...")

    db_user = os.getenv("DB_USER", "root")
    db_password = quote_plus(os.getenv("DB_PASSWORD", ""))
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "3306")
    db_name = os.getenv("DB_NAME", "ghana_economy")

    if not db_password:
        raise ValueError(
            "DB_PASSWORD is not set. Create a .env file from .env.example "
            "and provide your local MySQL password."
        )

    connection_url = (
        f"mysql+pymysql://{db_user}:{db_password}"
        f"@{db_host}:{db_port}/{db_name}"
    )

    engine = create_engine(connection_url)

    print("3. Updating records in MySQL...")

    # Rebuild the table with the latest 2009–2025 data.
    df.to_sql(
        "macro_indicators",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print(
        "ETL Complete! 'macro_indicators' was successfully updated "
        "with Ghana macroeconomic data for 2009–2025."
    )


if __name__ == "__main__":
    run_etl()
