from pages.modal_dialogs import ModalDialogsPage
import time

''' Тест-файл с текст кейсами из домашнего задания №9. '''


def test_modal_elements(browser):
    # Данный тест кейс проверяет, что на странице demoqa.com/modal-dialogs 5 кнопок подменю.
    # Также данный тест кейс проверяет, что на странице 35 элементов с не уникальным локатором.
    modal_dialogs_page = ModalDialogsPage(browser)  # Создали объект страницы
    modal_dialogs_page.visit()  # Перешли на страницу demoqa.com/modal-dialogs

    # Проверяем, что на странице 5 элементов субменю "Alerts, Frame and Windows"
    assert modal_dialogs_page.btns_submenu.check_count_elements(count=5)

    # Проверяем, что на странице 35 элементов с этим локатором
    assert modal_dialogs_page.btn_not_unique.check_count_elements(count=35)

# def test_navigation_modal(browser):
#     # Данный