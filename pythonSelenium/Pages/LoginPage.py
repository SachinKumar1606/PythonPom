from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SIGNIN_BUTTON = (By.XPATH, "//button/*[text()='Log in']")
    SIGNUP_LINK = (By.XPATH, "//a/*[contains(text(),'Sign up')]")

    def __init__(self, driver):
        self.driver = driver

    def get_login_page_tittle(self, tittle):
        return self.get_tittle(tittle)

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        print(self.driver.title)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SIGNIN_BUTTON)
