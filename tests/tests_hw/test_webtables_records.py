import time
import random
from pages.webtables import WebTablesPage


def test_crud_actions_with_webtables(browser):
    web_tables = WebTablesPage(browser)
    web_tables.visit()

    assert web_tables.btn_add_new_record.exist()  # Проверяем, что кнопка "Add" есть на странице
    web_tables.btn_add_new_record.click()  # Кликаем на кнопку "Add"
    assert web_tables.dialog_box_registration_form.exist()  # Проверяем, что диалоговое окно открылось

    """ Проверка на то, что в диалоге нельзя сохранить пустую форму """
    assert not web_tables.user_form.get_dom_attribute('class') == 'was-validated'  # Класс валидации у формы отсутствует
    web_tables.btn_submit.click()  # Кликаем на кнопку "Submit", чтобы отправить пустую форму
    assert web_tables.user_form.get_dom_attribute('class') == 'was-validated'  # # Класс валидации у формы присутствует
    browser.refresh()  # Обновляем страницу (чтобы сбросить форму)

    """ Проверка на добавление новой записи в таблицу """
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

    """ Проверяем, что в таблицу была добавлена новая запись с введёнными данными """
    assert web_tables.added_4th_first_name.get_text() == 'Иван'  # Проверяем поле "имя" у добавленной записи
    assert web_tables.added_4th_last_name.get_text() == 'Иванов'  # Проверяем поле "фамилия" у добавленной записи
    assert web_tables.added_4th_email.get_text() == 'test@test.com'  # Проверяем поле "email" у добавленной записи
    assert web_tables.added_4th_departament.get_text() == 'QA Automation'    # Проверяем поле "департамент"
    time.sleep(2)

    """ Проверяем изменение 4й добавленной нами записи в таблице """
    web_tables.btn_edit_4th_record.click()  # Кликаем на кнопку изменения 4-й записи
    assert web_tables.dialog_box_registration_form.exist()  # Проверяем, что диалоговое окно открылось
    # Проверяем, что в диалоговом окне находятся введённые нами данные
    assert web_tables.first_name.get_dom_attribute('value') == 'Иван'  # Проверяем поле "имя"
    assert web_tables.last_name.get_dom_attribute('value') == 'Иванов'  # Проверяем поле "фамилия"
    assert web_tables.email.get_dom_attribute('value') == 'test@test.com'  # Проверяем поле "email"
    assert web_tables.departament.get_dom_attribute('value') == 'QA Automation'    # Проверяем поле "департамент"

    # Изменяем поле "имя" и сохраняем изменения
    time.sleep(4)
    web_tables.first_name.clear()  # Удаляем ранее введённые данные (Выполняем CTRL + a -> DELETE)
    time.sleep(4)
    assert web_tables.first_name.get_text() == ''  # Проверяем, что данные были удалены
    time.sleep(2)
    web_tables.first_name.send_keys('Пётр')  # Заполняем поле "имя" новыми данными
    time.sleep(2)
    web_tables.btn_submit.click()  # Кликаем на кнопку "Submit"
    assert web_tables.added_4th_first_name.get_text() == 'Пётр'  # Проверяем, что данные были изменены
    time.sleep(2)

    """ Проверяем удаление 4й добавленной нами записи в таблице """
    web_tables.btn_delete_4th_record.click()  # Удаляем 4-й элемент из таблицы
    time.sleep(2)
    assert not web_tables.added_4th_first_name.get_text() == 'Иван'  # Проверяем по полю "имя", что запись удалена
    assert not web_tables.added_4th_last_name.get_text() == 'Иванов'  # Проверяем по полю "фамилия", что запись удалена
    assert not web_tables.added_4th_email.get_text() == 'test@test.com'  # Проверяем по полю "email", что запись удалена
    assert not web_tables.added_4th_departament.get_text() == 'QA Automation'    # Проверяем по полю "департамент"

    time.sleep(5)
