from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

# Start Spark session
spark = SparkSession.builder \
    .appName("CalendlyETLTransform") \
    .getOrCreate()

# Read cleaned CSV
df = spark.read.csv(
    "data/clean_calendly_events.csv",
    header=True,
    inferSchema=True
)

print("Raw Data:")
df.show(truncate=False)

# Transform timestamp columns
transformed_df = df.withColumn(
    "start_time_ts", to_timestamp(col("start_time"))
).withColumn(
    "end_time_ts", to_timestamp(col("end_time"))
).withColumn(
    "created_at_ts", to_timestamp(col("created_at"))
)

# Final cleaned dataframe
final_df = transformed_df.select(
    "name",
    "status",
    "location_type",
    "location_value",
    "invitees_active",
    "invitees_total",
    "start_time_ts",
    "end_time_ts",
    "created_at_ts",
    "uri"
)

print("Transformed Data:")
final_df.show(truncate=False)

# Save output
final_df.coalesce(1).write.mode("overwrite").option("header", True).csv(
    "data/pyspark_output"
)

print("PySpark transformation complete.")

spark.stop()