from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Basics.fixtureDemo.base_test import BaseTest


class Test_SauceDemo(BaseTest):

    def test_SauceDemoLogin(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div/span[text()='Products']")))
        isLogin = driver.find_element(By.XPATH, "//div/span[text()='Products']")
        assert isLogin

    def test_SauceDemoLogout(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div/span[text()='Products']")))
        isLogin = driver.find_element(By.XPATH, "//div/span[text()='Products']")
        assert isLogin
        driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
        driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        loginBtn = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        assert loginBtn

    def test_SauceDemoItemCount(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div/span[text()='Products']")))
        isLogin = driver.find_element(By.XPATH, "//div/span[text()='Products']")
        assert isLogin
        elementList = driver.find_elements(By.XPATH, "//div/a/img")
        assert 6 in len(elementList).as_integer_ratio()
        driver.find_element(By.XPATH, "//button[text()='Open Menu']").click()
        driver.find_element(By.XPATH, "//a[text()='Logout']").click()
        loginBtn = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
        assert loginBtn
