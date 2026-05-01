from pipeline.ingest import load_data
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.audit_rules import apply_audit_rules
from pipeline.output import save_data
from utils.logger import setup_logger


def run_pipeline():
    logger = setup_logger()

    logger.info("Starting audit data pipeline")

    df = load_data()
    logger.info(f"Loaded data with {len(df)} rows")

    df = validate_data(df)
    logger.info(f"After validation: {len(df)} rows")

    df = transform_data(df)
    logger.info(f"After transformation: {len(df)} rows")

    df = apply_audit_rules(df)
    logger.info("Audit rules applied")

    save_data(df)
    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()