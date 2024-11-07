INSERT INTO race_players (race_id, player_id, points)
SELECT race_id, t1_player_uid, t1_points FROM races
WHERE t1_player_uid IS NOT NULL AND t1_points IS NOT NULL;

INSERT INTO race_players (race_id, player_id, points)
SELECT race_id, t2_player_uid, t2_points FROM races
WHERE t2_player_uid IS NOT NULL AND t2_points IS NOT NULL;

INSERT INTO race_players (race_id, player_id, points)
SELECT race_id, t3_player_uid, t3_points FROM races
WHERE t3_player_uid IS NOT NULL AND t3_points IS NOT NULL;

INSERT INTO race_players (race_id, player_id, points)
SELECT race_id, t4_player_uid, t4_points FROM races
WHERE t4_player_uid IS NOT NULL AND t4_points IS NOT NULL;
