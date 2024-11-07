CREATE TABLE IF NOT EXISTS maps (
    map_id INT AUTO_INCREMENT PRIMARY KEY,
    map_name VARCHAR(255) UNIQUE NOT NULL,
    cup VARCHAR(255) NOT NULL
);

INSERT IGNORE INTO maps (map_name, cup)
VALUES
    -- Mushroom Cup
    ('Luigi Circuit', 'Mushroom'),
    ('Moo Moo Meadows', 'Mushroom'),
    ('Mushroom Gorge', 'Mushroom'),
    ('Toad''s Factory', 'Mushroom'),
    
    -- Flower Cup
    ('Mario Circuit', 'Flower'),
    ('Coconut Mall', 'Flower'),
    ('DK Summit', 'Flower'),
    ('Wario''s Gold Mine', 'Flower'),
    
    -- Star Cup
    ('Daisy Circuit', 'Star'),
    ('Koopa Cape', 'Star'),
    ('Maple Treeway', 'Star'),
    ('Grumble Volcano', 'Star'),
    
    -- Special Cup
    ('Dry Dry Ruins', 'Special'),
    ('Moonview Highway', 'Special'),
    ('Bowser''s Castle', 'Special'),
    ('Rainbow Road', 'Special'),
    
    -- Shell Cup
    ('GCN Peach Beach', 'Shell'),
    ('DS Yoshi Falls', 'Shell'),
    ('SNES Ghost Valley 2', 'Shell'),
    ('N64 Mario Raceway', 'Shell'),
    
    -- Banana Cup
    ('N64 Sherbet Land', 'Banana'),
    ('GBA Shy Guy Beach', 'Banana'),
    ('DS Delfino Square', 'Banana'),
    ('GCN Waluigi Stadium', 'Banana'),
    
    -- Leaf Cup
    ('DS Desert Hills', 'Leaf'),
    ('GBA Bowser Castle 3', 'Leaf'),
    ('N64 DK''s Jungle Parkway', 'Leaf'),
    ('GCN Mario Circuit', 'Leaf'),
    
    -- Lightning Cup
    ('SNES Mario Circuit 3', 'Lightning'),
    ('DS Peach Gardens', 'Lightning'),
    ('GCN DK Mountain', 'Lightning'),
    ('N64 Bowser''s Castle', 'Lightning');
