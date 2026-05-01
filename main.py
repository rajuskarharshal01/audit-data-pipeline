from pipeline.ingest import load_data
from pipeline.validate import validate_data
from pipeline.transform import transform_data
from pipeline.audit_rules import apply_audit_rules
from pipeline.output import save_data


def run_pipeline():
    df = load_data()
    df = validate_data(df)
    df = transform_data(df)
    df = apply_audit_rules(df)

    print(df.head())  # debug visibility

    save_data(df)


if __name__ == "__main__":
    run_pipeline()