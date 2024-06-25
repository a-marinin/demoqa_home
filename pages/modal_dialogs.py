from pages.base_page import BasePage
from components.components import WebElement

''' Новый класс страницы для текст кейсов из домашнего задания №9. '''


class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        # not_unique_btn - это элементы субменю "Alerts, Frame and Windows"
        self.btns_submenu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > .btn, btn-light ')

        # not_unique_btn - это элемент с не уникальным локатором, подходящим под все кнопки
        self.btn_not_unique = WebElement(driver, '.btn, btn-light ')  # 35 Элементов на странице

        # icon_home_page - это элемент иконки, ведущий на главную страницу сайта demoqa.com
        self.icon_home_page = WebElement(driver, '#app > header > a')
