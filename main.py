import argparse
import os

from pipeline.ingest import load_data_in_chunks
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.audit_rules import apply_audit_rules
from pipeline.output import save_chunk
from utils.logger import setup_logger
from utils.config import settings


def parse_args():
    parser = argparse.ArgumentParser(description="Audit Data Processing Pipeline")

    parser.add_argument("--input", type=str, help="Input file path")
    parser.add_argument("--output", type=str, help="Output file path")
    parser.add_argument("--chunk-size", type=int, help="Chunk size for processing")
    parser.add_argument("--threshold", type=float, help="High-value transaction threshold")

    return parser.parse_args()


def run_pipeline():
    args = parse_args()
    logger = setup_logger()

    logger.info("Starting audit data pipeline (CLI + streaming mode)")

    # 🔧 Override config from CLI
    if args.input:
        settings.input_file = args.input
        logger.info(f"Input file overridden: {settings.input_file}")

    if args.output:
        settings.output_file = args.output
        logger.info(f"Output file overridden: {settings.output_file}")

    if args.chunk_size:
        settings.chunk_size = args.chunk_size
        logger.info(f"Chunk size set to: {settings.chunk_size}")

    if args.threshold:
        settings.high_value_threshold = args.threshold
        logger.info(f"Threshold set to: {settings.high_value_threshold}")

    # 📁 Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    rejected_file = "data/processed/rejected_data.csv"
    first_chunk = True
    total_rows_processed = 0

    try:
        for i, chunk in enumerate(load_data_in_chunks(settings.chunk_size)):
            logger.info(f"Processing chunk {i + 1} with {len(chunk)} rows")

            # 🔍 Detailed tracking
            logger.info(f"Chunk {i+1}: initial rows = {len(chunk)}")

            before_validation = len(chunk)
            chunk, rejected = validate_data(chunk)
            logger.info(
                f"After validation: {len(chunk)} "
                f"(removed {before_validation - len(chunk)})"
            )

            # 💥 Save rejected rows (audit traceability)
            if not rejected.empty:
                rejected.to_csv(
                    rejected_file,
                    mode="w" if i == 0 else "a",
                    header=(i == 0),
                    index=False
                )
                logger.info(f"Rejected rows saved: {len(rejected)}")

            before_transform = len(chunk)
            chunk = transform_data(chunk)
            logger.info(
                f"After transform: {len(chunk)} "
                f"(removed {before_transform - len(chunk)})"
            )

            chunk = apply_audit_rules(chunk)

            save_chunk(
                chunk,
                mode="w" if first_chunk else "a",
                header=first_chunk
            )

            total_rows_processed += len(chunk)
            first_chunk = False

        logger.info(
            f"Pipeline completed successfully. Total rows processed: {total_rows_processed}"
        )

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()