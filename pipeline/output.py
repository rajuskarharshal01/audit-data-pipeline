from utils.config import settings


def save_chunk(df, mode="a", header=False):
    df.to_csv(
        settings.output_file,
        mode=mode,
        header=header,
        index=False
    )