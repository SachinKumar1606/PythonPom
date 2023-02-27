import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_dragAndDrop():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    tittle = driver.title
    assert tittle == "DragnDrop"

    action = ActionChains(driver)
    dragAble = driver.find_element(By.XPATH, "//div/p[text()='Drag me to my target']")
    """""
    dropAble = driver.find_element(By.XPATH, "//div/p[text()='Drop here']")
    action.drag_and_drop(dragAble, dropAble).perform()
    action.click_and_hold(dragAble).pause(2).move_to_element(dropAble).perform()
    action.click_and_hold(dragAble).pause(2).move_to_element_with_offset(dropAble, 10, 20).perform()
    """
    action.drag_and_drop_by_offset(dragAble, 173, 19).perform()
    time.sleep(2)
    textVerify = driver.find_element(By.XPATH, "//div/p[text()='Dropped!']")
    assert textVerify
    dragSlider = driver.find_element(By.XPATH, "//input[@type='range']")
    action.drag_and_drop_by_offset(dragSlider, 10, 0).perform()
    time.sleep(2)
    driver.save_screenshot("C:\\BrowserDriver\\screenshots\\droptest.png")
    driver.quit()
