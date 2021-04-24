from selenium import webdriver
from pages.home.login_page import LoginPage
from utilities.check_status import CheckStatus
import unittest
import time
import pytest

@pytest.mark.usefixtures("one_time_set_up", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.lp = LoginPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("test@email.com", "abcabc")
        result1 = self.lp.verify_login_title()
        self.ts.mark(result1, "Test is incorrect")
        result2 = self.lp.verify_login_success()
        self.ts.mark_final("test_login_valid", result2, "Login was not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.log_out()
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verify_login_fail()
        assert result == True