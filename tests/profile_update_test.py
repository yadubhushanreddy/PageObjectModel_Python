import time


class TestLogin:

    def test_profile_update(self):
        self.bp.close_unwanted_browsers()
        self.lp.login_to_naukri("yallatipalli@gmail.com", "Bharathi@30")
        assert self.lp.verify_page_title("Home | Mynaukri")
        self.hp.navigate_to_profile()
        self.hp.edit_skills_and_save()
        self.hp.click_logout_link()
        time.sleep(5)
