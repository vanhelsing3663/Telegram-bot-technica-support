import sqlite3 as sq
import re

with sq.connect('RZHD_BOT.db') as con:
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
    emp_id INTEGER ,
    CONSTRAINT InformEmployee,
    FOREIGN KEY (emp_id)
    REFERENCES information (id)
    )''')

    # cur.execute('''
    # INSERT INTO  employees (name, surname, patronymic, email, data_passport,job_title,emp_id) VALUES
    # ('Кирилл','Коннов','Максимович','konnov360@gmail.com','7915636718','Инженер',2),
    # ('Игорь','Рассомахин','Максимович','igor345@gmail.com','7715636718','Старший-Инженер',2),
    # ('Андрей','Гуцал','Александрович','andro30@gmail.com','7615636718','Инженер 1 категории',3),
    # ('Вячеслав','Дацик','Петрович','vycheslav1000@gmail.com','7415636718','Инженер 2 категории',4),
    # ('Денис','Петров','Иванович','den60@gmail.com','7315636718','Инженер 1 категории',5),
    # ('Анатолий','Иванов','Игоревич','tolya360@gmail.com','7215636718','Инженер 2 категории',6),
    # ('Павел','Ивлеев','Игоревич','pavel30@gmail.com','7515322718','Инженер 1 категории',6);
    # ''')
    # cur.execute('''
    # INSERT INTO information (id, information_name, receiving_address) VALUES
    # (1,'Справка по месту требования','Город Ярославль Волжская набережная 59'),
    # (2,'Справка о стаже','Город Ярославль Волжская набережная 59'),
    # (3,'Справка за выслугу лет','Город Ярославль Волжская набережная 59'),
    # (4,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59'),
    # (6,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59')
    # ''')
    with open('sql_damp.sql', 'w') as f:
        for sql in con.iterdump():
            f.write(sql)


    # расскоментировать, если бд по каким то причинам удалилась или была утеряна
    # with open('sql_damp.sql','r') as f:
    #     sql = f.read()
    #     cur.executescript(sql)
    def convert_to_string_employees(all_employees):
        '''Вывод всех работников из бд с помощью sql запроса'''

        # вывод всех сотрудников которые запросили справки
        s = '\n'.join(
            i[0] + ' - ' + i[1] + ' - ' + i[2] + ' - ' + i[3] + ' -паспортные данные- ' + i[4] + ' -квалификация- ' + i[
                5] for i in all_employees)
        return s


    def convert_email(all):
        '''Вывод всех имен, фамилий,емайлов и справок из бд с помощью sql запроса'''
        return f' \n'.join(i[0] for i in all)
        return all


    def convert_information(inf):
        inf = '\n'.join('Наименование справки - ' + i[0] + ' Адрес получения - ' + i[1] for i in inf)
        return inf


    def convert_inf_employees(emp):
        emp = '\n'.join(i[0] + ' ' + i[1] + ' ' + i[2] + ' Заказанная справка - ' + i[3] for i in emp)
        return emp


    all_employees = cur.execute(
        'select name,surname, patronymic, email, data_passport,job_title from employees').fetchall()

    all_information = cur.execute('SELECT information_name, receiving_address FROM information').fetchall()

    all_email_name = cur.execute('''SELECT name, surname, email, information_name
                                    FROM employees 
                                    JOIN information ON employees.emp_id = information.id''').fetchall()

    all_email = cur.execute('''SELECT email FROM employees''').fetchall()
