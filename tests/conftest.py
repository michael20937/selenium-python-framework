import pytest
from selenium import webdriver
from base.webdriver_factory import WebdriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def set_up():
    print('running method SET UP')
    yield
    print('running method TEAR DOWN')

@pytest.fixture(scope="class") #scope="module" when testing individual methods
def one_time_set_up(request, browser, os):
    print('conftest runs before every method')
    wdf = WebdriverFactory(browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    lp.login("test@email.com", "abcabc")
    # if browser == "chrome":
    #     base_url = "https://courses.letskodeit.com/"
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(3)
    #     driver.get(base_url)
    #     print("Running test on Google Chrome")
    # else:
    #     base_url = "https://courses.letskodeit.com/"
    #     driver = webdriver.Firefox()
    #     driver.get(base_url)
    #     print("Running test on FireFox")
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print('conftest runs after every method')

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--os")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def os(request):
    return request.config.getoption("--os")