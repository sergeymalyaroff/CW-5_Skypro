import psycopg2
from db_config import DB_CONFIG

def create_tables():
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS companies (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacancies (
        id SERIAL PRIMARY KEY,
        company_id INTEGER REFERENCES companies(id),
        title VARCHAR(255),
        salary VARCHAR(255),
        url VARCHAR(255)
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def insert_company(name, description):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO companies (name, description) VALUES (%s, %s) RETURNING id", (name, description))
    company_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return company_id

def insert_vacancy(company_id, title, salary, url):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO vacancies (company_id, title, salary, url) VALUES (%s, %s, %s, %s)", (company_id, title, salary, url))

    conn.commit()
    cursor.close()
    conn.close()
