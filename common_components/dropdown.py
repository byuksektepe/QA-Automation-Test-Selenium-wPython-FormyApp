from selenium.webdriver.common.by import By


class dropdown:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/dropdown")
        el_dropdown_menu = driver.find_element(By.ID, "dropdownMenuButton")
        el_dropdown_menu.click()

        item = driver.find_element(By.XPATH, "/html/body/div/div/div/a[8]")
        item.click()