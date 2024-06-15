from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


"""
В файл components.py вынесены однотипные действия с веб-элементами.
Класс WebElement не наследуется!
Класс WebElement при инициализации получает 2 аттрибута:
    1. driver
    2. locator - по-умолчанию пустая строка
В классе WebElement реализованы следующие методы:
    1. Метод click - Универсальный метод, кликающий по различным веб-элементам (иконки, кнопки и прочее).
    2. Метод find_element - Универсальный метод, ищущий веб-элемент по заданному CSS-локатору.
    3. Метод exist - Метод, выполняющий проверку на то, найден ли веб-элемент на странице или нет:
        Если веб-элемент не найден - обрабатывается исключение "NoSuchElementException".
    4. Метод get-text - Метод для получения текста из веб-элемента.
"""


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
        # Клик по элементу.
        self.find_element().click()

    def find_element(self):
        # Найти элемент.
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def exist(self):
        # Проверка на то, существует ли элемент.
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):
        # Получение текста элемента.
        return self.find_element().text
