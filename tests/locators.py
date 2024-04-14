from selenium.webdriver.common.by import By

class BurgerLocators:
    BUTTON_ACCOUNT = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/account']")
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
    BUTTON_SMALL_ENTER = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']")
    BUTTON_RESET_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']")
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
    BUTTON_REGISTRATE = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/register']")
    BUTTON_FINAL_REGISTRATE = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    BUTTON_CONSTRUCTOR = (By.XPATH, "//a[@class='AppHeader_header__link__3D_hX' and @href='/']")
    BUTTON_EXIT = (By.XPATH, "//button[@type='button' and @class='Account_button__14Yp3 text text_type_main-medium text_color_inactive' and text()='Выход']")

    INPUT_NAME = (By.XPATH, "//label[text() = 'Имя']/../input")
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/../input") #"//label[text() = 'Имя']/following-sibling::input"
    INPUT_PASSWORD = (By.XPATH, "//label[text() = 'Пароль']/../input")

    TITLE_ENTER = (By.XPATH, "//h2[text()='Вход']")
    TITLE_PROFILE = (By.XPATH, "//a[text()='Профиль']")
    TITLE_COLLECT_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")

    WRONG_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")
    FORM_AN_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

    FILLING = (By.XPATH, ".//span[text()='Начинки']")
    FILLING_SECTION = (By.XPATH, ".//span[text()='Начинки']/parent::div")

    ROLLS = (By.XPATH, ".//span[text()='Булки']")
    ROLLS_SECTION = (By.XPATH, ".//span[text()='Булки']/parent::div")

    SAUCES = (By.XPATH, ".//span[text()='Соусы']")
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']/parent::div")