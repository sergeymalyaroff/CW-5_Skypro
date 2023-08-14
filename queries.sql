CREATE TABLE IF NOT EXISTS employers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS vacancies (
    id SERIAL PRIMARY KEY,
    employer_id INTEGER REFERENCES employers(id),
    name VARCHAR(255),
    salary_from INTEGER,
    salary_to INTEGER,
    link VARCHAR(255)
);
