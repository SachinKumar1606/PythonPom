import pytest
from selenium import webdriver

from Config.conftest import TestData1


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(executable_path=TestData1.CHROME_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    web_driver.get(TestData1.BASE_URL)
    yield
    web_driver.close()
