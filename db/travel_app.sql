DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS countries;



CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    date INT,
    duration INT,
    review TEXT
);