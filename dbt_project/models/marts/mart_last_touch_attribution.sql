SELECT
  user_id,
  channel AS last_touch_channel,
  event_time
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_time DESC) AS rn
  FROM {{ ref('stg_events') }}
)
WHERE rn = 1
