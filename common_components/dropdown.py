from selenium.webdriver.common.by import By


class dropdown:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/dropdown")
        # el = driver.find_element(By.ID, "")