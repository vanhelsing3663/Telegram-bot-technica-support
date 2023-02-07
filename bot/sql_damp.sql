BEGIN TRANSACTION;CREATE TABLE employees( 
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
    );INSERT INTO "employees" VALUES(1,'Кирилл','Коннов','Максимович','konnov360@gmail.com','7915636718','Инженер',2);INSERT INTO "employees" VALUES(2,'Игорь','Рассомахин','Максимович','igor345@gmail.com','7715636718','Старший-Инженер',2);INSERT INTO "employees" VALUES(3,'Андрей','Гуцал','Александрович','andro30@gmail.com','7615636718','Инженер 1 категории',3);INSERT INTO "employees" VALUES(4,'Вячеслав','Дацик','Петрович','vycheslav1000@gmail.com','7415636718','Инженер 2 категории',4);INSERT INTO "employees" VALUES(5,'Денис','Петров','Иванович','den60@gmail.com','7315636718','Инженер 1 категории',5);INSERT INTO "employees" VALUES(6,'Анатолий','Иванов','Игоревич','tolya360@gmail.com','7215636718','Инженер 2 категории',6);INSERT INTO "employees" VALUES(7,'Павел','Ивлеев','Игоревич','pavel30@gmail.com','7515322718','Инженер 1 категории',6);CREATE TABLE information(
        id INTEGER PRIMARY KEY ,
        information_name TEXT NOT NULL,
        receiving_address TEXT NOT NULL
        );INSERT INTO "information" VALUES(1,'Справка по месту требования','Город Ярославль Волжская набережная 59');INSERT INTO "information" VALUES(2,'Справка о стаже','Город Ярославль Волжская набережная 59');INSERT INTO "information" VALUES(3,'Справка за выслугу лет','Город Ярославль Волжская набережная 59');INSERT INTO "information" VALUES(4,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59');INSERT INTO "information" VALUES(6,'Копия приказа о приеме на работу','Город Ярославль Волжская набережная 59');DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('employees',7);COMMIT;