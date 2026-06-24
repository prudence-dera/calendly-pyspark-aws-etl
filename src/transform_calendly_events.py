import pandas as pd
import ast

# Read raw Calendly CSV
df = pd.read_csv("data/calendly_events.csv")

# Convert nested text fields back into Python objects
df["location"] = df["location"].apply(ast.literal_eval)
df["invitees_counter"] = df["invitees_counter"].apply(ast.literal_eval)

# Create clean columns
df["location_type"] = df["location"].apply(
    lambda x: x.get("type") if isinstance(x, dict) else None
)

df["location_value"] = df["location"].apply(
    lambda x: x.get("location") if isinstance(x, dict) else None
)

df["invitees_active"] = df["invitees_counter"].apply(
    lambda x: x.get("active") if isinstance(x, dict) else None
)

df["invitees_total"] = df["invitees_counter"].apply(
    lambda x: x.get("total") if isinstance(x, dict) else None
)

# Select useful columns
clean_df = df[
    [
        "name",
        "start_time",
        "end_time",
        "status",
        "location_type",
        "location_value",
        "invitees_active",
        "invitees_total",
        "created_at",
        "updated_at",
        "uri"
    ]
]

# Save cleaned CSV
clean_df.to_csv("data/clean_calendly_events.csv", index=False)

# Display cleaned data
print(clean_df)

print("\nCleaned CSV saved to data/clean_calendly_events.csv")