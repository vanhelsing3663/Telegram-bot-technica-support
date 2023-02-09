import sqlite3 as sq

# Создаем таблицу Справки где прописываем такие атрибуты как:
#         первичный ключ с автоинкрементом
#         наименование справки, адрес получение
#         cur.execute('''CREATE TABLE IF NOT EXISTS  information(
#         id INTEGER PRIMARY KEY ,
#         information_name TEXT NOT NULL,
#         receiving_address TEXT NOT NULL
#         )''')
#         Создаем таблицу Сотрудники где прописываем такие атрибуты как:
#         первичный ключ с автоинкрементом
#         имя,фамилия,отчество,email,паспортные данные,должность сотрудника
with sq.connect('RZHD_BOT.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    patronymic TEXT NOT NULL,
    email TEXT NOT NULL,
    data_passport TEXT NOT NULL,
    job_title TEXT NOT NULL,
    emp_id INTEGER ,
    CONSTRAINT InformEmployee,
    FOREIGN KEY (emp_id)
    REFERENCES information (id)
    )''')

    cur.execute('''
        INSERT INTO  employees (name, surname, patronymic, email, data_passport,job_title,emp_id) VALUES
        ('Кирилл','Коннов','Максимович','konnov360@gmail.com','7915636718','Инженер',2),
        ('Игорь','Рассомахин','Максимович','igor345@gmail.com','7715636718','Старший-Инженер',2),
        ('Андрей','Гуцал','Александрович','andro30@gmail.com','7615636718','Инженер 1 категории',3),
        ('Вячеслав','Дацик','Петрович','vycheslav1000@gmail.com','7415636718','Инженер 2 категории',4),
        ('Денис','Петров','Иванович','den60@gmail.com','7315636718','Инженер 1 категории',5),
        ('Анатолий','Иванов','Игоревич','tolya360@gmail.com','7215636718','Инженер 2 категории',6),
        ('Павел','Ивлеев','Игоревич','pavel30@gmail.com','7515322718','Инженер 1 категории',6);
        ''')
    cur.execute('''
        INSERT INTO information (id, information_name, receiving_address) VALUES
        (1,'Справка по месту требования','Город Ярославль Волжская набережная 59'),
        (2,'Справка о стаже','Город Ярославль Волжская набережная 59'),
        (3,'Справка за выслугу лет','Город Ярославль Волжская набережная 59'),
        (4,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59'),
        (6,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59')
        ''')

    # дамп базы данных
    # with open('sql_damp.sql', 'r') as f:
    #     sql = f.read()
    #     cur.executescript(sql)
