CREATE TABLE IF NOT EXISTS races (
    race_id INT AUTO_INCREMENT PRIMARY KEY,
    act_id INT,
    map_id INT,
    race_number INT NOT NULL, -- 1-16, generally

    t1_player_uid INT NOT NULL,
    t2_player_uid INT NOT NULL,
    t3_player_uid INT,
    t4_player_uid INT,

    t1_points INT NOT NULL,
    t2_points INT NOT NULL,
    t3_points INT,
    t4_points INT,

    FOREIGN KEY (act_id) REFERENCES acts(act_id),
    FOREIGN KEY (map_id) REFERENCES maps(map_id)
);
