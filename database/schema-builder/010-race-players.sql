CREATE TABLE IF NOT EXISTS race_players (
    race_id INT NOT NULL,
    player_id INT NOT NULL,
    points INT NOT NULL,

    FOREIGN KEY (race_id) REFERENCES races(race_id),
    FOREIGN KEY (player_id) REFERENCES users(user_id)
);
