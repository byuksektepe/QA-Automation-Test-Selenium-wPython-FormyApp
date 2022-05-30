from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class scroll_to_element_scenario:
    def start(self, driver):
        actions = ActionChains(driver)
        el_name = driver.find_element(By.ID, "name")

        actions.move_to_element(el_name).perform()
        el_name.send_keys("Berkant Yüksektepe")

        el_date = driver.find_element(By.ID, "date")
        el_date.send_keys("5/30/2022")


