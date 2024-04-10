from locators import BurgerLocators
import time
from data import BurgerTestData
from faker import Faker
import settings
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(settings.URL)

    yield driver

    driver.quit()

fake = Faker()

class TestRegistration:
    def test_successful_registration(self, driver):

        button_account = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        button_account.click()

        button_register = driver.find_element(*BurgerLocators.BUTTON_REGISTRATE)
        button_register.click()

        driver.find_element(*BurgerLocators.INPUT_NAME).send_keys(*BurgerTestData.NAME)
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(fake.email())
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        button_final_register = driver.find_element(*BurgerLocators.BUTTON_FINAL_REGISTRATE)
        button_final_register.click()
        time.sleep(1)
        success_registration = driver.find_element(*BurgerLocators.TITLE_ENTER)
        assert success_registration.is_displayed() and success_registration.text == 'Вход'

    def test_wrong_password_registration(self, driver):
        button_account = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        button_account.click()

        button_register = driver.find_element(*BurgerLocators.BUTTON_REGISTRATE)
        button_register.click()

        driver.find_element(*BurgerLocators.INPUT_NAME).send_keys(*BurgerTestData.NAME)
        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(fake.email())
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.WRONG_PASSWORD)
        button_final_register = driver.find_element(*BurgerLocators.BUTTON_FINAL_REGISTRATE)
        button_final_register.click()
        time.sleep(1)
        wrong_password = driver.find_element(*BurgerLocators.WRONG_PASSWORD)
        assert wrong_password.is_displayed() and wrong_password.text == 'Некорректный пароль'

