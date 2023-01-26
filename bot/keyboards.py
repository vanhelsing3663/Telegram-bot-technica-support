from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

key_board = ReplyKeyboardMarkup(resize_keyboard=True)  # Меню при старте бота которое будет видеть пользователь
button1 = KeyboardButton(text='🚂Главное меню для сотрудников🚂')
button2 = KeyboardButton(text='🚂Для сотрудников технической поддержки🚂')
button3 = KeyboardButton(text='🚂Вспомогательная информации по использованию бота🚂')
key_board.add(button1, button2).add(button3)

key_board_of_menu_support = ReplyKeyboardMarkup(resize_keyboard=True)
b_1 = KeyboardButton('🚂Полезные статьи для технической поддержки🚂')
b_2 = KeyboardButton('🚂Местоположение организации🚂')
b_3 = KeyboardButton('🚂Контактная информация🚂')
b_4 = KeyboardButton('/back_to_start_menu')
key_board_of_menu_support.add(b_1, b_2).add(b_3).add(b_4)

key_board_geo_position = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения геолакации организации
btn1 = KeyboardButton(text='/location')
btn2 = KeyboardButton(text='/back')
key_board_geo_position.add(btn1, btn2)

key_board_contact_info = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения Контактной информации
butn1 = KeyboardButton(text='/contactinfo')
butn2 = KeyboardButton(text='/back')
key_board_contact_info.add(butn1, butn2)

key_board_help = ReplyKeyboardMarkup(resize_keyboard=True)  # кнопка получения справочной информации по боту
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/back_to_start_menu')
key_board_help.add(b1, b2)

key_board_back = ReplyKeyboardMarkup(resize_keyboard=True)
bb1 = KeyboardButton(text='/back_to_start_menu')

key_board_back_to_start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
bb2 = KeyboardButton(text='/back_to_start_menu')
key_board_back_to_start_menu.add(bb2)