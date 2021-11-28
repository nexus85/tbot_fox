# https://wttr.in/Krasnodar?format=4&lang=ru

import os
import requests
from getuseragent import UserAgent


useragent = UserAgent("desktop").Random()
# TOKEN = os.environ.get('TOKEN')
TOKEN = os.getenv('TOKEN')


# res = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates', headers={"useragent":useragent})
# data = res.json()
#
# print(data['result'][2]['message']['text'])


from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import Updater

updater = Updater(token=TOKEN) #обновляетя данные
dispatcher = updater.dispatcher  #решаетя что делать с данными от ползователей










def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Напиши города, я тебе погоду")


def weather(update, context):
    city = update.message.text
    w = requests.get(f'https://wttr.in/{city}?format=3')

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=w.text)



weather_handler = MessageHandler(Filters.text & (~Filters.command), weather)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)


updater.start_polling()
updater.idle()


# print('hello')



