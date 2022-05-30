from selenium.webdriver.common.by import By
import time


class switch_to_window_scenario:
    def start(self, driver):
        el_newtabbutton = driver.find_element(By.ID, "new-tab-button")
        el_newtabbutton.click()

        original_handle = driver.current_window_handle
        for handle1 in driver.window_handles:
            time.sleep(1)
            driver.switch_to.window(handle1)

        driver.switch_to.window(original_handle)