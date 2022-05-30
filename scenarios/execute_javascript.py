from selenium.webdriver.common.by import By
import time

class execute_javascript_scenario:
    def start(self, driver):
        el_modalbutton = driver.find_element(By.ID, "modal-button")
        el_modalbutton.click()

        el_closebutton = driver.find_element(By.ID, "close-button")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", el_closebutton)