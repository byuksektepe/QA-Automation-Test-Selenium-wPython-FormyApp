from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

        # Tarih gir
        driver.find_element(By.ID, "datepicker").send_keys("06/01/2022")



