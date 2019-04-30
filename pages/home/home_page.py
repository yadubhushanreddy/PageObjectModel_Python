from base.base_page import BasePage


class HomePage(BasePage):

    _my_naukri_link = "//div[text()='My Naukri' and @class='mTxt']"
    _edit_profile_link = "//a[text()='Edit Profile']"
    _edit_link_key_skills = "div.keySkills span.edit.icon"
    _save_skills_btn = "button#saveKeySkills"
    _save_success_msg = "//p[contains(text(),'successfully saved')]"
    _logout_link = "a[title='Logout']"

    def mouse_hover_mynaukri(self):
        self.mouse_hover(self._my_naukri_link, "xpath")

    def click_edit_profile(self):
        self.click_element(self._edit_profile_link, "xpath")

    def click_edit_key_skills(self):
        self.wait_for_element(self._edit_link_key_skills, "css")
        self.click_element(self._edit_link_key_skills, "css")

    def click_skills_save_btn(self):
        self.wait_for_element(self._save_skills_btn, "css")
        self.click_element(self._save_skills_btn, "css")

    def check_success_msg(self):
        self.wait_for_element(self._save_success_msg, "xpath")
        self.element_display(self._save_success_msg, "xpath")

    def navigate_to_profile(self):
        self.mouse_hover_mynaukri()
        self.wait_for_element(self._edit_profile_link, "xpath")
        self.click_edit_profile()

    def edit_skills_and_save(self):
        self.click_edit_key_skills()
        self.click_skills_save_btn()
        self.check_success_msg()

    def click_logout_link(self):
        self.mouse_hover_mynaukri()
        self.wait_for_element(self._logout_link, "css")
        self.click_element(self._logout_link, "css")




