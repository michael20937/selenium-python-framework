from selenium.webdriver.common.by import By
import time
from base.basepage import BasePage
# from base.selenium_driver import SeleniumDriver ###already inherits the BasePage that inherits Selenium

class NavigationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    # _practice = ""
    _user_settings_icon = "zl-navbar-rhs-img"
    _my_account = "My Account"

    def navigate_to_my_courses(self):
        self.element_click(self._my_courses, locator_type="link")

    def navigate_to_all_courses(self):
        self.element_click(self._all_courses, locator_type="link")

    def navigate_to_user_settings(self):
        self.element_click(self._user_settings_icon, locator_type="class")

    def navigate_to_my_account(self):
        self.navigate_to_user_settings()
        self.element_click(self._my_account, locator_type="link")