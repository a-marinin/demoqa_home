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

        """ Локаторы для домашнего задания №12 """
        self.modal_windows = WebElement(driver, 'div.fade.modal.show > div > div')

        # Кнопки открытия модальных окон:
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        # Кнопки закрытия модальных окон:
        self.btn_close_small_modal = WebElement(driver, '#closeSmallModal')
        self.btn_close_large_modal = WebElement(driver, '#closeLargeModal')
        # Заголовки модальных окон:
        self.title_small_modal = WebElement(driver, '#example-modal-sizes-title-sm')
        self.title_large_modal = WebElement(driver, '#example-modal-sizes-title-lg')

