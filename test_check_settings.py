import unittest
import os
import json
from check_settings import check_settings

class TestSettings(unittest.TestCase):

	def setUp(self):
		self.settings_file = 'settings_test.json'
		self.empty_settings = {'api_id': '', 'api_hash': '', 'bot_token': ''}
		self.settings = {'api_id': '12345678qwerty', 'api_hash': '12345678qwerty', 'bot_token': '123456qwerty'}


	# Тест с пустым файлом
	def test_check_settings_empty(self):
		result = check_settings(settings_file=self.settings_file)
		self.assertEqual(result, self.empty_settings)


	# Тест с заполненным файлом
	def test_check_settings_full(self):
		with open(self.settings_file, 'w') as file:
			json.dump(self.settings, file)

		with open(self.settings_file, 'r') as file:
			result = check_settings(settings_file=self.settings_file)
			self.assertEqual(result, self.settings)


	def tearDown(self):
		files = os.listdir('.')

		if self.settings_file in files:
			os.remove(self.settings_file)



if __name__ == '__main__':
	unittest.main()