from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def test_dropdown():
    driver = webdriver.Chrome("C:\\BrowserDriver\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(60)
    driver.get("https://qavbox.github.io/demo/signup/")
    tittle = driver.title
    assert tittle == "Registration Form"
    select = Select(driver.find_element(By.NAME, "sgender"))
    """
    # select.select_by_visible_text("Male")
    # print(select.first_selected_option.text)
    # assert "Male" in select.first_selected_option.text
    # select.select_by_value("female")
    # print(select.first_selected_option.text)
    # assert "Female" in select.first_selected_option.text
    """
    select.select_by_index(3)  # index start from 0
    listOption = select.options
    for option in listOption:
        print(option.text + "\n")
    print(select.first_selected_option.text)
    assert "Not Applicable" in select.first_selected_option.text
    driver.close()
