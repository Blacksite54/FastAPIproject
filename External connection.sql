INSERT INTO full_names (filename, status)
SELECT s.filename, s.status
FROM short_names s
LEFT JOIN full_names f ON s.filename = f.filename
WHERE f.filename IS NOT NULL;