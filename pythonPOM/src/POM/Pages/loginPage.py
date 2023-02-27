from selenium.webdriver.common.by import By

from src.POM.Pages.basePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        self.driver = driver

    userNameInput = By.XPATH, "//input[@data-test='username']"
    passwordInput = By.XPATH, "//input[@data-test='password']"
    loginButton = By.XPATH, "//input[@data-test='login-button']"
    dashboadProduct = By.XPATH, "//div/span[text()='Products']"

    def login(self, username, password):
        self.do_send_keys(self.userNameInput, username)
        self.do_send_keys(self.passwordInput, password)
        self.do_click(self.loginButton)

    def verifyUserIsLogin(self):
        visible = self.is_visible(self.dashboadProduct)
        assert visible
