import subprocess

print("Starting Calendly ETL pipeline...")

steps = [
    "src/fetch_calendly_events.py",
    "src/transform_calendly_events.py",
    "src/pyspark_transform_calendly_events.py"
]

for step in steps:
    print(f"\nRunning {step}...")

    result = subprocess.run(["python", step])

    if result.returncode != 0:
        print(f"Pipeline failed at {step}")
        exit(1)

print("\nCalendly ETL pipeline completed successfully.")