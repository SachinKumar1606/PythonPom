from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webTable():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.get("https://qavbox.github.io/demo/webtable/")
    tittle = driver.title
    assert tittle == "webtable"
    table = driver.find_element(By.XPATH, "//table[@id='table01']")
    headers = table.find_elements(By.TAG_NAME, "th")
    body = table.find_element(By.TAG_NAME, "tbody")
    cells = body.find_elements(By.TAG_NAME, "td")
    for header in headers:
        print(header.text + "\n")
        body1 = table.find_element(By.XPATH, "tbody")
        cells1 = body1.find_elements(By.TAG_NAME, "td")
        for cell1 in cells1:
            print(cell1.text)
    print("____________________________________------------------"
          "------------------____________________________________")
    for cell in cells:
        print(cell.text)
    driver.quit()
