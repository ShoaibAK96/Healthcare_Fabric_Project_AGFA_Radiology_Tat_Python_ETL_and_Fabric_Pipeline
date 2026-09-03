-- Replace schema and table names through an approved deployment process.
SELECT business_date, COUNT(*) AS row_count
FROM analytics.fact_radiology_tat
GROUP BY business_date
ORDER BY business_date;

SELECT source_file, file_hash_sha256, status, COUNT(*) AS occurrences
FROM analytics.fact_radiology_tat_file_log
WHERE status = 'SUCCESS'
GROUP BY source_file, file_hash_sha256, status
HAVING COUNT(*) > 1;
