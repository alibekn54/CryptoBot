from aiogram import Bot, Dispatcher, executor, types
from config import bot_token
import logging
from pycoingecko import CoinGeckoAPI

from markups import cripto_list
logging.basicConfig(level=logging.INFO)

bot = Bot(bot_token)
dp = Dispatcher(bot)
cg = CoinGeckoAPI()


async def startUp(_):
    print('Бот запущен го тестить')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id,  f'Выберите криптовалюту', reply_markup=cripto_list)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        result = cg.get_price(ids=message.text, vs_currencies='usd')
        try:
            await bot.send_message(message.from_user.id, f'Криптовалюта: {message.text.lower()}\nСтоимость на данный момент {result[message.text.lower()]["usd"]}$')
        except:
            await message.answer('Введите корректную криптовалюту!!!')



@dp.callback_query_handler(text_contains='cc_')
async def cripto(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    print(call.data)
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies='usd')
    await bot.send_message(call.from_user.id, f'Криптовалюта: {currency}\nСтоимость на данный момент {result[currency]["usd"]}$', reply_markup=cripto_list)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startUp)

