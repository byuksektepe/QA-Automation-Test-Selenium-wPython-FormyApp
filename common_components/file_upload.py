from selenium.webdriver.common.by import By

class file_upload:
    def start(self, driver):
        driver.get("https://formy-project.herokuapp.com/fileupload")

        file_upload_field = driver.find_element(By.ID, "file-upload-field")
        file_upload_field.send_keys("faustx-fx1-image.png")
