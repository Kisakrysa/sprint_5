from tests.locators import BurgerLocators
from tests.data import BurgerTestData


class TestEnterAccountAsUser:
    def test_enter_account_as_user(self, driver):
        button_account_enter = driver.find_element(*BurgerLocators.BUTTON_ENTER_ACCOUNT)
        button_account_enter.click()

        driver.find_element(*BurgerLocators.INPUT_EMAIL).send_keys(*BurgerTestData.MAIL)
        driver.find_element(*BurgerLocators.INPUT_PASSWORD).send_keys(*BurgerTestData.PASSWORD)
        driver.find_element(*BurgerLocators.BUTTON_ENTER).click()

        personal_account_enter = driver.find_element(*BurgerLocators.BUTTON_ACCOUNT)
        personal_account_enter.click()

        title_profile = driver.find_element(*BurgerLocators.TITLE_PROFILE)
        assert title_profile.is_displayed() and title_profile.text == 'Профиль'