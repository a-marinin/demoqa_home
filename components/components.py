from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from selenium import webdriver  # TEMP!!!

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
    def __init__(self, driver, locator='', locator_type="css"):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):
        # Клик по элементу.
        self.find_element().click()

    def click_force(self):
        # Принудительный клик по элементу.
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):
        # Найти один конкретный элемент по уникальному локатору.
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)
        #return self.driver.find_element(self.get_by_type(), self.locator)  # не работает

    def find_elements(self):
        # Найти несколько элементов по не уникальному локатору.
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)
        #return self.driver.find_elements(self.get_by_type(), self.locator)  # не работает

    # """ Тестовый метод для ДЗ №10 """
    # def find_element_by_text(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.locator)

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

    def visible(self):
        return self.find_element().is_displayed()

    ''' Тестовый метод для ДЗ № 10 '''
    def visible_by_text(self):
        return self.find_element_by_text().is_displayed()

    def check_count_elements(self, count: int) -> bool:
        if len(self.find_elements()) == count:
            return True
        return False

    def send_keys(self, text: str):
        # Передать в поле сочетание клавиш
        self.find_element().send_keys(text)

    def clear(self):
        # Очистить поле
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):
        # Найти аттрибут HTML элемента
        value = self.find_element().get_dom_attribute(name)  # Найти элемент, затем найти его аттрибут

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True

    def scroll_to_element(self):
        # Прокрутка страницы до любого элемента
        self.driver.execute_script(
            "windows.scrollTo(0, document.body.scrollHeight);",
            self.find_element().get_attibute('outerHTML')
        )

    def get_by_type(self):
        # Мульти-поиск (можем передавать любой тип локатора)
        if self.locator_type == "id":
            return By.ID
        elif self.locator_type == "name":
            return By.NAME
        elif self.locator_type == "xpath":
            return By.XPATH
        elif self.locator_type == "ccs":
            return By.CSS_SELECTOR
        elif self.locator_type == "class":
            return By.CLASS_NAME
        elif self.locator_type == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + self.locator_type + " not correct.")
        return False  # Если ни одно из перечисленных выше условий не пройдёт

    # def get_attribute(self):
    #     """ 1й тестовый метод для дополнительного задания к ДЗ № 10 """
    #     self.find_element().get_attribute('innerHTML')
    #
    # def get_attribute2(self):
    #     """ 2й тестовый метод для дополнительного задания к ДЗ № 10 """
    #     self.find_element().get_attribute('outerHTML')
    #
    # def get_html_code(self):
    #     """ 3й тестовый метод для дополнительного задания к ДЗ № 10 """
    #     self.driver.page_source()
