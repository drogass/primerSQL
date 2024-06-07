from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.key_inlane import get_keyboard_inlane, get_keyboard_inlane2, get_keyboard_inlane3
from keboard.keboards import get_keyboard_1, get_keyboard_2
from database.database import initialize_db, add_user, get_user

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

initialize_db()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_user(message.from_user.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name)
        await message.answer('Привет', reply_markup=get_keyboard_1())
    else:
        await message.answer('Привет', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправить фото пиццы')
async def handle_button_1(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://w.forfun.com/fetch/f3/f3615b5326ee913a0c8334927f736d80.jpeg', caption='Вот это пицца', reply_markup=get_keyboard_inlane2())

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def handle_button_2(message: types.Message):
    await message.answer('Переход сделан', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправить фото бургера')
async def handle_button_3(message: types.Message):
    await bot.send_photo(message.chat.id, photo='https://gas-kvas.com/grafic/uploads/posts/2023-09/1695925236_gas-kvas-com-p-kartinki-burger-3.png', caption='Вот это бургер', reply_markup=get_keyboard_inlane())

@dp.message_handler(lambda message: message.text == 'Перейти назад')
async def handle_button_4(message: types.Message):
    await message.answer('Переход сделан', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправить фото суши')
async def handle_button_5(message: types.Message):
    await bot.send_photo(message.chat.id, photo='http://npo-imp.ru/images/news/sushi.jpg', caption='Вот это суши', reply_markup=get_keyboard_inlane3())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
