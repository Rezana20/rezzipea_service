### Datbase Rules
1. Table name should be singular. 
2. Table name should not be added/duplicated into a table attribute. Example user.id is preferred over user.user_id


### Subscriber Table

CREATE TABLE subscriber (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(255) UNIQUE NOT NULL,
    subscribed_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO subscriber (name, email)
VALUES ('Rezana', 'ganierezana8@gmail.com');

SELECT * FROM subscriber;

DELETE FROM subscriber
WHERE email = 'ganierezana8@gmail.com';