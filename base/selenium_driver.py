from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():

    log = cl.CustomLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        #function gets the locator type and returns the right By.locator for it
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type='id'):
        #function gets the By.locator type and the locator itself and finds the element
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info('Element Found: ' + locator + " --- " + locator_type)
        except:
            self.log.info('Element not found: ' + locator + " --- " + locator_type)
        return element

    def is_element_present(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locator_type: " + locator_type)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locator_type: " + locator_type)
                return False
        except:
            print("Element not found")
            return False

    def element_presence_check(self, locator, by_type):
        #checks whether there are elements under the given locator
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if element_list > 0:
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info('Element not found')
            return False

    def element_click(self, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.log.info("Cannot click on the element with locator: " + locator +
                          " locator_type: " + locator_type)
        print_stack()

    def element_send(self, data, locator, locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locator_type: " + locator_type)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                  " locator_type: " + locator_type)
            print_stack()

    def wait_for_element(self, locator, locator_type="id",
                       timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def screenshot(self, result_message):
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        dir_path = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, dir_path)
        destination_dir = os.path.join(current_dir, screenshot_dir)
        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot was saved to directory: " + destination_file)
        except:
            self.log.error("### Exception occurred when taking screenshot")
            print_stack()

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locator type: " + locator_type)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locator type: " + locator_type)
            return is_displayed
        except:
            print("Element not found")
            return False

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " +  info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def get_element_list(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locator_type: " + locator_type)
        return element

    def switch_to_frame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_frame_by_index(self, locator, locator_type="xpath"):
        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locator_type="xpath")
            self.log.info("Length of IFrame list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switch_to_frame(index=iframe_list[i])
                result = self.is_element_present(locator, locator_type)
                if result:
                    self.log.info("IFrame index is: ")
                    self.log.info(str(i))
                    break
                self.switch_to_default()
            return result
        except:
            print("IFrame index not found")
            return result

    def switch_to_default(self):
        self.driver.switch_to.default_content()