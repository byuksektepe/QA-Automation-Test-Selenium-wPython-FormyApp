import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class main:
    def Open_Formy_App():
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        chrome_driver.get('https://www.google.com')
        chrome_driver.maximize_window()
        if not "Google" in chrome_driver.title:
            raise Exception("Could not load page")

        chrome_driver.quit()


main.Open_Formy_App()
