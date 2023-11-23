import telegram
import asyncio
import schedule
import time
import pytz
import datetime


token = "6881294482:AAEwliP1LDBTVEyYYs4sGuNxeRi7S0i9qis"
# Bot: K2023_2_test_bot
# Token:6881294482:AAEwliP1LDBTVEyYYs4sGuNxeRi7S0i9qis
# chat id: -1002068226051
# 6881294482
# channel : K20232test
bot =telegram.Bot(token = token)
public_chat_name = '@K20232test'
# id_channel = bot.sendMessage(chat_id=public_chat_name, text= "alarm arrived!!!!!!!").chat_id
# print(id_channel)

chat_id = "-1002068226051"
text = 'Hello, Telegram!'
# asyncio.run(bot.sendMessage(chat_id= chat_id , text=text))
# bot.sendMessage(chat_id = chat_id , text = text)

async def async_job():
    now = time.localtime()
    text = str(now)
    await chat(text)

async def chat(str):
    await bot.sendMessage(chat_id=chat_id, text=str)
    pass

def job():
    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if (23 <= now.hour or now.hour < 6) or (now.hour == 6 and now.minute == 0):
        return  # 오후 11시부터 오전 6시까지는 작업을 실행하지 않음
    asyncio.create_task(async_job())

schedule.every(30).minutes.do(job)
#schedule.every(5).seconds.do(job)

async def main():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
