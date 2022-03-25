from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnBitcoin = InlineKeyboardButton(text='Bitcoin', callback_data='cc_bitcoin')
btnLitecoin = InlineKeyboardButton(text='Litecoin', callback_data='cc_litecoin')
btnDogecoin = InlineKeyboardButton(text='Dogecoin', callback_data='cc_dogecoin')

cripto_list = InlineKeyboardMarkup(row_width=1)
cripto_list.insert(btnBitcoin)
cripto_list.insert(btnLitecoin)
cripto_list.insert(btnDogecoin)

