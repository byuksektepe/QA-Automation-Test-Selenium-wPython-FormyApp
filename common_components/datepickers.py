from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class datepickers:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/datepicker")
        el_datepicker = driver.find_element(By.ID, "datepicker")
        el_datepicker.click()

        el_datepicker.send_keys("05/08/2021")
        el_datepicker.send_keys(Keys.RETURN)