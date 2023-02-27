from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_seleniumWaits():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    wait = WebDriverWait(driver, 20)
    driver.get("https://qavbox.github.io/demo/delay/")
    assert "Delay elements" in driver.title
    el1 = driver.find_element(By.XPATH, "//input[@value='Click me!']")
    el1.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='I am here!']")))
    el1Text = driver.find_element(By.XPATH, "//h2[@id='two']")
    print(el1Text.text)

    el2 = driver.find_element(By.XPATH, "//input[@value='Try me!']")
    el2.click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='I appeared after 5 sec']")))
    el2Text = driver.find_element(By.XPATH, "//h2[@id='delay']")
    print(el2Text.text)

    el3 = driver.find_element(By.XPATH, "//input[@value='Start']")
    el3.click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//div/b[text()='Loading...']")))
    el3Text = driver.find_element(By.XPATH, "//h2[@id='loaderdelay']")
    print(el3Text.text)
    driver.close()
