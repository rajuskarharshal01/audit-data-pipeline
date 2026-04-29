from pydantic import BaseSettings

class Settings(BaseSettings):
    input_file: str = "data/raw/audit_data.csv"
    output_file: str = "data/processed/cleaned_data.csv"
    log_file: str = "pipeline.log"
    high_value_threshold: float = 10000.0

    class config:
        env_file = '.env'


settings = Settings()
