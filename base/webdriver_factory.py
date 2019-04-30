from selenium import webdriver


class DriverFactory():

    def __init__(self, browser_name):
        self.browser_name = browser_name

    def launch_browser(self):
        base_url = "https://www.naukri.com/"
        self.browser_name = self.browser_name.lower()
        if self.browser_name == "chrome":
            driver = webdriver.Chrome()
        elif self.browser_name == "firefox":
            driver = webdriver.Firefox()
        elif self.browser_name == "safari":
            driver = webdriver.Safari()
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get(base_url)
        return driver

