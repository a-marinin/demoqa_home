import time
import random
from pages.webtables import WebTablesPage

"""
Проверки того, на какой странице мы находимся реализованы через:
    1. Через значение атрибута 'value', элемента 'field_jump_to_page' (Основная проверка).
    2. Через наличие/отсутствие кнопок 'Edit' и 'Delete' для 1-й и 6-й записей (Дополнительные проверки):
        2.1. Как определяем, что мы на 1-й странице (когда выбрано отображение 5-ти записей на странице):
            - Если кнопки 'Edit/Delete' для 1-й записи существуют -> мы на 1-й странице
            - Если кнопки 'Edit/Delete' для 6-й записи отсутствуют -> мы на 1-й странице
        2.2. Как определяем, что мы на 2-й странице (когда выбрано отображение 5-ти записей на странице):
            - Если кнопки 'Edit/Delete' для 1-й записи отсутствуют -> мы на 2-й странице
            - Если кнопки 'Edit/Delete' для 6-й записи существуют -> мы на 2-й странице        
"""


def test_advanced_webtables_page_navigation(browser):
    web_tables = WebTablesPage(browser)
    web_tables.visit()  # Посещаем страницу

    """ Предусловия """
    # Проверяем, что на странице отображается 10 записей (значение по умолчанию)
    assert web_tables.qty_current_rows_on_the_page.check_count_elements(count=10)
    web_tables.option_dropdown_page_size.click()  # Кликаем на выпадающее меню
    time.sleep(2)
    web_tables.option_page_size_show_5_elements.click()  # Выбираем "отображать 5 элементов на странице"
    # Проверяем, что на странице теперь отображается 5 записей
    assert web_tables.qty_current_rows_on_the_page.check_count_elements(count=5)
    time.sleep(2)

    """ Проверка заблокированных кнопок 'Next' и 'Previous' """
    assert web_tables.btn_next_page.get_dom_attribute('disabled')  # Кнопка 'Next' заблокирована
    assert web_tables.btn_previous_page.get_dom_attribute('disabled')  # Кнопка 'Previous' заблокирована

    web_tables.btn_next_page.click()  # Кликаем на кнопку 'Next'
    assert web_tables.field_jump_to_page.get_dom_attribute('value') == '1'  # Проверка, что находимся на 1-й странице
    assert not web_tables.btn_edit_6th_record.exist()  # Проверяем, что ничего не произошло(находимся на 1-й странице)
    assert not web_tables.btn_delete_6th_record.exist()  # Проверяем, что ничего не произошло(находимся на 1-й странице)

    web_tables.btn_previous_page.click()  # Кликаем на кнопку 'Previous'
    assert web_tables.field_jump_to_page.get_dom_attribute('value') == '1'  # Проверка, что находимся на 1-й странице
    assert web_tables.btn_edit_1st_record.exist()  # Проверяем, что ничего не произошло(находимся на 1-й странице)
    assert web_tables.btn_delete_1st_record.exist()  # Проверяем, что ничего не произошло(находимся на 1-й странице)

    """ Проверка добавления 3-х записей в таблицу """
    assert web_tables.total_pages_qty.get_text() == '1'  # Проверяем количество доступных страниц
    for row in range(3):
        web_tables.btn_add_new_record.click()  # Кликаем на кнопку "Add"
        web_tables.first_name.send_keys('Иван')  # Заполняем поле "имя"
        web_tables.last_name.send_keys('Иванов')  # Заполняем поле "фамилия"
        web_tables.email.send_keys('test@test.com')  # Заполняем поле "email"
        web_tables.age.send_keys('{}'.format(random.randrange(18, 100, 2)))  # Генерируем случайный возраст
        web_tables.salary.send_keys('{}'.format(random.randrange(500, 10000, 2)))  # Генерируем случайную зарплату
        web_tables.departament.send_keys('QA Automation')  # Заполняем поле "департамент"
        assert web_tables.dialog_box_registration_form.exist()  # Проверяем, что диалоговое окно открыто
        web_tables.btn_submit.click()  # Кликаем на кнопку "submit"
        time.sleep(2)
        assert not web_tables.dialog_box_registration_form.exist()  # Проверяем, что диалоговое окно закрыто
    assert web_tables.total_pages_qty.get_text() == '2'  # Проверяем количество доступных страниц
    time.sleep(2)

    """ Проверка перехода на 2-ю страницу """
    assert not web_tables.btn_next_page.get_dom_attribute('disabled')  # Проверяем, что кнопка 'Next' стала активна
    web_tables.btn_next_page.click()  # Кликаем на кнопку 'Next'
    assert web_tables.field_jump_to_page.get_dom_attribute('value') == '2'  # Проверка, что находимся на 2-й странице

    assert not web_tables.btn_edit_1st_record.exist()  # Дополнительная проверка на то, что находимся на 2-й странице
    assert not web_tables.btn_delete_1st_record.exist()  # Дополнительная проверка на то, что находимся на 2-й странице
    assert web_tables.btn_edit_6th_record.exist()  # Дополнительная проверка на то, что находимся на 2-й странице
    assert web_tables.btn_delete_6th_record.exist()  # Дополнительная проверка на то, что находимся на 2-й странице

    """ Проверка перехода на 1-ю страницу """
    assert not web_tables.btn_previous_page.get_dom_attribute('disabled')  # Проверяем, что кнопка 'Previous' активна
    web_tables.btn_previous_page.click()  # Кликаем на кнопку 'Previous'
    assert web_tables.field_jump_to_page.get_dom_attribute('value') == '1'  # Проверка, что находимся на 1-й странице

    assert web_tables.btn_edit_1st_record.exist()  # Дополнительная проверка на то, что находимся на 1-й странице
    assert web_tables.btn_delete_1st_record.exist()  # Дополнительная проверка на то, что находимся на 1-й странице
    assert not web_tables.btn_edit_6th_record.exist()  # Дополнительная проверка на то, что находимся на 1-й странице
    assert not web_tables.btn_delete_6th_record.exist()  # Дополнительная проверка на то, что находимся на 1-й странице
