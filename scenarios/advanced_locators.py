from selenium.webdriver.common.by import By


# There is the define area for advenced locators
class advanced_locators_scenario:

    @staticmethod
    def start(driver):
        # CSS Selector Examples ----->
        # <input class="q" type="text"/>
        element = driver.find_element(By.CSS_SELECTOR, "input.q")
        # <input id="q" type="text"/>
        element = driver.find_element(By.CSS_SELECTOR, "input#q")
        # <input type="radio" value="radio button"/>
        element = driver.find_element(By.CSS_SELECTOR, "input[type='radio']")
        element = driver.find_element(By.CSS_SELECTOR, "input[value='radio button']")
        # <button type="button" class="btn btn-lg btn-primary"/>
        element = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
        # <-----

        # Match Text Examples ----->
        # Exact Match
        # <div id="textField"/>
        element = driver.find_element(By.CSS_SELECTOR, "div[id='textField']")
        # By Prefix
        # <div id="textField_randomID"/>
        element = driver.find_element(By.CSS_SELECTOR, "div[id^='textField']")
        # By Suffix
        # <div id="randomID_textField"/>
        element = driver.find_element(By.CSS_SELECTOR, "div[id$='textField']")
        # By Substring
        # <div id="123_textField_randomID"/>
        element = driver.find_element(By.CSS_SELECTOR, "div[id*='textField']")
        # <-----

        # Find Child Nodes ----->
        # Child Node
        # <div id="parent">
        #   <a id="child" href="/child">Child</a>
        # </div>
        element = driver.find_element(By.CSS_SELECTOR, "div#parent a")
        # Nth-Child Node
        # <ul id="list">
        #   <li>One 1n</li>
        #   <li>Two 2n</li>
        #   <li>Three 3n</li>
        # </ul>
        element = driver.find_element(By.CSS_SELECTOR, "#list li:nth-child(n)")



