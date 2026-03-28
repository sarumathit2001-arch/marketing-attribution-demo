# Assumptions

## Lookback Window
We assume all events are within a reasonable timeframe (no strict lookback window applied for simplicity).

## Identity Resolution
We assume user_id uniquely identifies a user across all events.

## Tie-breakers
If multiple events have the same timestamp, ordering is arbitrary based on ROW_NUMBER().

## Data Quality
We assume:
- event_id is unique
- event_time is not null
- channel is valid
