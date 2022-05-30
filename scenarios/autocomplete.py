from selenium.webdriver.common.by import By
import time
class autocomplete_scenario:

    def start(self, driver):

        el = driver.find_element(By.ID, "autocomplete")
        el.send_keys("Çengelköy, Vahdettin Köșkü, Şehitler Yolu Sokak, Üsküdar/İstanbul")
        time.sleep(1)

        el = driver.find_element(By.CLASS_NAME, "dismissButton")
        el.click()

        el = driver.find_element(By.ID, "street_number")
        el.send_keys("Şehitler Yolu Sokak")

        el = driver.find_element(By.ID, "locality")
        el.send_keys("Istanbul")

        el = driver.find_element(By.ID, "postal_code")
        el.send_keys("34680")

        el = driver.find_element(By.ID, "country")
        el.send_keys("Türkiye")