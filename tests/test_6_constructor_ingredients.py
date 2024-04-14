from tests.locators import BurgerLocators


class TestConstructorSections:
    def test_fillings(self, driver):
        fillings = driver.find_element(*BurgerLocators.FILLING)
        fillings.click()

        filling_section = driver.find_element(*BurgerLocators.FILLING_SECTION)
        assert "current" in filling_section.get_attribute('class')


    def test_rolls_or_sauces(self, driver):
        sauces = driver.find_element(*BurgerLocators.SAUCES)
        sauces.click()
        rolls = driver.find_element(*BurgerLocators.ROLLS)
        rolls.click()

        rolls_section = driver.find_element(*BurgerLocators.ROLLS_SECTION)
        assert "current" in rolls_section.get_attribute('class')
