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
            raise Exception("Page Could Not Load, Check Title Text")


    def sleep_and_quit():
        time.sleep(2)
        main.chrome_driver.quit()

    def click_element(find_element_mode, item):
        s = 1
        if find_element_mode == "XPATH":
            click_element = main.chrome_driver.find_element(By.XPATH, item)
        elif find_element_mode == "ID":
            click_element = main.chrome_driver.find_element(By.ID, item)
        elif find_element_mode == "NAME":
            click_element = main.chrome_driver.find_element(By.NAME, item)
        elif find_element_mode == "CLASS_NAME":
            click_element = main.chrome_driver.find_element(By.CLASS_NAME, item)
        else:
            raise Exception("in click_element function, find_element_mode does not match.")
            s = 0

        if s == 1:
            click_element.click()


main.Get_Formy_App()
main.click_element(find_element_mode="XPATH", item="/html/body/div/div/li[9]/a")

# Call This lAST!
main.sleep_and_quit()
