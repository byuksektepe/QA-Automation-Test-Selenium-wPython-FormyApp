from selenium.webdriver.common.by import By

class radio_buttons_and_checkboxes:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/radiobutton")

        el_radio_1 = driver.find_element(By.ID, "radio-button-1")
        el_radio_1.click()

        el_radio_2 = driver.find_element(By.CSS_SELECTOR, "input[value='option2']")
        el_radio_2.click()

        el_radio_3 = driver.find_element(By.CSS_SELECTOR, "input[value='option3']")
        el_radio_3.click()

        driver.get("https://formy-project.herokuapp.com/checkbox")

        el_check_1 = driver.find_element(By.ID, "checkbox-1")
        el_check_1.click()

        el_check_2 = driver.find_element(By.ID, "checkbox-2")
        el_check_2.click()

        el_check_3 = driver.find_element(By.ID, "checkbox-3")
        el_check_3.click()
