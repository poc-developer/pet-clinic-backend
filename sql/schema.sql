
-- Create owners table
CREATE TABLE IF NOT EXISTS owners (
	owner_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	address VARCHAR(100) NOT NULL,
	city VARCHAR(25) NOT NULL,
	telephone VARCHAR(25) UNIQUE NOT NULL
);

CREATE INDEX ON owners (name);

-- Create pets table
CREATE TABLE IF NOT EXISTS pets (
	pet_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	type VARCHAR(25),
	owner_id INTEGER NOT NULL,
	FOREIGN KEY (owner_id) REFERENCES owners (owner_id)
);
CREATE INDEX ON pets (pet_id);
CREATE INDEX ON pets (owner_id);
CREATE INDEX ON pets (name);