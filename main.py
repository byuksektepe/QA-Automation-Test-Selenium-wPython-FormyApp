import time
import pytest
from chrome_driver import chrome_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

class main:
    chrome_driver = chrome_driver().set()
    chrome_driver.get('https://formy-project.herokuapp.com/')

    def Get_Formy_App():

        main.chrome_driver.maximize_window()

        if not "Formy" in main.chrome_driver.title:
            raise Exception("Page Could Not Load, Check Title Text")


    def sleep_and_quit():
        time.sleep(2)
        main.chrome_driver.quit()

    def click_element(find_element_mode, item, page_load_wait_id):
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
            timeout = 5
            try:
                element_present = EC.presence_of_element_located((By.ID, page_load_wait_id))
                WebDriverWait(main.chrome_driver, timeout).until(element_present)
            except TimeoutException:
                print("Timed out waiting for page to load")
            finally:
                print("Page loaded")


main.Get_Formy_App()
main.click_element(find_element_mode="XPATH", item="/html/body/div/div/li[9]/a", page_load_wait_id="name")
element_input = main.chrome_driver.find_element(By.ID, "name")
element_input.click()
element_input.send_keys("Berkant")

element_button = main.chrome_driver.find_element(By.ID, "button")
element_button.click()

# Call This lAST!
main.sleep_and_quit()
