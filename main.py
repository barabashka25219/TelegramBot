#!/usr/bin/env python3
import pyrogram
import os
from check_settings import check_settings

if 'NewsBot.session' not in os.listdir('.'):
	settings = check_settings()
	api_id = settings['api_id']
	api_hash = settings['api_hash']
	bot_token = settings['bot_token']

	if api_id == '' or api_hash == '' or bot_token == '':
		print('Check your settings file.')


	else:
		client = pyrogram.Client('NewsBot', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

else:
	client = pyrogram.Client('NewsBot')
	
