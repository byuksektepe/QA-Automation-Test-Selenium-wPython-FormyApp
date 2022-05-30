from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



class drag_and_drop_scenario:
    def start(self, driver):
        actions = ActionChains(driver)

        drag = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "image")))
        drop = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "box")))
        actions.drag_and_drop(drag, drop).perform()

