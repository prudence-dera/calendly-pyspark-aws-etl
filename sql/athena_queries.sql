-- Athena Queries for Calendly PySpark AWS ETL Project

-- Preview cleaned Calendly data
SELECT *
FROM calendly_etl_db.clean_calendly_events_fixed
LIMIT 10;

-- Count events by status
SELECT
    status,
    COUNT(*) AS total_events
FROM calendly_etl_db.clean_calendly_events_fixed
GROUP BY status;

-- Count events by location type
SELECT
    location_type,
    COUNT(*) AS total_events
FROM calendly_etl_db.clean_calendly_events_fixed
GROUP BY location_type;

-- Total invitees
SELECT
    SUM(CAST(invitees_active AS INTEGER)) AS total_active_invitees,
    SUM(CAST(invitees_total AS INTEGER)) AS total_invitees
FROM calendly_etl_db.clean_calendly_events_fixed;

-- Event schedule view
SELECT
    name,
    status,
    location_type,
    location_value,
    start_time,
    end_time
FROM calendly_etl_db.clean_calendly_events_fixed
ORDER BY start_time;
