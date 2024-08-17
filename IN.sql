INSERT INTO full_names (filename, status)
SELECT filename, status
FROM short_names
WHERE filename IN (SELECT filename FROM full_names);