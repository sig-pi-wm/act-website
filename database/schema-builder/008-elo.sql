-- CREATE TABLE IF NOT EXISTS elo (
--     user_id INT,
--     race_id INT,
--     time_stamp TIMESTAMP,
--     elo DECIMAL
-- )

-- ALTER TABLE users ADD COLUMN elo FLOAT DEFAULT 1500.0;
-- UPDATE users SET elo = 1500.0 WHERE elo IS NULL;
DROP TABLE IF EXISTS elo;
