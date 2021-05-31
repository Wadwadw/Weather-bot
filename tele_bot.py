from aiogram import Bot, Dispatcher, executor, types
import logging
import parce



API_TOKEN = '#######################'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет это Бот-погоды, введи название города что бы узнать прогноз погоды на 7 дней."
                         " Нажми на /help что бы увидеть подсказки")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("Название города нужно вводить кириллицей, регистр букв не имеет значения. Города названия которых "
                         "менялись нужнно вводить в старом формате. Например если вам нужно узнать погоду в Днепре нужно ввести"
                         " Днепропетровск")

@dp.message_handler()
async def answer(message: types.Message):
    o = parce.parce(city=message.text)

    await message.answer('\n'.join(o))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)














