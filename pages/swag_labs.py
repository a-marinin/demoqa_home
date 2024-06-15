from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

"""
В файле swag_labs.py создан класс SwagLabs.
Это файл из домашнего задания №6. В домашнем задании №7 мы его большне не исользуем.
Возможно, в будущем, нужно будет удалить его из проекта. Но пока что оставлю его.
"""


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
