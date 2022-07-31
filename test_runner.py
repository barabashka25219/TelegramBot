#!/usr/bin/env python3

import unittest
from test_check_settings import TestSettings

# Тест работы с фалом настроек
settingsTestSuite = unittest.TestSuite()
settingsTestSuite.addTest(unittest.makeSuite(TestSettings))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(settingsTestSuite)
