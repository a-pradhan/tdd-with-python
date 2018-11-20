import os
from selenium import webdriver

DRIVER_PATH = os.path.realpath(os.path.join(__file__, '../webdrivers/MicrosoftWebDriver.exe'))
print(DRIVER_PATH)
browser = webdriver.Edge(executable_path=DRIVER_PATH)
browser.get('http://localhost:8000')

assert 'Django' in browser.title