#https://app.codility.com/demo/results/training9XMW98-4AE/

WITH latest_events AS 
(
SELECT event_type
,value
,time
,LAG(value, 1) OVER (PARTITION BY event_type ORDER BY time, event_type DESC) AS last_event_value
,row_number() over(partition by event_type order by time desc) as row_no
from events
)

SELECT event_type
,value - last_event_value AS value
FROM latest_events
WHERE row_no = 1
AND last_event_value IS NOT NULL