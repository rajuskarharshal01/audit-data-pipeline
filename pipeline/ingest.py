import pandas as pd
from utils.config import settings

def load_data_in_chunks(chunk_size=10000):
    try:
        return pd.read_csv(settings.input_file, chunksize=chunk_size)
    except Exception as e:
        raise RuntimeError(f"Error Loading data in chunks: {e}")






    