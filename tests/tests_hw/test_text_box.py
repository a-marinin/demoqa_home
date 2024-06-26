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
