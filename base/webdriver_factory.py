from selenium import webdriver
import traceback

class WebdriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        base_url = "https://courses.letskodeit.com/"
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser =="firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver