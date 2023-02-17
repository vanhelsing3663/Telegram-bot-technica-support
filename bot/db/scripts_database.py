import sqlite3 as sq


class Database:
    def __init__(self):
        with sq.connect('../RZHD_BOT.db') as con:
            self.cur = con.cursor()

    def convert_to_string_employees(self):
        '''Вывод всех работников из бд с помощью sql запроса'''

        # вывод всех сотрудников которые запросили справки
        all_employees = self.cur.execute(
            'select name,surname, patronymic, email, data_passport,job_title from employees').fetchall()
        s = '\n'.join(
            i[0] + ' - ' + i[1] + ' - ' + i[2] + ' - ' + i[3] + ' -паспортные данные- ' + i[
                4] + ' -квалификация- ' + i[
                5] for i in all_employees)
        return s

    def convert_email(self):
        '''Вывод всех имен, фамилий,емайлов и справок из бд с помощью sql запроса'''
        all_email = self.cur.execute('''SELECT email FROM employees''').fetchall()
        return f' \n'.join(i[0] for i in all_email)

    def convert_information(self):
        '''Вывод справки и адреса ее получения'''
        all_information = self.cur.execute('SELECT information_name, receiving_address FROM information').fetchall()
        inf = '\n'.join('Наименование справки - ' + i[0] + ' Адрес получения - ' + i[1] for i in all_information)
        return inf

    def convert_inf_employees(self):
        '''Вывод фио и заказанной справки'''
        all_email_name = self.cur.execute('''SELECT name, surname, email, information_name
                                                FROM employees 
                                                JOIN information ON employees.emp_id = information.id''').fetchall()
        emp = '\n'.join(i[0] + ' ' + i[1] + ' ' + i[2] + ' Заказанная справка - ' + i[3] for i in all_email_name)
        return emp
