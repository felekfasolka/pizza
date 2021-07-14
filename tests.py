
import unittest

from tests.test_maker import TestMaker, TestFullMakingGain
from tests.test_fridge import TestFridge, TestFridgeCount

try:
    from tests.test_sauce import TestSauce
except (ModuleNotFoundError, ImportError):
    TestSauce = None


class ValidationTests(unittest.TestCase):
    def test_sauce_feature(self):
        self.assertTrue(TestSauce is not None, msg='Sauce feature not found')

    def test_angry(self):
        self.assertTrue(False, msg='There is a problem with the pizza maker')


if __name__ == '__main__':
    unittest.main()
