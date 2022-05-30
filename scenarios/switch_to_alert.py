from selenium.webdriver.common.by import By


class switch_to_alert_scenario:
    def start(self, driver):
        el_alertbutton = driver.find_element(By.ID, "alert-button")
        el_alertbutton.click()

        alert = driver.switch_to.alert
        alert.accept()
