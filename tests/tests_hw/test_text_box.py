from pages.text_box import TextBox
import time

''' 1й тест-файл с текст кейсами из домашнего задания №10. '''


def test_text_box(browser):
    text_box_page = TextBox(browser)

    text_box_page.visit()
    time.sleep(2)
    text_box_page.input_name.send_keys('Саша')
    text_box_page.input_current_address.send_keys('Санкт-Петербург')
    text_box_page.btn_submit.click()

    time.sleep(2)

    assert text_box_page.output_name.get_text() == 'Name:Саша'  # Проверка имени в поле вывода
    assert text_box_page.output_current_address.get_text() == 'Current Address :Санкт-Петербург'  # Проверка адреса в поле вывода


def test_text_box_with_variables(browser):
    user_name = 'Александр'
    current_address = 'Ленинград'

    text_box_page = TextBox(browser)

    text_box_page.visit()
    time.sleep(2)
    # Ввод текста через переменные.
    text_box_page.input_name.send_keys(user_name)
    text_box_page.input_current_address.send_keys(current_address)

    text_box_page.btn_submit.click()

    time.sleep(2)

    # Сравнение текста через переменные.
    # Также добавить метод .replace(), чтобы удалить лишний текст, генерируемый на сайте при выводе результата.
    assert text_box_page.output_name.get_text().replace('Name:', '') == user_name
    assert text_box_page.output_current_address.get_text().replace('Current Address :', '') == current_address
