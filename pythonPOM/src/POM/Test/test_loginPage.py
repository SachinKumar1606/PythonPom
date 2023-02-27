from src.POM.Pages.loginPage import LoginPage
from src.POM.Test.base_test import BaseTest


class TestLoginPage(BaseTest):

    def test_validLogin(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login("standard_user", "secret_sauce")
        self.loginPage.verifyUserIsLogin()
        