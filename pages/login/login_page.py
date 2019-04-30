from base.base_page import BasePage


class LoginPage(BasePage):

    _login_link = "//div[text()='Login' and @class='mTxt']"
    _email_id_textbox = "eLoginNew"
    _password_textbox = "pLogin"
    _login_btn = "//button[@type='submit' and @class='blueBtn' and @value='Login']"
    _my_naukri_link = "//div[text()='My Naukri' and @class='mTxt']"
    _edit_profile_link = "//a[text()='Edit Profile']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_link(self):
        self.click_element(self._login_link, "xpath")

    def enter_email_id(self, email_id):
        self.send_data(email_id, self._email_id_textbox)

    def enter_password(self, password):
        self.send_data(password, self._password_textbox)

    def click_login_btn(self):
        self.click_element(self._login_btn, "xpath")

    def login_to_naukri(self, email_id="", password=""):
        self.click_login_link()
        self.enter_email_id(email_id)
        self.enter_password(password)
        self.click_login_btn()

    def verify_login(self, title_to_verify):
        return self.verify_page_title(title_to_verify)









