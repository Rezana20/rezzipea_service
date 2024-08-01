### Datbase Rules
1. Table name should be singular.
2. Table name should not be added/duplicated into a table attribute. Example user.id is preferred over user.user_id


### Subscriber Table
```
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
```

### Table: users
```
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name STRING NOT NULL,
    email STRING UNIQUE NOT NULL,
    password_hash STRING NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now()
);```
```
### Table: recipe_book
```
CREATE TABLE recipe_book (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    name STRING NOT NULL,
    description TEXT,
    image_location STRING,  -- Optional image location attribute
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now(),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### Table: tag
```
CREATE TABLE tag (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name STRING UNIQUE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now()
);
```

### Table: recipe
```
CREATE TABLE recipe (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipe_book_id UUID NOT NULL,
    title STRING NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now(),
    FOREIGN KEY (recipe_book_id) REFERENCES recipe_book(id)
);
```

### Table: recipe_tag
```
CREATE TABLE recipe_tag (
    recipe_id UUID NOT NULL,
    tag_id UUID NOT NULL,
    PRIMARY KEY (recipe_id, tag_id),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    FOREIGN KEY (tag_id) REFERENCES tag(id)
);
```

### Table: recipe_instruction
```
CREATE TABLE recipe_instruction (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipe_id UUID NOT NULL,
    step_number INT NOT NULL,
    instruction TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now(),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id),
    UNIQUE (recipe_id, step_number)  -- Ensure unique step numbers per recipe
);
```

### Table: recipe_ingredient
```
CREATE TABLE ingredient (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    recipe_id UUID NOT NULL,
    name STRING NOT NULL,
    quantity_value DECIMAL(10, 2),  -- Stores the numeric value of the quantity
    quantity_unit STRING,  -- Stores the unit of measurement
    created_at TIMESTAMPTZ DEFAULT now(),
    updated_at TIMESTAMPTZ DEFAULT now() ON UPDATE now(),
    FOREIGN KEY (recipe_id) REFERENCES recipe(id)
);
```
