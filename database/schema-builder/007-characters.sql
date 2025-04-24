CREATE TABLE IF NOT EXISTS characters (
        character_id INT AUTO_INCREMENT PRIMARY KEY,
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

