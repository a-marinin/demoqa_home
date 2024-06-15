from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):

    def exist_icon(self):  # Проверяем наличия лого сайта
        try:
            self.find_element(locator='div.login_logo')  # Не работает после изменения кода, старая реализация.
        except NoSuchElementException:
            return False
        return True

    def username_field(self):  # Проверяем наличие поля ввода имени
        try:
            self.find_element(locator='#user-name')  # Не работает после изменения кода, старая реализация.
        except NoSuchElementException:
            return False
        return True

    def password_field(self):  # Проверяем наличие поля ввода пароля
        try:
            self.find_element(locator='#password')  # Не работает после изменения кода, старая реализация.
        except NoSuchElementException:
            return False
        return True
