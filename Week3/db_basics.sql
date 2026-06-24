CREATE TABLE users (
id    SERIAL PRIMARY KEY,
name  VARCHAR(50) NOT NULL,
email VARCHAR(50) UNIQUE NOT NULL,
age   INTEGER
);

INSERT INTO users (name, email, age)
VALUES ('Ramya', 'ramya@example.com', 21);

INSERT INTO users (name, email, age)
VALUES ('Priya', 'priya@example.com', 24);

INSERT INTO users (name, email, age)
VALUES ('Ravi', 'ravi@example.com', 21);

INSERT INTO users (name, email, age)
VALUES ('Meena', 'meena@example.com', 25);

INSERT INTO users (name, email, age)
VALUES ('Arjun', 'arjun@example.com', 23);

SELECT * FROM users;


SELECT * FROM users 
WHERE age > 22;


SELECT * FROM users
ORDER BY name ASC;


SELECT * FROM users
ORDER BY age DESC;


SELECT name, email FROM users
ORDER BY id ASC;