from selenium.webdriver.common.by import By

# Waits for a specified amount of time before throwing a no such element exception
# Default wait time is 0
class implicit_waits:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/autocomplete")
        # its a example for scenarios/autocomplete.py
        # I used time.sleep(1) for no sync issues, now use implicit_wait
        el = driver.find_element(By.ID, "autocomplete")
        el.send_keys("Çengelköy, Vahdettin Köșkü, Şehitler Yolu Sokak, Üsküdar/İstanbul")
        # time.sleep(1)
        driver.implicitly_wait(5)
        el = driver.find_element(By.CLASS_NAME, "dismissButton")
        el.click()