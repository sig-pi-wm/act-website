CREATE TABLE IF NOT EXISTS acts (
    act_id INT AUTO_INCREMENT PRIMARY KEY,
    act_date DATE NOT NULL,

    -- Scores
    t1_score INT NOT NULL,
    t2_score INT NOT NULL,
    t3_score INT,
    t4_score INT,

    -- Team 1 players
    t1_p1_uid INT NOT NULL,
    t1_p2_uid INT,
    t1_p3_uid INT,
    t1_p4_uid INT,
    
    -- Team 2 players
    t2_p1_uid INT NOT NULL,
    t2_p2_uid INT,
    t2_p3_uid INT,
    t2_p4_uid INT,
    
    -- Team 3 players
    t3_p1_uid INT,
    t3_p2_uid INT,
    t3_p3_uid INT,
    t3_p4_uid INT,
    
    -- Team 4 players
    t4_p1_uid INT,
    t4_p2_uid INT,
    t4_p3_uid INT,
    t4_p4_uid INT,

    -- Foreign key constraints
    FOREIGN KEY (t1_p1_uid) REFERENCES users(user_id),
    FOREIGN KEY (t1_p2_uid) REFERENCES users(user_id),
    FOREIGN KEY (t1_p3_uid) REFERENCES users(user_id),
    FOREIGN KEY (t1_p4_uid) REFERENCES users(user_id),
    
    FOREIGN KEY (t2_p1_uid) REFERENCES users(user_id),
    FOREIGN KEY (t2_p2_uid) REFERENCES users(user_id),
    FOREIGN KEY (t2_p3_uid) REFERENCES users(user_id),
    FOREIGN KEY (t2_p4_uid) REFERENCES users(user_id),
    
    FOREIGN KEY (t3_p1_uid) REFERENCES users(user_id),
    FOREIGN KEY (t3_p2_uid) REFERENCES users(user_id),
    FOREIGN KEY (t3_p3_uid) REFERENCES users(user_id),
    FOREIGN KEY (t3_p4_uid) REFERENCES users(user_id),
    
    FOREIGN KEY (t4_p1_uid) REFERENCES users(user_id),
    FOREIGN KEY (t4_p2_uid) REFERENCES users(user_id),
    FOREIGN KEY (t4_p3_uid) REFERENCES users(user_id),
    FOREIGN KEY (t4_p4_uid) REFERENCES users(user_id)
);
