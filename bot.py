from glob import glob
import logging
from random import choice
import requests


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
from PIL import Image
from io import BytesIO
from emoji import emojize

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']

def greet_user(bot, update, user_data):
    logging.info("/start commited")
    emo = get_user_emo(user_data)
    user_data['emo'] = emo
    text = 'Привет {}'.format(emo)
    update.message.reply_text(text)

def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = "Привет, {} {}! Ты написал: '{}'".format(update.message.chat.first_name, emo, update.message.text)
    logging.info("User: %s, Chat ID: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

def send_cat_pic(bot, update, user_data):
    cat_list = glob("images/cat*.jp*g")
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))
    logging.info("User: %s, Chat ID: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)

def send_cat_pic_rnd(bot, update, user_data):
    url="https://api.thecatapi.com/v1/images/search"
    r= requests.get(url)
    logging.info("User: %s, Chat ID: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text)
    if (r.status_code != 200):
        update.message.reply_text('Sorry, there is a problem retrieving a picture.')
    else:
        data=json.loads(r.text)
        url=data[0]['url']
        print(url)
        r= requests.get(url)
        bot.send_photo(chat_id=update.message.chat.id, photo=Image.open(BytesIO(r.content)))

def main():
    mybot = Updater(settings.API_KEY)
    
    logging.info("Bot started")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_pic,  pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me,  pass_user_data=True))

    mybot.start_polling()
    mybot.idle()

main()
