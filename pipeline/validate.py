import pandas as pd


def validate_data(df: pd.DataFrame):
    df = df.copy()

    # Rows with missing critical fields
    invalid_rows = df[
        df["amount"].isna() |
        df["date"].isna()
    ]

    # Drop missing
    df = df.dropna(subset=["transaction_id", "amount", "date"])

    # Convert date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Rows with invalid dates
    invalid_date_rows = df[df["date"].isna()]

    # Drop invalid dates
    df = df.dropna(subset=["date"])

    # Combine all rejected rows
    rejected = pd.concat([invalid_rows, invalid_date_rows])

    return df, rejected