from pipeline.ingest import load_data_in_chunks
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.audit_rules import apply_audit_rules
from pipeline.output import save_chunk
from utils.logger import setup_logger
import pandas as pd


def run_pipeline():
    logger = setup_logger()
    logger.info("Starting audit data pipeline (chunked mode)")

    first_chunk = True

    for i, chunk in enumerate(load_data_in_chunks()):
        logger.info(f"Processing chunk {i+1}")

        chunk = validate_data(chunk)
        chunk = transform_data(chunk)
        chunk = apply_audit_rules(chunk)

        save_chunk(
            chunk,
            mode="w" if first_chunk else "a",
            header=first_chunk
        )

        first_chunk = False 
    logger.info("Pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()

