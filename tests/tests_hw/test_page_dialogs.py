from pages.modal_dialogs import ModalDialogsPage

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


def test_navigation_modal(browser):
    # Данный тест кейс проверяет навигацию по страницам, refresh, back, forward и set_windows_size
    modal_dialogs_page = ModalDialogsPage(browser)  # Создали объект страницы

    modal_dialogs_page.visit()  # Перешли на страницу demoqa.com/modal-dialogs
    modal_dialogs_page.refresh()  # Обновили страницу
    modal_dialogs_page.icon_home_page.click()  # Нажали на иконку, ведущую на главную страницу сайта demoqa.com

    # Проверяем, Title главной страницы сайта
    assert browser.title == 'DEMOQA'  # Сравниваем Title у browser с эталонным.

    modal_dialogs_page.back()  # Шаг назад стрелкой браузера. Можно просто browser.back()
    browser.set_window_size(width=900, height=400)  # Установили размеры экрана
    modal_dialogs_page.forward()  # Шаг вперёд стрелкой браузера. Можно просто browser.forward()

    # Проверяем, что URL не главной страницы (demoqa.com), т.к. мы вернулись назад на страницу demoqa.com/modal-dialogs
    assert not modal_dialogs_page.equal_url()

    browser.set_window_size(width=1000, height=1000)  # Возвращаем размеры экрана по-умолчанию
