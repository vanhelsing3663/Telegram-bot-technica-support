class HtmlText:
    HI = '<em>Привет 😀</em> <b>'
    HI2 = '</b>, <em>Добро пожаловать в нашего бота для технической поддержки компании РЖД!</em>'
    LOCATE = '<em>Наша организация на карте </em>Находится по адресу - <b>\nГород Ярославль Волжская набережная 59</b>'
    CONTACT_INFO = '<b>Номер телефона </b>- <em>8 (800) 755-50-05</em>\n<b>Адрес</b> - <em>Город Ярославль Волжская набережная 59</em> \n<b>Сайт Организации - </b><em>https://szd.rzd.ru/</em> \n<b>VK</b> - <em>https://vk.com/szd_official</em>\n<b>Telegram</b> - <em>https://t.me/szdrzd</em>'
    HELP = '<em>/help </em>- <b>команда помощник</b> \n<em>/location</em> - <b>команда для показа местонахождения организации на карте (Google maps)</b>\n<em>/contactinfo</em> - <b>Команда для получения Контактной информации</b> \n<em>/back</em> - <b>Вернуться на раздел назад</b> \n<em>/back_to_start_menu</em> - <b>Вернуться в стартовое меню</b>'

    @classmethod
    def ret_hi(cls):
        return cls

    def __init__(self):
        pass

    def user_greeting(self):
        return self.HI

    def user_greeting_from_user_id(self):
        return self.HI2

    def return_location(self):
        return self.LOCATE

    def return_contact_info(self):
        return self.CONTACT_INFO

    def return_help_info(self):
        return self.HELP