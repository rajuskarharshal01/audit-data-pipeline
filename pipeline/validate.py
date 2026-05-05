import polars as pl


def validate_data(df: pl.DataFrame):
    df = df.clone()

    # Step 1: convert date column FIRST (important)
    df = df.with_columns(
        pl.col("date").str.strptime(pl.Date, strict=False)
    )

    # Step 2: invalid rows (missing or failed date parsing)
    rejected = df.filter(
        (pl.col("amount").is_null()) |
        (pl.col("date").is_null())
    )

    # Step 3: valid rows
    valid_df = df.filter(
        (pl.col("amount").is_not_null()) &
        (pl.col("date").is_not_null())
    )

    return valid_df, rejected