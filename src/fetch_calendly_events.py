import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get Calendly token from .env
CALENDLY_TOKEN = os.getenv("CALENDLY_TOKEN")

# Validate token exists
if not CALENDLY_TOKEN:
    raise ValueError("Calendly token not found in .env file")

# API headers
headers = {
    "Authorization": f"Bearer {CALENDLY_TOKEN}",
    "Content-Type": "application/json"
}

# ---------------------------------------------------
# STEP 1: Get current user information
# ---------------------------------------------------

me_response = requests.get(
    "https://api.calendly.com/users/me",
    headers=headers
)

print("User Status Code:", me_response.status_code)

# Convert response to JSON
me_data = me_response.json()

# Print user info
print(me_data)

# Extract user URI
user_uri = me_data["resource"]["uri"]

print("\nUser URI:", user_uri)

# ---------------------------------------------------
# STEP 2: Get scheduled events
# ---------------------------------------------------

events_response = requests.get(
    "https://api.calendly.com/scheduled_events",
    headers=headers,
    params={
        "user": user_uri
    }
)

print("\nEvents Status Code:", events_response.status_code)

# Convert events response to JSON
events_data = events_response.json()

# Print scheduled events
print(events_data)


# Extract collection of events
events = events_data["collection"]

# Convert to DataFrame
df = pd.DataFrame(events)

# Display first rows
print(df.head())

# Save to CSV
df.to_csv("data/calendly_events.csv", index=False)
print("Number of events found:", len(events))
print("\nCSV file saved successfully to data/calendly_events.csv")