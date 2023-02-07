from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

key_board = ReplyKeyboardMarkup(resize_keyboard=True)  # Меню при старте бота которое будет видеть пользователь
button1 = KeyboardButton(text='🚂Главное меню для сотрудников🚂')
button2 = KeyboardButton(text='🚂Для сотрудников технической поддержки🚂')
button3 = KeyboardButton(text='🚂Вспомогательная информации по использованию бота🚂')
key_board.add(button1, button2).add(button3)

key_board_of_menu_support = ReplyKeyboardMarkup(resize_keyboard=True)
b_1 = KeyboardButton('🚂Полезные видео для специалистов технической поддержки🚂')
b_2 = KeyboardButton('🚂Местоположение организации🚂')
b_3 = KeyboardButton('🚂Контактная информация🚂')
b_4 = KeyboardButton('🚂Вернуться в Стартовое меню🚂')
key_board_of_menu_support.add(b_1, b_2).add(b_3).add(b_4)

key_board_geo_position = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения геолакации организации
btn1 = KeyboardButton(text='/location')
btn2 = KeyboardButton(text='🚂Назад🚂')
key_board_geo_position.add(btn1, btn2)

key_board_contact_info = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения Контактной информации
butn1 = KeyboardButton(text='/contactinfo')
butn2 = KeyboardButton(text='🚂Назад🚂')
key_board_contact_info.add(butn1, butn2)

key_board_help = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения справочной информации по боту
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='🚂Вернуться в Стартовое меню🚂')
key_board_help.add(b1, b2)

key_board_back = ReplyKeyboardMarkup(resize_keyboard=True)
bb1 = KeyboardButton(text='🚂Вернуться в Стартовое меню🚂')

key_board_back_to_start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
bb2 = KeyboardButton(text='🚂Вернуться в Стартовое меню🚂')
key_board_back_to_start_menu.add(bb2)

key_board_articles_support = ReplyKeyboardMarkup(resize_keyboard=True)
bb3 = KeyboardButton(text='🚂Вывести случайное видео🚂')
bb4 = KeyboardButton(text='🚂Назад🚂')
key_board_articles_support.add(bb3).add(bb4)

ikb = InlineKeyboardMarkup(row_width=2)
ib1 = InlineKeyboardButton(text='🤍❤️ ', callback_data='like')
ib2 = InlineKeyboardButton(text='💔  ', callback_data='dislike')
ib3 = InlineKeyboardButton(text='Следующее видео', callback_data='next')

ikb.add(ib1, ib2).add(ib3)

key_board_bd = ReplyKeyboardMarkup(resize_keyboard=True)
b_b = KeyboardButton(text='🚂Запросы на вывод🚂')
b_b2 = KeyboardButton(text='🚂Сформировать запрос🚂')
b_b3 = KeyboardButton(text='🚂Вернуться в Стартовое меню🚂')
key_board_bd.add(b_b).add(b_b2).add(b_b3)

key_board_menu_support = ReplyKeyboardMarkup(resize_keyboard=True)
bbb1 = KeyboardButton(text='🚂Вывести всех сотрудников с их личной информацией🚂')
bbb2 = KeyboardButton(text='🚂Вывести все виды справок🚂')
bbb3 = KeyboardButton(text='🚂Вывести имя, фамилию и справку которую заказал сотрудник🚂')
bbb4 = KeyboardButton(text='🚂Вывести все почты сотрудников🚂')
bbb5 = KeyboardButton(text='🚂Вернуться назад🚂')
key_board_menu_support.add(bbb1, bbb2).add(bbb3, bbb4).add(bbb5)
