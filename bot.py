#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import requests
import urllib
BOT_API = "730716713:AAGy7qWPNEuVkWW61h1tm9ALsNnMkl4nWDk"
bot = telebot.TeleBot(BOT_API)
def get_voice(message):
    print("GOT")
    if (message.voice.duration != 0):
        print("You are heard")
        download(message)
    else:
        print(message.from_user.id)
        bot.send_message(message.from_user.id, "Этот бот принимает только голосовые сообщения")
def download(message):
        file_info = bot.get_file(message.voice.file_id)
        file = ('https://api.telegram.org/file/bot{0}/{1}'.format(BOT_API, file_info.file_path))
        urllib.request.urlretrieve(file, file_info.file_path[6:])
        print(file_info)
@bot.message_handler(content_types=['voice'])
def voice_message(message):
    print("You are heard")
    print(message.voice.file_id)
    download(message)
bot.polling(none_stop=True, timeout=123)