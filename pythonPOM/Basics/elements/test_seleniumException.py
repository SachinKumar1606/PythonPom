import traceback

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_seleniumException():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    wait = WebDriverWait(driver, 20)
    driver.get("https://qavbox.github.io/demo/signup/")
    tittle = driver.title
    assert tittle == "Registration Form"

    try:
        el1 = driver.find_element(By.ID, "lblname1")
        assert "Full Name" in el1.text
    except NoSuchElementException:
        print(traceback.format_exc())

    el1Input = driver.find_element(By.NAME, "uname")
    el1Input.send_keys("Name")
    # assert "Name" in el1Input.text
    driver.close()
