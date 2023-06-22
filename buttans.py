from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

havo1 = KeyboardButton('Bugun 👆')
havo2 = KeyboardButton('Erta 👆')
havo3 = KeyboardButton('keyingi kun 👆')

natija = ReplyKeyboardMarkup(resize_keyboard=True).add(havo1,havo2,havo3)