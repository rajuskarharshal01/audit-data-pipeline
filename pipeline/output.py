from utils.config import settings


def save_data(df):
    df.to_csv(settings.output_file, index=False)
    print(f"Saved processed data to {settings.output_file}")