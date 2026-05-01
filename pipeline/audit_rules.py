from utils.config import settings

def apply_audit_rules(df):
    df = df.copy()

    df["high_value_flag"] = df["amount"] > settings.high_value_threshold

    return df