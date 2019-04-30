from base.reusables import Reusable


class BasePage(Reusable):

    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self, expected_title):
        self.wait_for_title(expected_title)
        if self.get_title() == expected_title:
            print("Matching page title: Expected = {0}, Actual = {1}"
                  .format(expected_title, self.get_title()))
            return True
        else:
            return False

    def close_unwanted_browsers(self):

        parent_window_handle = self.driver.current_window_handle
        all_windows_handles = self.driver.window_handles
        for handle in all_windows_handles:
            if handle != parent_window_handle:
                self.driver.switch_to.window(handle)
                self.driver.close()
                print("Closing unwanted browser with handle {0}".format(handle))
        self.driver.switch_to.window(parent_window_handle)
