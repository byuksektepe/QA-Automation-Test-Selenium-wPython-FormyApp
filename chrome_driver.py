from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class chrome_driver:

    def set(self):
        chrome_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return chrome_driver
    pass
#end