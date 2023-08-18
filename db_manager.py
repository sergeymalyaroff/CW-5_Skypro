"""Module for working with the HH.ru API and the PostgreSQL database."""

import requests
import psycopg2
from db_config import DB_CONFIG

BASE_URL = "https://api.hh.ru/"
HEADERS = {
    "User-Agent": "CompanyVacancyFetcher/1.0 (sergeymalyaroff@yandex.ru)"
}


def get_employer_id(company_name):
    response = requests.get(BASE_URL + "employers", params={"text": company_name}, headers=HEADERS)

    data = response.json()
    if 'items' in data and data['items']:
        return data['items'][0]['id']
    else:
        print(f"Error fetching data for {company_name}: {data.get('description', 'Unknown error')}")
        return None


def get_vacancies_for_employer(employer_id):
    response = requests.get(BASE_URL + "vacancies", params={"employer_id": employer_id}, headers=HEADERS)
    data = response.json()

    if 'items' in data:
        return data['items']
    else:
        print(f"Unexpected data structure for employer_id {employer_id}: {data}")
        return []


def insert_into_db(company, vacancies):
    """
    Insert company and its vacancies into the database.

    :param company: Company name.
    :param vacancies: List of vacancies.
    """
    with psycopg2.connect(**DB_CONFIG) as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO employers (name) VALUES (%s) RETURNING id;", (company,))
        employer_id = cur.fetchone()[0]

        for vacancy in vacancies:
            cur.execute(
                """
                INSERT INTO vacancies (employer_id, name, salary_from, salary_to, link)
                VALUES (%s, %s, %s, %s, %s);
                """,
                (
                    employer_id, vacancy['name'],
                    vacancy['salary']['from'] if vacancy['salary'] else None,
                    vacancy['salary']['to'] if vacancy['salary'] else None,
                    vacancy['alternate_url']
                )
            )
        conn.commit()


def main():
    """
    Main function: fetches vacancies for desired companies and inserts them into the database.
    """
    companies = ["Yandex", "НЛМК", "Сбер", "VK", "Tele2", "Lindstrom", "Альфа-Банк", "Газпромбанк"]
    company_ids = [get_employer_id(company) for company in companies]

    all_vacancies = {}
    for company, employer_id in zip(companies, company_ids):
        if employer_id:
            all_vacancies[company] = get_vacancies_for_employer(employer_id)

    for company, vacancies in all_vacancies.items():
        insert_into_db(company, vacancies)


if __name__ == "__main__":
    main()
