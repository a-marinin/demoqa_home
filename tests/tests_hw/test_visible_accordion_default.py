from pages.accordion import AccordionPage
import time

''' 2й тест-файл с текст кейсами из домашнего задания №8. '''


def test_visible_accordion_2nd_and_3dr_cards(browser):
    # Проверка видимости текста во 2-й и 3-й картах аккордеона.
    accordion_page = AccordionPage(browser)  # Создали объект страницы Accordion
    accordion_page.visit()  # Переход на страницу demoqa.com/accordian

    # Проверки на то, что 2-й, 3-й и 4-й тексты скрыты по-умолчанию.
    assert not accordion_page.text_where_does_it_come_from_1.visible()  # Текст №2 (по-умолчанию).
    assert not accordion_page.text_where_does_it_come_from_2.visible()  # Текст №3 (по-умолчанию).
    assert not accordion_page.text_why_do_we_use_it.visible()  # Текст №4 (по-умолчанию).

    # Проверки на то, что 2-й и 3-й тексты становятся видны, когда мы раскрываем 2-ю карту.
    accordion_page.card_where_does_it_come_from.click()  # Кликаем по карте №2 - она разворачивается.
    time.sleep(2)  # Ждём 2 секунды
    assert accordion_page.text_where_does_it_come_from_1.visible()  # 2-й текст стал видимым после клика по 2-й карте.
    assert accordion_page.text_where_does_it_come_from_2.visible()  # 3-й текст стал видимым после клика по 2-й карте.

    # Проверка на то, что 4-й текст становится видим, когда мы раскрываем 3-ю карту.
    accordion_page.card_why_do_we_use_it.click()  # Кликаем по карте №3 - она раскрывается.
    time.sleep(2)  # Ждём 2 секунды
    assert accordion_page.text_why_do_we_use_it.visible()  # 4-й текст становится видимым после клика по 3-й карте.
