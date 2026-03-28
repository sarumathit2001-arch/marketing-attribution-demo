import time
from datetime import datetime
from google.cloud import bigquery

client = bigquery.Client()

table_id = "your_project_id.marketing_data.raw_events"

events = [
    {"event_id": "e7", "user_id": "u4", "channel": "facebook"},
    {"event_id": "e8", "user_id": "u4", "channel": "google"},
    {"event_id": "e9", "user_id": "u5", "channel": "email"},
    {"event_id": "e10", "user_id": "u5", "channel": "direct"},
]

for event in events:
    row = [{
        "event_id": event["event_id"],
        "user_id": event["user_id"],
        "event_time": datetime.utcnow().isoformat(),
        "channel": event["channel"]
    }]

    print(f"Inserting event: {event}")

    # Simulated insert (commented if no billing)
    # errors = client.insert_rows_json(table_id, row)

    # if errors:
    #     print("Error:", errors)
    # else:
    #     print("Inserted successfully")

    time.sleep(2)  # simulate streaming delay
