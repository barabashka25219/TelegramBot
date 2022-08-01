#!/usr/bin/env python3
import telebot
import sys
from check_settings import check_settings

hello_message = "Я обучающий бот. Давай я расскажу тебе как устроен телеграм! :)"

settings = check_settings()

if settings['bot_token'] == '':
	print('Check your settings file')
	sys.exit(-1)

bot = telebot.TeleBot(settings['bot_token'])

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(
			message.chat.id, 
			f"Привет, {message.from_user.first_name} {hello_message}", 
			parse_mode='html')

bot.polling(none_stop=True)													