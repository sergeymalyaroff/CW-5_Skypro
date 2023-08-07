import requests
from db_manager import create_tables, insert_company, insert_vacancy

def get_company_info(company_name):
    # Пример функции для получения информации о компании с hh.ru (здесь должен быть ваш код)
    return {
        'name': company_name,
        'description': 'Description for ' + company_name
    }

def get_vacancies(company_id):
    # Пример функции для получения вакансий с hh.ru (здесь должен быть ваш код)
    vacancies = [
        {
            'title': 'Software Engineer',
            'salary': '1000-2000',
            'url': 'http://hh.ru/vacancy/1'
        },
        # ... другие вакансии
    ]
    return vacancies

create_tables()

COMPANIES = ["Google", "Amazon", "Facebook"] # Пример списка компаний

for company_name in COMPANIES:
    company_info = get_company_info(company_name)
    company_id = insert_company(company_info['name'], company_info['description'])

    vacancies = get_vacancies(company_id)
    for vacancy in vacancies:
        insert_vacancy(company_id, vacancy['title'], vacancy['salary'], vacancy['url'])
