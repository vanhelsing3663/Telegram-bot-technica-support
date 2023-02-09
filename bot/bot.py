from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from import_of_message.message_answer import HtmlText
from keyboards import Keyboard
from config import TOKEN
from information_about_video.video_array import Video
import random
from scripts_database import Database

# Объект бота
bot = Bot(TOKEN)  # экземпляр бота , connection API
dp = Dispatcher(bot)
kb = Keyboard()
db = Database()
video = Video()
htm = HtmlText()

async def start_up_bot(_):
    print('Бот начал свою работу и готов к использованию  ')


async def random_video(message: types.Message):
    random_video = random.choice(video.array_video())
    await bot.send_message(chat_id=message.chat.id,
                           text=random_video,
                           reply_markup=kb.inline_buttons()
                           )


@dp.message_handler(commands=['start'])
async def bot_launch(message: types.Message):
    '''
       Функции запуска бота в чат с ботом вводиться /start
    после чего бот приветствует пользователя по его id юзера
    message - это сообзение которое будет возвращенно пользователю '''
    await message.answer(text=f'{htm.user_greeting()} {message.from_user.first_name} {htm.user_greeting_from_user_id()}',
                         parse_mode='HTML',
                         reply_markup=kb.menu_on_start_bot()
                         )  # приветствие пользователя
    await bot.send_photo(message.from_user.id,
                         photo='https://im.kommersant.ru/gboxtexts/sp_com/logos/005.jpg')
    # ссылка на картинку и отправка ее вместе с приветсвием пользователя
    await message.delete()  # команда для удаление команд /% при ее вводе или нажатии на кнопку


@dp.message_handler(commands=['help'])
async def desc_command(message: types.Message):
    '''
        Фукнция для просмотра справки по боту вводиться /help
    :param message:сообщение которое выводиться
    возвращается полная справка по боту
    '''
    await message.answer(text=htm.return_help_info(), parse_mode='HTML',
                         reply_markup=kb.button_help_on_bot()
                         )
    await message.delete()


@dp.message_handler(commands=['contactinfo'])
async def contact_info(messages: types.Message):
    '''Функция для просмотра контактной информации вводиться /contactinfo
    Возвращается к.и (сайты, ссылки на социальные сети,адрес и т.д) '''
    await messages.answer(text=htm.return_contact_info(), parse_mode='HTML', reply_markup=kb.button_contact_information())
    await messages.delete()


@dp.message_handler(commands=['location'])
async def location_organization(message: types.Message):
    '''Функция возврата организации на карте вводиться /location
    Возвращается информация на гугл картах которая содержит в себе кординаты и адрес организации
    " Северная железная дорога " '''
    await message.answer(text=htm.return_location(), parse_mode='HTML')
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=57.636032,
                            longitude=39.890337,
                            reply_markup=kb.button_geopozition()
                            )
    # кординаты организации 57.636032, 39.890337 из гугл карт
    await message.delete()


@dp.message_handler(Text(equals='🚂Назад🚂'))
async def back_to_menu(message: types.Message):
    await message.answer(text='Вы вернулись на раздел назад',
                         reply_markup=kb.menu_support())
    await message.delete()


@dp.message_handler(Text(equals='🚂Главное меню для сотрудников🚂'))
async def menu_of_support(message: types.Message):
    await message.answer(text='Вы перешли в главное меню',
                         reply_markup=kb.menu_support())
    await message.delete()


@dp.message_handler(
    Text(equals='🚂Полезные видео для специалистов технической поддержки🚂'))  # дописать кнопку со статьями
async def article_support(message: types.Message):
    await message.answer(text='Вы перешли в этот раздел для просмотра статей',
                         reply_markup=kb.button_random_video())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вывести случайное видео🚂'))
async def send_random_article(message: types.Message):
    await random_video(message)


@dp.message_handler(Text(equals='🚂Местоположение организации🚂'))
async def recieve_location_organization(message: types.Message):
    await message.answer(text='Вы перешли в этот раздел для просмотра местоположения организации',
                         reply_markup=kb.button_geopozition())
    await message.delete()


@dp.message_handler(Text(equals='🚂Контактная информация🚂'))
async def recieve_contact_info_organization(message: types.Message):
    await message.answer(text='Вы перешли в этот раздел для просмотра контанктной информации организации',
                         reply_markup=kb.button_contact_information())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вспомогательная информации по использованию бота🚂'))
async def help_information_bot(message: types.Message):
    await message.answer(text='Вы перешли в раздел вспомогательной информации по боту @RZD_TECHNICAL_BOT',
                         reply_markup=kb.button_help_on_bot())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вернуться в Стартовое меню🚂'))
async def help_information_bot(message: types.Message):
    await message.answer(text='Вы перешли в раздел вспомогательной информации по боту @RZD_TECHNICAL_BOT',
                         reply_markup=kb.menu_on_start_bot())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вспомогательная информации по использованию бота🚂'))
async def help_info_of_support(message: types.Message):
    await message.answer(text='Вы перешли в раздел вспомогательной ифнормации',
                         reply_markup=kb.button_help_on_bot())
    await message.delete()


@dp.message_handler(Text(equals='🚂Для сотрудников технической поддержки🚂'))
async def request_bd(message: types.Message):
    await message.answer(text='Вы перешли в раздел для специалистов тех поддержки',
                         reply_markup=kb.key_board_bd())
    await message.delete()


@dp.message_handler(Text(equals='🚂Запросы на вывод🚂'))
async def request_bd(message: types.Message):
    await message.answer(text='Вы перешли в раздел сформированных запросов БД',
                         reply_markup=kb.button_select_info())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вернуться назад🚂'))
async def back_menu(message: types.Message):
    await message.answer(text='Вы вернулись назад',
                         reply_markup=kb.menu_support())
    await message.delete()


@dp.message_handler(Text(equals='🚂Вывести всех сотрудников с их личной информацией🚂'))
async def conclusion_employees(message: types.Message):
    await message.answer(text=db.convert_to_string_employees())
    await message.delete()

@dp.message_handler(Text(equals='🚂Вывести имя, фамилию и справку которую заказал сотрудник🚂'))
async def consolution_email_name(message:types.Message):
    await message.answer(text=db.convert_inf_employees())
    await message.delete()

@dp.message_handler(Text(equals='🚂Вывести все виды справок🚂'))
async def consolution_information(message:types.Message):
    await message.answer(text=db.convert_information())
    await message.delete()

@dp.message_handler(Text(equals='🚂Вывести все почты сотрудников🚂'))
async def consolution_email(message:types.Message):
    await message.answer(text=db.convert_email())

flag = False
@dp.callback_query_handler()
async def callback_video_random(callback: types.CallbackQuery):
    global flag
    if callback.data == 'like':
        if not flag:
            await callback.answer('Спасибо, мы рады ,что вам понравился наш материал!')
            flag = not flag
        else:
            await callback.answer('Вы уже лайкнули')
    elif callback.data == 'dislike':
        if not flag:
            await callback.answer('Спасибо, за честный ответ,будем работать над этим!')
            flag = not flag
        else:
            await callback.answer('Мы вас уже услышали,спасибо)')

    else:
        await random_video(message=callback.message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=start_up_bot)
