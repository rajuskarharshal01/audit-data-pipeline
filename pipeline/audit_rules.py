from utils.config import settings


def apply_audit_rules(df):
    df = df.copy()

    # High value transactions
    df["high_value_flag"] = df["amount"] > settings.high_value_threshold

    # Duplicate vendor transactions (example risk pattern)
    df["duplicate_vendor_flag"] = df.duplicated(subset=["vendor"], keep=False)

    # Suspicious transactions (combined rule)
    df["suspicious_flag"] = (
        df["high_value_flag"] & df["duplicate_vendor_flag"]
    )

    return df