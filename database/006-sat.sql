CREATE TABLE IF NOT EXISTS sats (
    sat_id INT AUTO_INCREMENT PRIMARY KEY,
    sat_start_date DATE NOT NULL,
    sat_final_date DATE NOT NULL,
    final_act_id INT,

    FOREIGN KEY (final_act_id) REFERENCES acts(act_id)
);

CREATE TABLE IF NOT EXISTS sat_round1_acts (
    sat_id INT,
    act_id INT,
    
    FOREIGN KEY (sat_id) REFERENCES sats(sat_id),
    FOREIGN KEY (act_id) REFERENCES acts(act_id)
);

CREATE TABLE IF NOT EXISTS sat_round2_acts (
    sat_id INT,
    act_id INT,
    
    FOREIGN KEY (sat_id) REFERENCES sats(sat_id),
    FOREIGN KEY (act_id) REFERENCES acts(act_id)
);

CREATE TABLE IF NOT EXISTS sat_round3_acts (
    sat_id INT,
    act_id INT,
    
    FOREIGN KEY (sat_id) REFERENCES sats(sat_id),
    FOREIGN KEY (act_id) REFERENCES acts(act_id)
);
