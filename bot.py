#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import requests
import urllib3
import audio
import apiai
import json
import os
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
        file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(BOT_API, file_info.file_path))
        with open('message.ogg','wb') as f:
                f.write(file.content)
                file.close()
        print(file_info)
@bot.message_handler(content_types=['voice'])
def voice_message(message):
    print("You are heard")
    print(message.voice.file_id)
    bot.send_message(message.from_user.id, "Функция приема голосовых сообщений временно недоступна")
    #download(message)
    #voice = audio.start()
    #if (len(voice) > 0):
        #textMessage(voice, message)
    #else:
        #bot.send_message(message.from_user.id, "Я ничего не понял, повторите еще раз")

@bot.message_handler(content_types=['text'])
def text_message(message):
        print("Text message")
        text = message.text
        textMessage(text, message)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.from_user.id, "Привет, я обучаемый бот, я понимаю как текстовые сообщения, так и голосовые")

def textMessage(voice, message):
    request = apiai.ApiAI(os.environ['CLD_TOKEN']).text_request()
    request.lang = 'ru'
    request.session_id = 'SelfLearningBot'
    request.query = voice
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=message.from_user.id, text=response)
    else:
        bot.send_message(chat_id=message.from_user.id, text='Я Вас не совсем понял!')  
bot.polling(none_stop=True, timeout=200)