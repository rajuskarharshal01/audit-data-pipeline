import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")


    df["currency"] = df["currency"].str.upper().str.strip()

    df = df.drop_duplicates(subset=["transaction_id"])
    return df