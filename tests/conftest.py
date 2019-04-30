import pytest
from base.webdriver_factory import DriverFactory
from base.base_page import BasePage
from pages.login.login_page import LoginPage
from pages.home.home_page import HomePage


@pytest.fixture(scope="class", autouse=True)
def set_up(request):
    df = DriverFactory("Chrome")
    driver = df.launch_browser()
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.bp = BasePage(driver)
        request.cls.lp = LoginPage(driver)
        request.cls.hp = HomePage(driver)
        yield driver
        driver.quit()