Описание

Эта программа позволяет получить информацию о вакансиях компаний с HH.ru, используя API HH.ru, и сохранять их в базу данных PostgreSQL.

Установка и настройка

Установка зависимостей:
bash
Copy code
pip install requests psycopg2
Настройка базы данных:
Убедитесь, что у вас установлен PostgreSQL и создайте базу данных и таблицы, которые будут использоваться программой.
Конфигурация программы:
Откройте файл db_config.py и убедитесь, что параметры соединения с базой данных верны.
Использование

Для запуска программы выполните:

bash
Copy code
python main.py
Функциональность

Получение ID работодателя:
Программа ищет компанию на HH.ru по ее названию и возвращает ID этой компании.
Получение вакансий для работодателя:
Программа получает список вакансий для конкретного работодателя по его ID.
Вставка в базу данных:
Информация о компании и связанных с ней вакансиях сохраняется в базу данных PostgreSQL.