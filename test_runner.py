#!/usr/bin/env python3

import unittest
from test_check_settings import TestSettings
from test_system import TestSystem

# Тест работы с фалом настроек
settingsTestSuite = unittest.TestSuite()
settingsTestSuite.addTest(unittest.makeSuite(TestSettings))

# Test for system functions 
systemTestSuite = unittest.TestSuite()
systemTestSuite.addTest(unittest.makeSuite(TestSystem))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(settingsTestSuite)
runner.run(systemTestSuite)
