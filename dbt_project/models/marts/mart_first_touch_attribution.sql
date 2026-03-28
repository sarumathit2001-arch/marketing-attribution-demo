SELECT
  user_id,
  channel AS first_touch_channel,
  event_time
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY event_time ASC) AS rn
  FROM {{ ref('stg_events') }}
)
WHERE rn = 1
