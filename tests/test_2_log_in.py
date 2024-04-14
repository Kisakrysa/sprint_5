from tests import settings
from tests.locators import BurgerLocators
from tests.data import BurgerTestData



class TestSuccessfulLogIn:
    def test_successful_log_in_account_button(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

    def test_successful_log_in_personal_account(self, driver):
        personal_account_enter = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        personal_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

    def test_successful_log_in_registration_form(self, driver):
        driver.get(settings.URL + "login")
        button_register = driver.find_element(*BurgerLocators.BUTTON_REGISTRATE)
        button_register.click()

        small_enter = driver.find_element(*BurgerLocators.BUTTON_SMALL_ENTER)
        small_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'

    def test_successful_log_in_reset_password(self, driver):
        driver.get(settings.URL + "login")
        button_reset_password = driver.find_element(*BurgerLocators.BUTTON_RESET_PASSWORD)
        button_reset_password.click()

        small_enter = driver.find_element(*BurgerLocators.BUTTON_SMALL_ENTER)
        small_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        form_an_order = driver.find_element(*BurgerLocators.FORM_AN_ORDER)
        assert form_an_order.is_displayed() and form_an_order.text == 'Оформить заказ'