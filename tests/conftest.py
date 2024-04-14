import pytest
from selenium import webdriver
import settings

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(settings.URL)

    yield driver

    driver.quit()