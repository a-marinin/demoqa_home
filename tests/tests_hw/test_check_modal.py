import pytest
from pages.modal_dialogs import ModalDialogsPage
import time


# @pytest.mark.slow  # Пропускаем тест
def test_small_and_large_modal_dialogs(browser):
    modal_dialogs_page = ModalDialogsPage(browser)  # Создали объект страницы
    modal_dialogs_page.visit()  # Перешли на страницу demoqa.com/modal-dialogs

    assert modal_dialogs_page.btn_small_modal.exist()  # Проверяем, что кнопка "Small modal" присутствует
    assert modal_dialogs_page.btn_large_modal.exist()  # Проверяем, что кнопка "Large modal" присутствует
    assert not modal_dialogs_page.modal_windows.exist()  # Проверяем, что модального окна сейчас нет

    """ Проверяем маленькое модальное окно (Small modal) """
    modal_dialogs_page.btn_small_modal.click()  # Кликаем на кнопку "Small modal"
    time.sleep(2)
    assert modal_dialogs_page.modal_windows.exist()  # Проверяем, что модальное окно сейчас открыто
    assert modal_dialogs_page.title_small_modal.get_text() == 'Small Modal'  # Проверяем заголовок 'Small modal'
    assert modal_dialogs_page.btn_close_small_modal.exist()  # Проверяем, что есть кнопка "Close" Small modal
    modal_dialogs_page.btn_close_small_modal.click()  # Кликаем на кнопку "Close" у Small modal
    time.sleep(2)
    assert not modal_dialogs_page.modal_windows.exist()  # Проверяем, что модальное окно закрыто

    """ Проверяем большое модальное окно (Large modal) """
    modal_dialogs_page.btn_large_modal.click()  # Кликаем на кнопку "Large modal"
    time.sleep(2)
    assert modal_dialogs_page.modal_windows.exist()  # Проверяем, что модальное окно сейчас открыто
    assert modal_dialogs_page.title_large_modal.get_text() == 'Large Modal'  # Проверяем заголовок 'Large modal'
    assert modal_dialogs_page.btn_close_large_modal.exist()  # Проверяем, что есть кнопка "Close" Large modal
    modal_dialogs_page.btn_close_large_modal.click()  # Кликаем на кнопку "Close" у Large modal
    time.sleep(2)
    assert not modal_dialogs_page.modal_windows.exist()  # Проверяем, что модальное окно закрыто
