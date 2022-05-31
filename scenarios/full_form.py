from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from unittest import TestCase
unittest = TestCase()

# This is for colored console messages
from colorama import Fore, Style

class full_form:
    def start(self, driver):
        actions = ActionChains(driver)
        driver.get("https://formy-project.herokuapp.com/form")

        # css selectors, burada for kullanmayı denedim, kısa oldu iyi oldu niye türkçe yazdım bilmiyorum, neyse sa.
        ID_FIELDS = [["first-name", "Berkant"], ["last-name", "Yüksektepe"],
                     ["job-title", "QA Test Automation Engineer"]]

        # Türkçe devam edelim, ID_FIELD arrayine göre sırasıyla inputları doldur
        for ID_FIELD in ID_FIELDS:
            driver.find_element(By.ID, ID_FIELD[0]).send_keys(ID_FIELD[1])

        # Sayfanın sonuna js ile kaydır
        driver.execute_script("window.scrollBy(0,250);")

        # Radio ve checkboxları işaretle
        driver.find_element(By.CSS_SELECTOR, "input[value='radio-button-2']").click()
        driver.find_element(By.CSS_SELECTOR, "input[value='checkbox-1']").click()

        # Select boxu seç
        driver.find_element(By.CSS_SELECTOR, "option[value='2']").click()

        # Tarih gir ve entera bas
        datepicker = driver.find_element(By.ID, "datepicker")
        datepicker.send_keys("06/01/2022")
        datepicker.send_keys(Keys.RETURN)

        # Formu Yolla
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary").click()

        # Formun başarıyla yollandığını doğrula
        try:
            alert_element_visible = EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success"))
            WebDriverWait(driver, 5).until(alert_element_visible)

        except TimeoutException:
            raise Exception("Timed out waiting for form submit page load")

        finally:
            get_alert = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
            alert_text = get_alert.text

            unittest.assertEqual("The form was successfully submitted!", alert_text)

            print(f"{Fore.GREEN}[PASS]{Style.RESET_ALL} Form Submitted Successfully")

        # Bu kadar



