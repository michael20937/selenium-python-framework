from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.check_status import CheckStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_set_up(self, one_time_set_up):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = CheckStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234567812345678", "1234", "123"), ("Selenium WebDriver Advanced", "1234567812345678", "1234", "123"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_cvv):
        self.courses.enter_course_name(course_name)
        time.sleep(3)
        self.courses.select_course_to_enroll(course_name)
        time.sleep(3)
        self.courses.enroll_course(num=cc_num, exp=cc_exp, cvv=cc_cvv)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment verification FAILED")
        self.courses.web_scroll()
        self.driver.find_element_by_link_text("ALL COURSES").click()
        time.sleep(5)