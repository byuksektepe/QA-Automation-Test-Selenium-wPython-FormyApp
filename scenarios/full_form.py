from selenium.webdriver.common.by import By

class full_form:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/form")

        # css selectors, burada for kullanmayı denedim, kısa oldu iyi oldu niye türkçe yazdım bilmiyorum, neyse sa.
        ID_FIELDS = [["first-name", "Berkant"], ["last-name", "Yüksektepe"],
                     ["job-title", "QA Test Automation Engineer"]]

        for ID_FIELD in ID_FIELDS:
            driver.find_element(By.ID, ID_FIELD[0]).send_keys(ID_FIELD[1])



