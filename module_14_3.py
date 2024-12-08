# Домашнее задание по теме "Доработка бота"
# Цель: подготовить Telegram-бота для взаимодействия с базой данных.


from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from texts import *
from import_bd import select_info_from_db

api_f = open('api.txt', 'r')
api = api_f.read()
bot = Bot(token=api)
api_f.close()
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Расчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button, button2)
kb.add(button3)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')]
    ]
)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    await message.answer(select_info_from_db(1))
    with open('Product1.jpg', 'rb') as img1:
        await message.answer_photo(img1)

    await message.answer(select_info_from_db(2))
    with open('Product2.jpg', 'rb') as img2:
        await message.answer_photo(img2)

    await message.answer(select_info_from_db(3))
    with open('Product3.jpg', 'rb') as img3:
        await message.answer_photo(img3)

    await message.answer(select_info_from_db(4))
    with open('Product4.jpg', 'rb') as img4:
        await message.answer_photo(img4)

    await message.answer("Выберите продукт для покупки", reply_markup=catalog_kb)


ikb = InlineKeyboardMarkup(resize_keyboard=True)
ibutton1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ibutton2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(ibutton1, ibutton2)


@dp.message_handler(text='Информация')
async def inf(message):
    with open('Info pictures.jpg', 'rb') as img:
        await message.answer_photo(img, about, reply_markup=kb)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт! ')
    await call.answer()

@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer(hello, reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Расчитать')
async def main_menu(message):
    await message.answer('Выбрите опцию: ', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(
        'Расчёт каллорий производится по формуле: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (полных лет)')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост, см')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес, кг')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваши калории {calories}')
    except ValueError:
        await message.answer(
            'Данные введены некорректно. Введите числовые значения: полных лет, рост в сантиметрах, вес в килограммах')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
