import time

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
    chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome_driver.get('https://formy-project.herokuapp.com/')

    def Get_Formy_App():

        main.chrome_driver.maximize_window()

        if not "Formy" in main.chrome_driver.title:
            raise Exception("Could not load page")


    def sleep_and_quit():
        time.sleep(3)
        main.chrome_driver.quit()


main.Get_Formy_App()
main.sleep_and_quit()
