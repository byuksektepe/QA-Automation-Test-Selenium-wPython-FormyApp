from selenium.webdriver.common.by import By


class keyboard_mouse_input_scenario:

    def start(self, driver):
        element_input = driver.find_element(By.ID, "name")
        element_input.click()
        element_input.send_keys("Berkant Yüksektepe")
        element_button = driver.find_element(By.ID, "button")
        element_button.click()