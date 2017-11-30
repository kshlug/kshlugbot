#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from telegram.error import BadRequest
import logging
updater = Updater('your_TOKEN')
logging.basicConfig(filename='mylogs.txt', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

#Robot Function
def cuskeyboard(bot, update):
    custom_keyboard = [['/site', '/group'], ['/jalasat', '/location', '/podcast']]
    reply_markup=ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(update.message.chat_id, "به ربات تلگرام گروه کاربران لینوکس کرمانشاه خوش امدید یکی از گزینه ها رو انتخاب کن", reply_markup= reply_markup)


def site_link(bot, update):
    bot.sendMessage(update.message.chat_id, "🔗 آدرس سایت کرمانشاه لاگ:\nhttp://kshlug.ir")
def gp_link(bot, update):
    bot.sendMessage(update.message.chat_id, "👥 لینک گروه کرمانشاه لاگ :\nhttps://tiny.cc/Kermanshah")
def barnameh_jalasat(bot, update):
    with open('/home/sabulous/kshlugbot/jalasat.md') as j:
        jalasatmd = j.read()
        bot.sendMessage(update.message.chat_id, jalasatmd, parse_mode='Markdown')
def sendloc(bot, update):
    chat_id = update.message.chat_id
    bot.sendLocation(chat_id,'34.33587298', '47.08713663')
    bot.sendMessage(update.message.chat_id, " اینم لینک نقشه اوپن استریت مپ به شدت توصیه میکنم http://www.openstreetmap.org/#map=19/34.3358743/47.0872472")

def podcast(bot, update):
    with open('/home/sabulous/kshlugbot/podcast.md') as f:
        podcastmd = f.read()
        bot.sendMessage(update.message.chat_id, podcastmd, parse_mode='Markdown')

def callback_errorhandler(bot, update, error):
    try:
        raise error
    except BadRequest:
        print ("Bad Request")
        logging.getLogger().info("Bad Request")
        bot.sendMessage(update.message.chat_id, "متاسفانه هنوز چنین دستوری تعریف نشده")

# Robot Handler
updater.dispatcher.add_handler(CommandHandler('start', cuskeyboard))
updater.dispatcher.add_handler(CommandHandler('site', site_link))
updater.dispatcher.add_handler(CommandHandler('group', gp_link))
updater.dispatcher.add_handler(CommandHandler('jalasat', barnameh_jalasat))
updater.dispatcher.add_handler(CommandHandler('location', sendloc))
updater.dispatcher.add_handler(CommandHandler('podcast', podcast))
updater.dispatcher.add_error_handler(callback_errorhandler)
updater.start_polling()
# for exit
updater.idle()
