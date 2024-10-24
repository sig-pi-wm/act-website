-- CREATE TABLE IF NOT EXISTS elo (
--     user_id INT,
--     race_id INT,
--     time_stamp TIMESTAMP,
--     elo DECIMAL
-- )

ALTER TABLE users ADD COLUMN elo DECIMAL(10,2) DEFAULT 1000.00;
UPDATE users SET elo = 1000 WHERE elo IS NULL;
