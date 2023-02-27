from Config.conftest import TestData1
from Pages.LoginPage import LoginPage
from Tests.base_test import BaseTest


class Test_Login(BaseTest):
    def test_verify_signup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_tittle(self):
        self.loginPage = LoginPage(self.driver)
        tittle = self.loginPage.get_login_page_tittle(TestData1.LOGIN_PAGE_TITTLE)
        assert tittle == TestData1.LOGIN_PAGE_TITTLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData1.USER_NAME, TestData1.PASSWORD)


