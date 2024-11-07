CREATE TABLE IF NOT EXISTS teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_number INT NOT NULL, -- 1, 2, 3, 4
    act_id INT NOT NULL,
    team_character VARCHAR(50) NOT NULL,
    score INT NOT NULL,

    FOREIGN KEY (act_id) REFERENCES acts(act_id),
    FOREIGN KEY (team_character) REFERENCES characters(character_name)
);

CREATE TABLE IF NOT EXISTS team_players (
    team_id INT NOT NULL,
    player_id INT NOT NULL,

    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (player_id) REFERENCES users(user_id)
);
