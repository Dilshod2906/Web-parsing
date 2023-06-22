from bs4 import BeautifulSoup
import requests
import logging 
from aiogram import Bot,Dispatcher,executor,types
from config import API_TOKEN
from buttans import natija

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("salom botimizga xush kelibsiz  \n Toshkent ob-havo malumotlarini bilish uchun kerakli kunni tanlang ☀️☀️☀️",reply_markup=natija)

@dp.message_handler()
async def havo(message: types.Message):

    sayt_url1 = "https://weather.com/uz-UZ/ob-havo/10kun/l/Toshkent?canonicalCityId=f879fcadcba322a7d9bd310904607e224fa03180c1791cb15667f33fa61ae54e"
    my_user_agent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}

    full_malumot_olish = requests.get(sayt_url1,headers=my_user_agent)
    qirqib_olish = BeautifulSoup(full_malumot_olish.content,"html.parser")

    malumotni_olish1 = qirqib_olish.findAll('div',{'data-testid':'ConditionsSummary'})
    malumotni_olish2 = qirqib_olish.findAll('div',{'class':'DaypartDetails--Content--2Yg3_ DaypartDetails--contentGrid--2_szQ'})
    malumotni_olish3 = qirqib_olish.findAll('span',{'data-testid':'TemperatureValue'})
    if message.text == "Bugun 👆":
        await message.answer(f"Bugungi malumot  {malumotni_olish1[0].text}  😊")
    elif message.text == "Erta 👆":
        await message.answer(f"Ertagi malumot{malumotni_olish2[0].text}  😊")
    elif message.text == "keyingi kun 👆":
        await message.answer(f"keyingi kun {malumotni_olish3[0].text}  😊")


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)

