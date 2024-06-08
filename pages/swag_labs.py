from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class SwagLabs(BasePage):

    def exist_icon(self):  # Проверяем наличия лого сайта
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    # def click_on_the_icon(self):
    #     self.find_element(locator='div.login_logo').click()

    def username_field(self):  # Проверяем наличие поля ввода имени
        try:
            self.find_element(locator='#user-name')
        except NoSuchElementException:
            return False
        return True

    def password_field(self):  # Проверяем наличие поля ввода пароля
        try:
            self.find_element(locator='#password')
        except NoSuchElementException:
            return False
        return True
