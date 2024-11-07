-- Insert team scores into the team_scores table
INSERT INTO team_scores (act_id, team_number, score)
SELECT act_id, 1, t1_score FROM acts;
INSERT INTO team_scores (act_id, team_number, score)
SELECT act_id, 2, t2_score FROM acts;
INSERT INTO team_scores (act_id, team_number, score)
SELECT act_id, 3, t3_score FROM acts
WHERE t3_score IS NOT NULL;
INSERT INTO team_scores (act_id, team_number, score)
SELECT act_id, 4, t4_score FROM acts
WHERE t4_score IS NOT NULL;

-- Insert players into team_players table for each team number
-- Team 1 players
INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t1_p1_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t1_p1_uid IS NOT NULL AND ts.team_number = 1;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t1_p2_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t1_p2_uid IS NOT NULL AND ts.team_number = 1;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t1_p3_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t1_p3_uid IS NOT NULL AND ts.team_number = 1;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t1_p4_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t1_p4_uid IS NOT NULL AND ts.team_number = 1;

-- Team 2 players
INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t2_p1_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t2_p1_uid IS NOT NULL AND ts.team_number = 2;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t2_p2_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t2_p2_uid IS NOT NULL AND ts.team_number = 2;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t2_p3_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t2_p3_uid IS NOT NULL AND ts.team_number = 2;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t2_p4_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t2_p4_uid IS NOT NULL AND ts.team_number = 2;

-- Team 3 players
INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t3_p1_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t3_p1_uid IS NOT NULL AND ts.team_number = 3;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t3_p2_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t3_p2_uid IS NOT NULL AND ts.team_number = 3;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t3_p3_uid
FROM acts a JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t3_p3_uid IS NOT NULL AND ts.team_number = 3;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t3_p4_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t3_p4_uid IS NOT NULL AND ts.team_number = 3;

-- Team 4 players
INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t4_p1_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t4_p1_uid IS NOT NULL AND ts.team_number = 4;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t4_p2_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t4_p2_uid IS NOT NULL AND ts.team_number = 4;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t4_p3_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t4_p3_uid IS NOT NULL AND ts.team_number = 4;

INSERT INTO team_players (team_id, player_id)
SELECT ts.team_id, a.t4_p4_uid FROM acts a
JOIN team_scores ts ON ts.act_id = a.act_id
WHERE a.t4_p4_uid IS NOT NULL AND ts.team_number = 4;
