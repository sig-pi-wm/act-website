CREATE TABLE IF NOT EXISTS characters (
        character_name VARCHAR(50) UNIQUE NOT NULL
);

INSERT IGNORE INTO characters (character_name)
VALUES
    ('Baby Mario'),
    ('Baby Luigi'),
    ('Baby Peach'),
    ('Baby Daisy'),

    ('Toad'),
    ('Toadette'),
    ('Koopa Troopa'),
    ('Dry Bones'),

    ('Mario'),
    ('Luigi'),
    ('Peach'),
    ('Daisy'),

    ('Yoshi'),
    ('Birdo'),
    ('Diddy Kong'),
    ('Bowser Jr.'),

    ('Wario'),
    ('Waluigi'),
    ('Donkey Kong'),
    ('Bowser'),

    ('King Boo'),
    ('Rosalina'),
    ('Funky Kong'),
    ('Dry Bowser'),

    ('Small Mii'),
    ('Medium Mii'),
    ('Large Mii');

ALTER TABLE acts ADD COLUMN t1_character VARCHAR(50) NOT NULL;
ALTER TABLE acts ADD COLUMN t2_character VARCHAR(50) NOT NULL;
ALTER TABLE acts ADD COLUMN t3_character VARCHAR(50);
ALTER TABLE acts ADD COLUMN t4_character VARCHAR(50);
ALTER TABLE acts ADD CONSTRAINT fk_t1_c FOREIGN KEY (t1_character) REFERENCES characters(character_name);
ALTER TABLE acts ADD CONSTRAINT fk_t2_c FOREIGN KEY (t2_character) REFERENCES characters(character_name);
ALTER TABLE acts ADD CONSTRAINT fk_t3_c FOREIGN KEY (t3_character) REFERENCES characters(character_name);
ALTER TABLE acts ADD CONSTRAINT fk_t4_c FOREIGN KEY (t4_character) REFERENCES characters(character_name);
