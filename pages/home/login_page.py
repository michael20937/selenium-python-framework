from selenium.webdriver.common.by import By
from pages.home.navigation_page import NavigationPage
import time
from base.basepage import BasePage
# from base.selenium_driver import SeleniumDriver ###already inherits the BasePage that inherits Selenium

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #locators - original home page
    # _login_link = "Login"
    # _email = "user_email"
    # _password = "user_password"
    # _login_button = "commit"

    #locators - courses.letskodeit.com
    _login_link = "SIGN IN"
    _email = "email"
    _password = "password"
    _login_button = "//input[@value='Login']"

    #action functions
    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def enter_email_field(self, email):
        self.element_send(email, self._email)

    def enter_password_field(self, password):
        self.element_send(password, self._password)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="xpath")

    #main login page function
    def login(self, email, password):
        self.click_login_link()
        time.sleep(3)
        self.enter_email_field(email)
        time.sleep(1)
        self.enter_password_field(password)
        time.sleep(1)
        self.click_login_button()

    def verify_login_success(self):
        result = self.is_element_present("//div[@id='course-list']/div[1]", locator_type="xpath")
        return result

    def verify_login_fail(self):
        result = self.is_element_present("//span[contains(text(), 'invalid')]", locator_type="xpath")
        return result

    def verify_login_title(self):
        return self.verify_page_title("All Courses")

    def log_out(self):
        self.nav.navigate_to_user_settings()
        self.element_click(locator="//a[@href='/logout']", locator_type="xpath")