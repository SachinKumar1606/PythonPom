from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webTable():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.get("https://qavbox.github.io/demo/signup/")
    tittle = driver.title
    assert "Registration Form" in tittle

    print("Tittle - " + driver.execute_script("return document.title;"))

    print("URL - " + driver.execute_script("return document.URL;"))
    driver.close()
