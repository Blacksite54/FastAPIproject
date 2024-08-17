INSERT INTO full_names (filename, status)
SELECT filename, status
FROM short_names s
WHERE EXISTS (SELECT 1 FROM full_names f WHERE f.filename = s.filename);