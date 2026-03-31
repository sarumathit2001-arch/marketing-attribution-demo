# Marketing Attribution Demo

## 📊 Overview
This project demonstrates a simple marketing attribution pipeline using BigQuery, dbt-style transformations, and a dashboard.

---

## 🏗️ Architecture

Tools used:
- Google BigQuery (data warehouse)
- SQL (transformations)
- Looker Studio (dashboard)
- GitHub (version control)

### Data Flow
Raw Events → Staging → Attribution Models → Dashboard

### Dataset & Tables
- Dataset: `marketing_data`
- Raw Table: `raw_events`
- Models:
  - `stg_events`
  - `mart_first_touch_attribution`
  - `mart_last_touch_attribution`

---

## 🧱 Data Model

### Raw Table: `raw_events`

| Column      | Type      | Description |
|------------|----------|-------------|
| event_id   | STRING   | Unique event identifier |
| user_id    | STRING   | User identifier |
| event_time | TIMESTAMP| Time of event |
| channel    | STRING   | Marketing channel |

---

## 🔄 Transformations

### First Touch Attribution
- First interaction per user
- Uses window function with `ORDER BY event_time ASC`
- Window functions (ROW_NUMBER) were used to identify first and last touch events per user.

### Last Touch Attribution
- Most recent interaction per user
- Uses window function with `ORDER BY event_time DESC`
- Window functions (ROW_NUMBER) were used to identify first and last touch events per user.

---

## ⚙️ Assumptions

- Lookback window: Not applied (full history used)
- Identity resolution: Based on `user_id`
- Tie-breaker: Earliest/latest timestamp
- No duplicate event_ids
- ## ✅ Data Quality Tests

Basic dbt tests such as not_null and uniqueness were defined in schema.yml.

---

## 📡 Streaming Demo

- Simulated event streaming using insert queries
- Demonstrates near real-time updates in dashboard
- Due to BigQuery free tier limitations, streaming API was simulated using delayed inserts. In production, this would be implemented using Pub/Sub or streaming inserts.
- In production, streaming would be implemented using Pub/Sub and BigQuery streaming inserts for low-latency ingestion.
- Expected latency is near real-time (seconds to minutes depending on ingestion method).

### Key Concepts
- Idempotency: event_id ensures uniqueness
- Deduplication: handled via event_id
- Expected latency: few seconds to minutes

---

## 📊 Dashboard

🔗 Dashboard Link:
https://lookerstudio.google.com/reporting/5303f919-e083-4138-8514-88a97031010d/page/J5XtF

### Includes:
- Channel breakdown (bar chart)
- 14-day time series
- Live events table

---

## 🚀 How to Run

1. Create dataset in BigQuery
2. Create `raw_events` table
3. Insert sample data
4. Run SQL transformations
5. Connect Looker Studio to BigQuery
6. Build dashboard

---

## ⚠️ Failure Handling

- Missing data → handled via null checks
- Duplicate events → prevented via event_id
- Late arriving data → supported

---

## 📈 Monitoring

- Query performance in BigQuery
- Dashboard refresh validation
- Row counts consistency

---

## 💰 Cost Notes

- Uses BigQuery free tier / sandbox
- Minimal data → negligible cost

---

## 🎥 Demo

Ready for live demo or screencast (5–8 minutes)

Demo Link - https://www.loom.com/share/0f47c3c6bc82480190c050134932e66e

---

## 📝 Worklog

See `worklog.md` for daily progress tracking

---

## 🚀 Future Improvements

- Implement incremental dbt models
- Add identity resolution across devices
- Use Pub/Sub for real-time streaming
