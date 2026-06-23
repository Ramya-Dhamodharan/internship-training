CREATE TABLE posts (
    id      SERIAL PRIMARY KEY,
    title   VARCHAR(100) NOT NULL,
    content TEXT,
    user_id INTEGER REFERENCES users(id)  
);

INSERT INTO posts (title, content, user_id)
VALUES ('Ramya Post 1', 'Python', 1);

INSERT INTO posts (title, content, user_id)
VALUES ('Ramya Post 2', 'FastAPI', 1);

INSERT INTO posts (title, content, user_id)
VALUES ('Ramya Post 3', ' SQL', 1);

INSERT INTO posts (title, content, user_id)
VALUES ('Priya Post 1', 'OOP', 2);

INSERT INTO posts (title, content, user_id)
VALUES ('Ravi Post 1', 'Git', 3);

select* from posts;

UPDATE users
SET age = 20
WHERE name = 'Ramya';

UPDATE posts
SET title = 'Ramya Post 1 - Updated', content = 'Updated content'
WHERE id = 1;

DELETE FROM posts
WHERE id = 5;  

SELECT * FROM users;
SELECT * FROM posts;

SELECT
posts.id AS post_id,
posts.title AS post_title,
users.name AS author_name
FROM posts
INNER JOIN users 
ON posts.user_id = users.id
ORDER BY posts.id;


SELECT
users.name AS author_name,
posts.title AS post_title
FROM users
LEFT JOIN posts 
ON users.id = posts.user_id
ORDER BY users.id;


SELECT
users.name AS author_name,
COUNT(posts.id)AS post_count
FROM users
LEFT JOIN posts 
ON users.id = posts.user_id
GROUP BY users.name
ORDER BY post_count DESC;


SELECT COUNT(*) AS total_posts FROM posts;


SELECT AVG(age) AS average_age FROM users;


SELECT
users.name,
COUNT(posts.id) AS post_count
FROM users
LEFT JOIN posts 
ON users.id = posts.user_id
GROUP BY users.name
HAVING COUNT(posts.id) > 1;

SELECT
MAX(age) AS oldest,
MIN(age) AS youngest
FROM users;

