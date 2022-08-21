import unittest
import os
from system import (
	change_dir
)

class TestSystem(unittest.TestCase):
	def setUp(self):
		self.home_path = os.environ['HOME']

	def test_change_dir_wrong_path(self):
		changed_dir = change_dir('/0123test/test4529', '/')
		self.assertEqual(changed_dir, False)

	def test_change_dir_true_path_linux(self):
		changed_dir = change_dir(self.home_path, '/')
		self.assertEqual(changed_dir, self.home_path + '/')

	def test_change_dir_wrong_path_nt(self):
		changed_dir = change_dir(self.home_path, '\\')
		self.assertEqual(changed_dir, self.home_path + '\\')

