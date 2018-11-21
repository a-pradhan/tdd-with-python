import os
from selenium import webdriver
import unittest

DRIVER_PATH = os.path.realpath(os.path.join(__file__, '../webdrivers/MicrosoftWebDriver.exe'))


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Edge(executable_path=DRIVER_PATH)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # User navigates to the home page
        self.browser.get('http://localhost:8000')

        # User notices the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)

        # User is invited to enter a to-do item
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
