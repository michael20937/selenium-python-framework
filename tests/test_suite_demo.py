import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_tests import RegisterCoursesTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTests)

smoke_test = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smoke_test)