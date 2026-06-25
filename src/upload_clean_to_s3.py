import os
import boto3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

PROJECT_DIR = Path("/Users/prudencedera/Downloads/calendly-pyspark-aws-project")
LOCAL_FILE = PROJECT_DIR / "data" / "clean_calendly_events.csv"

S3_BUCKET = os.getenv("S3_BUCKET", "prudence-pyspark-project")
S3_KEY = "Calendly/clean/clean_calendly_events.csv"


def upload_file_to_s3():
    if not LOCAL_FILE.exists():
        raise FileNotFoundError(f"Clean file not found: {LOCAL_FILE}")

    s3 = boto3.client("s3")

    s3.upload_file(
        Filename=str(LOCAL_FILE),
        Bucket=S3_BUCKET,
        Key=S3_KEY,
    )

    print(f"Uploaded {LOCAL_FILE} to s3://{S3_BUCKET}/{S3_KEY}")


if __name__ == "__main__":
    upload_file_to_s3()
