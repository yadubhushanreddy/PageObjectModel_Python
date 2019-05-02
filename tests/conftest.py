import pytest
from base.webdriver_factory import DriverFactory
from base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage


@pytest.fixture(scope="class", autouse=True)
def set_up(request, username, password):
    df = DriverFactory("Chrome")
    driver = df.launch_browser()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.bp = BasePage(driver)
        request.cls.lp = LoginPage(driver)
        request.cls.hp = HomePage(driver)
        request.cls.username = username
        request.cls.password = password
        yield driver
        driver.quit()


def pytest_addoption(parser):
    parser.addoption("--username")
    parser.addoption("--password")


@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="session")
def password(request):
    return request.config.getoption("--password")