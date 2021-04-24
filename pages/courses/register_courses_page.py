from base.basepage import BasePage
import logging
import utilities.custom_logger as cl
import time
from selenium import webdriver

class RegisterCoursesPage(BasePage):

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locators:
    _search_box = "//input[@id='search']" #xpath
    _search_button = '//button[@type="submit"]' #xpath
    _course_name = "//h4[@class='dynamic-heading']" #xpath
    _enroll_button = "//div[@class='col-md-8 col-md-offset-2']//button" #xpath
    _cc_num = "//input[@name='cardnumber']" #xpath
    _num_iframe = "__privateStripeFrame4855" #name
    _cc_exp = "exp-date" #name
    _exp_iframe = "__privateStripeFrame4857"
    _cc_cvv = "cvc" #name
    _cvc_iframe = "__privateStripeFrame4856"
    _submit_enroll = "free" #name
    _enroll_error_message = "//span[text()='Your card number is invalid.']" #xpath

    def enter_course_name(self, name):
        self.element_send(name, self._search_box, "xpath")
        self.element_click(self._search_button, "xpath")

    def select_course_to_enroll(self, full_course_name):
        JS_course_name = self.get_text(self._course_name, "xpath")
        if full_course_name.lower() == JS_course_name.lower():
            self.element_click(self._course_name, "xpath")

    def enter_card_num(self, num):
        time.sleep(6)
        self.switch_frame_by_index(self._cc_num)
        self.element_send(num, self._cc_num, "xpath")
        self.switch_to_default()

    def enter_card_exp(self, exp):
        self.switch_frame_by_index(self._cc_exp, "name")
        self.element_send(exp, self._cc_exp, "name")
        self.switch_to_default()

    def enter_card_cvv(self, cvv):
        self.switch_frame_by_index(self._cc_cvv, "name")
        self.element_send(cvv, self._cc_cvv, "name")
        self.switch_to_default()

    def click_enroll_submit_button(self):
        self.element_click(self._submit_enroll, "name")

    def enter_credit_card_info(self, num, exp, cvv):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)

    def enroll_course(self, num="", exp="", cvv=""):
        self.element_click(self._enroll_button, "xpath")
        self.driver.execute_script("window.scrollBy(0, 700);")
        time.sleep(2)
        self.enter_credit_card_info(num, exp, cvv)
        self.click_enroll_submit_button()

    def verify_enroll_failed(self):
        if self.is_element_present(self._enroll_error_message, "xpath"):
            time.sleep(3)
            return self.is_element_displayed(self._enroll_error_message, "xpath")
        else:
            return False