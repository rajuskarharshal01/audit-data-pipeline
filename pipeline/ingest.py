import pandas as pd
from utils.config import settings

def load_data():
    try:
        df = pd.read_csv(settings.input_file)
        print(f"Loaded {len(df)} rows")
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")
    