-- CREATE TABLE IF NOT EXISTS romance_movies (
-- movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
-- title TEXT NOT NULL,
-- release_year INTEGER,
-- director TEXT,
-- lead_actors TEXT,
-- duration_minutes INTEGER,
-- rating REAL,
-- review TEXT,
-- genre TEXT DEFAULT 'Romance',
-- UNIQUE(title, release_year) -- prevents duplicates
-- );


-- INSERT INTO romance_movies 
-- (title, release_year, director, lead_actors, duration_minutes, rating, review, genre)
-- VALUES 
-- ('La La Land', 2016, 'Damien', 'Ryan Gosling, Emma Stone', 128, 8.0, 'A modern musical about love and ambition.', 'Romantic Musical');

-- INSERT INTO romance_movies 
-- (title, release_year, director, lead_actors, duration_minutes, rating, review, genre)
-- VALUES
-- ('Little Women', 2019, 'Greta Gerwig', 'Saoirse Ronan, Emma Watson, Florence Pugh, Timothée Chalamet', 135, 7.8, 'A timeless adaptation exploring love, family, and independence.', 'Romantic Drama');

-- INSERT INTO romance_movies 
-- (title, release_year, director, lead_actors, duration_minutes, rating, review, genre)
-- VALUES
-- ('Five Feet Apart', 2019, 'Justin Baldoni', 'Haley Lu Richardson, Cole Sprouse', 116, 7.1, 'A heartfelt story of young love challenged by illness and distance.', 'Romantic Drama');

-- INSERT INTO romance_movies 
-- (title, release_year, director, lead_actors, duration_minutes, rating, review, genre)
-- VALUES
-- ('How to Lose a Guy in 10 Days', 2003, 'Donald Petrie', 'Kate Hudson, Matthew McConaughey', 116, 6.4, 'A witty romantic comedy about love, deception, and unexpected connection.', 'Romantic Comedy');




-- ******* QUERIES ******
SELECT * FROM romance_movies;

