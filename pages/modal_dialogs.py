from pages.base_page import BasePage
from components.components import WebElement

''' Новый класс страницы для текст кейсов из домашнего задания №9. '''


class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # not_unique_btn - это элемент с не уникальным локатором, подходящим под все кнопки
        self.btn_not_unique = WebElement(driver, '.btn, btn-light ')  # 35 Элементов на странице
