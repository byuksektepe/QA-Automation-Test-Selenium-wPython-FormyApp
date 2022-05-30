import time
import pytest
from chrome_driver import chrome_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from sub import sub
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
sub = sub()
class main:
    chrome_driver = chrome_driver().set()
    chrome_driver.get('https://formy-project.herokuapp.com/')

    def Get_Formy_App():

        main.chrome_driver.maximize_window()

        if not "Formy" in main.chrome_driver.title:
            raise Exception("Page Could Not Load, Check Title Text")


    def sleep_and_quit(t):
        ts = int(t)
        time.sleep(ts)
        main.chrome_driver.quit()

main.Get_Formy_App()

sub.click_element(find_element_mode="XPATH", item="/html/body/div/div/li[9]/a", page_load_wait_id="name", driver=main.chrome_driver)

element_input = main.chrome_driver.find_element(By.ID, "name")
element_input.click()
element_input.send_keys("Berkant")
element_button = main.chrome_driver.find_element(By.ID, "button")
element_button.click()

# Call This lAST!
sub.sleep_and_quit(2, main.chrome_driver)
