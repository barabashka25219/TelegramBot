import json

def check_settings(settings_file='settings.json'):
	settings = {'api_id': '', 'api_hash': '', 'bot_token': ''}

	try:
		with open(settings_file, 'r') as file:
			settings = json.load(file)


	except FileNotFoundError:
		with open(settings_file, 'w') as file:
			json.dump(settings, file)
	
	return settings