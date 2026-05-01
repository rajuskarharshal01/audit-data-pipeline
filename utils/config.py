from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    input_file: str = "C:\\Users\\DELL\\audit-data-pipeline\\data\\raw\\audit_data.csv"
    output_file: str = "C:\\Users\\DELL\\audit-data-pipeline\\data\\processed\\cleaned_data.csv"
    log_file: str = "C:\\Users\\DELL\\audit-data-pipeline\\pipeline.log"
    high_value_threshold: float = 10000.0

    class config:
        env_file = ".env"


settings = Settings()
