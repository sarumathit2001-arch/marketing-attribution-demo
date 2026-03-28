# Streaming Simulation

## Approach
Since BigQuery streaming requires billing, we simulate streaming using a Python script that sends events one by one with delay.

## How it works
- Events are generated in a loop
- Each event is inserted (or simulated) every 2 seconds
- Mimics real-time ingestion

## Dedupe
- event_id is used as unique identifier
- Prevents duplicate event ingestion

## Idempotency
- If same event is processed again, logic ensures duplicates are ignored
- Can be handled using MERGE in production

## Expected Latency
- 1–5 seconds per event (simulated)
- Depends on ingestion and processing
