import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

# Wait for a specified amount of time for a certain condition to be true
# Waits for dynamically located elements, gives better options and intelligent than implicit wait
class explicit_waits:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/autocomplete")
        # its a example for scenarios/autocomplete.py
        # I used time.sleep(1) for no sync issues, now use explicit wait
        el = driver.find_element(By.ID, "autocomplete")
        el.send_keys("Çengelköy, Vahdettin Köșkü, Şehitler Yolu Sokak, Üsküdar/İstanbul")

        try:
            element_visible = EC.visibility_of_element_located((By.CLASS_NAME, "dismissButton"))
            WebDriverWait(driver, 5).until(element_visible)
        except TimeoutException:
            print("Timed out waiting for item load")
        finally:
            print("explicit wait works")

        el = driver.find_element(By.CLASS_NAME, "dismissButton")
        el.click()

