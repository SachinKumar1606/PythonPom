import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def test_dropdown():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.get("https://qavbox.github.io/demo/signup/")
    tittle = driver.title
    assert tittle == "Registration Form"
    action = ActionChains(driver)

    """
    element = driver.find_element(By.XPATH, "//input[@type='button']")
    action.click(element).perform()
    time.sleep(3)
    tittle = driver.title
    assert tittle == "QAVBOX Demo"
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")
    rightClickEle = driver.find_element(By.XPATH, "//span[text()='right click me']")
    action.context_click(rightClickEle).send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ARROW_DOWN).pause(2)\
        .send_keys(Keys.ARROW_DOWN).pause(2).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    textAlert = driver.switch_to.alert.text
    print("textAlert - " + textAlert)
    assert "clicked: copy" in textAlert
    driver.switch_to.alert.accept()
    
    element = driver.find_element(By.XPATH, "//input[@type='button']")
    action.context_click(element).send_keys(Keys.ENTER).perform()
    """

    userName = driver.find_element(By.XPATH, "//input[@name='uname']")
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    action.move_to_element(userName).click().send_keys("Sachin").perform()
    action.key_down(Keys.CONTROL).key_down("A").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    action.key_down(Keys.CONTROL).key_down("C").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    action.click(email).key_down(Keys.CONTROL).key_down("V").key_up(Keys.CONTROL).perform()
    time.sleep(3)
    driver.close()
