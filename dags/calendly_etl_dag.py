from __future__ import annotations

import datetime
import pendulum

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


PROJECT_DIR = "/Users/prudencedera/Downloads/calendly-pyspark-aws-project"
PYTHON_BIN = f"{PROJECT_DIR}/venv311/bin/python"


default_args = {
    "owner": "prudence",
    "retries": 2,
    "retry_delay": datetime.timedelta(minutes=5),
}


with DAG(
    dag_id="calendly_pyspark_aws_etl",
    description="Scheduled Calendly ETL pipeline using Python, PySpark, AWS S3, and Airflow",
    default_args=default_args,
    start_date=pendulum.datetime(2026, 6, 24, tz="America/Chicago"),
    schedule="@daily",
    catchup=False,
    tags=["calendly", "pyspark", "aws", "s3", "etl"],
) as dag:

    fetch_calendly_events = BashOperator(
        task_id="fetch_calendly_events",
        bash_command=f"cd {PROJECT_DIR} && {PYTHON_BIN} src/fetch_calendly_events.py",
    )

    transform_with_pyspark = BashOperator(
        task_id="transform_with_pyspark",
        bash_command=f"cd {PROJECT_DIR} && {PYTHON_BIN} src/pyspark_transform_calendly_events.py",
    )

    validate_clean_file = BashOperator(
        task_id="validate_clean_file",
        bash_command=f"test -s {PROJECT_DIR}/data/clean_calendly_events.csv",
    )

    upload_clean_to_s3 = BashOperator(
        task_id="upload_clean_to_s3",
        bash_command=f"cd {PROJECT_DIR} && {PYTHON_BIN} src/upload_clean_to_s3.py",
    )

    fetch_calendly_events >> transform_with_pyspark >> validate_clean_file >> upload_clean_to_s3
