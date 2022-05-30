import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class sub:
    def sleep_and_quit(self, t, driver):
        ts = int(t)
        time.sleep(ts)
        driver.quit()

    def click_element(self, find_element_mode, item, page_load_wait_id, driver, require_wait = 1):
        s = 1
        if find_element_mode == "XPATH":
            click_element = driver.find_element(By.XPATH, item)
        elif find_element_mode == "ID":
            click_element = driver.find_element(By.ID, item)
        elif find_element_mode == "NAME":
            click_element = driver.find_element(By.NAME, item)
        elif find_element_mode == "CLASS_NAME":
            click_element = driver.find_element(By.CLASS_NAME, item)
        elif find_element_mode == "LINK_TEXT":
            click_element = driver.find_element(By.LINK_TEXT, item)
        else:
            raise Exception("in click_element function, find_element_mode does not match.")
            s = 0

        if s == 1:
            click_element.click()
            timeout = 5
            if require_wait == 1:
                try:
                    element_present = EC.presence_of_element_located((By.ID, page_load_wait_id))
                    WebDriverWait(driver, timeout).until(element_present)
                except TimeoutException:
                    print("Timed out waiting for page to load")
                finally:
                    print("Page/item loaded %s" % item)