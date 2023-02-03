import sqlite3 as sq

with sq.connect('RZHD_TG_DB.db') as con:
    cur = con.cursor()
    # Создаем таблицу Справки где прописываем такие атрибуты как:
    # первичный ключ с автоинкрементом
    # наименование справки, адрес получение
    cur.execute('''CREATE TABLE IF NOT EXISTS  information(
        id INTEGER PRIMARY KEY ,
        information_name TEXT NOT NULL,
        receiving_address TEXT NOT NULL
        )''')
    # Создаем таблицу Сотрудники где прописываем такие атрибуты как:
    # первичный ключ с автоинкрементом
    # имя,фамилия,отчество,email,паспортные данные,должность сотрудника
    cur.execute('''CREATE TABLE IF NOT EXISTS employees( 
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT NOT NULL,
    email TEXT NOT NULL,
    data_passport TEXT NOT NULL,
    job_title TEXT NOT NULL,
    CONSTRAINT fk_employees,
    FOREIGN KEY (employee_id)
    REFERENCES information (id)
    )''')
    cur.execute('''
    INSERT INTO  employees (name, surname, patronymic, email, data_passport,job_title) VALUES
    ('Кирилл','Коннов','Максимович','konnov360@gmail.com','7815636718','Инженер'),
    ('Игорь','Рассомахин','Максимович','igor345@gmail.com','7815636718','Старший-Инженер'),
    ('Андрей','Гуцал','Александрович','andro30@gmail.com','7815636718','Инженер 1 категории'),
    ('Вячеслав','Дацик','Петрович','vycheslav1000@gmail.com','7815636718','Инженер 2 категории'),
    ('Денис','Петров','Иванович','den60@gmail.com','7815636718','Инженер 1 категории'),
    ('Анатолий','Иванов','Игоревич','tolya360@gmail.com','7815636718','Инженер 2 категории');
    ''')
    cur.execute('''
    INSERT INTO information (id, information_name, receiving_address) VALUES
    (1,'Справка по месту требования','Город Ярославль Волжская набережная 59'),
    (2,'Справка о стаже','Город Ярославль Волжская набережная 59'),
    (3,'Справка за выслугу лет','Город Ярославль Волжская набережная 59'),
    (4,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59'),
    (6,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59')
    ''')
