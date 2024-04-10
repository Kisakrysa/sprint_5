from locators import BurgerLocators
from data import BurgerTestData
import settings
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(settings.URL)

    yield driver

    driver.quit()


class TestJumpFromAccountToConstructor:
    def test_jump_from_acc_to_constructor(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        personal_account_enter = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        personal_account_enter.click()

        button_constructor = driver.find_element(*BurgerLocators.BUTTON_CONSTRUCTOR)
        button_constructor.click()

        title_collect_burger = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed() and title_collect_burger.text == 'Соберите бургер'

    def test_jump_from_acc_to_constructor_by_logo(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        personal_account_enter = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        personal_account_enter.click()

        logo = driver.find_element(*BurgerLocators.LOGO)
        logo.click()

        title_collect_burger = driver.find_element(*BurgerLocators.TITLE_COLLECT_BURGER)
        assert title_collect_burger.is_displayed() and title_collect_burger.text == 'Соберите бургер'