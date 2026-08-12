cat > README.md <<'EOF'
# Calendly PySpark AWS ETL Pipeline

## Project Overview

This project is an end-to-end ETL pipeline that extracts Calendly event data, transforms it with Python/PySpark, validates the cleaned output, uploads the clean CSV file to Amazon S3, and makes the data queryable with Amazon Athena.

The project currently runs locally on my MacBook using Apache Airflow. The final clean dataset is stored in AWS S3 and queried using Athena.

## Architecture

Calendly API
→ Python extraction script
→ PySpark transformation
→ Clean CSV validation
→ Amazon S3
→ Athena external table
→ SQL analytics queries

## Tech Stack

- Python
- PySpark
- Apache Airflow
- AWS S3
- Amazon Athena
- AWS Glue Data Catalog
- boto3
- AWS CLI
- Git and GitHub

## Airflow Workflow

The Airflow DAG is located in:

dags/calendly_etl_dag.py

The DAG runs four tasks:

1. fetch_calendly_events
2. transform_with_pyspark
3. validate_clean_file
4. upload_clean_to_s3

## What Each Task Does

- fetch_calendly_events: Extracts event data from the Calendly API.
- transform_with_pyspark: Cleans and transforms the data using PySpark.
- validate_clean_file: Confirms the clean CSV exists and is not empty.
- upload_clean_to_s3: Uploads the clean CSV to Amazon S3.

## AWS S3 Integration

The clean CSV is uploaded to:

s3://prudence-pyspark-project/Calendly/clean/clean_calendly_events.csv

## Athena Integration

Amazon Athena is used to query the clean CSV stored in S3.

Database:

calendly_etl_db

Main table:

clean_calendly_events_fixed

A schema mismatch issue was fixed by recreating the Athena external table with the correct CSV column order.

Correct column order:

name,
start_time,
end_time,
status,
location_type,
location_value,
invitees_active,
invitees_total,
created_at,
updated_at,
uri

## Example Athena Queries

Preview cleaned data:

SELECT *
FROM calendly_etl_db.clean_calendly_events_fixed
LIMIT 10;

Count events by status:

SELECT
    status,
    COUNT(*) AS total_events
FROM calendly_etl_db.clean_calendly_events_fixed
GROUP BY status;

Total invitees:

SELECT
    SUM(CAST(invitees_active AS INTEGER)) AS total_active_invitees,
    SUM(CAST(invitees_total AS INTEGER)) AS total_invitees
FROM calendly_etl_db.clean_calendly_events_fixed;

## Current Status

Completed:

- GitHub repository setup
- Python 3.11 virtual environment
- Calendly API extraction
- PySpark transformation
- Local Airflow DAG orchestration
- Successful Airflow DAG run
- S3 upload integration
- Athena external table creation
- Athena schema mismatch fix
- SQL analytics queries saved

## Local vs Cloud

This project currently runs locally on my MacBook using Apache Airflow.

The pipeline connects to AWS by uploading cleaned data to Amazon S3 and querying that data through Amazon Athena.

Current setup:

Local Airflow orchestration + AWS cloud storage/query layer

## Next Improvements

- Add stronger error handling and logging.
- Add screenshots of Airflow and Athena results.
- Improve schema management.
- Add more sample data.
- Explore cloud scheduling options such as Amazon MWAA, EC2, Lambda/EventBridge, or ECS/Fargate.

## How to Run Locally

Activate the environment:

cd /Users/prudencedera/Downloads/calendly-pyspark-aws-project
source venv311/bin/activate

Set Airflow home:

export AIRFLOW_HOME=/Users/prudencedera/Downloads/calendly-pyspark-aws-project

Start Airflow:

airflow standalone

Open Airflow UI:

http://localhost:8080

Trigger the DAG:

calendly_pyspark_aws_etl

## Notes

Sensitive files such as AWS credentials, Airflow database files, logs, virtual environments, and local configuration files should not be committed to GitHub.
EOF
# Calendly PySpark AWS ETL Pipeline

## Project Overview

This project is an end-to-end ETL pipeline that extracts Calendly event data, transforms it with Python/PySpark, validates the cleaned output, uploads the clean CSV file to Amazon S3, and makes the data queryable with Amazon Athena.

The project currently runs locally on my MacBook using Apache Airflow, while the final cleaned data is stored and queried in AWS.

## Architecture

```text
Calendly API
    ↓
Python extraction script
    ↓
PySpark transformation
    ↓
Clean CSV validation
    ↓
Amazon S3
    ↓
AWS Glue / Athena external table
    ↓
Athena SQL analytics queries
