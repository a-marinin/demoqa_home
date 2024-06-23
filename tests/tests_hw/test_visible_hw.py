from pages.accordion import AccordionPage
import time

''' 1й тест-файл с текст кейсами из домашнего задания №8. '''


def test_visible_accordion(browser):
    # Проверка видимости элемента "What is Lorem Ipsum?" на странице demoqa.com/accordian
    accordion_page = AccordionPage(browser)  # Создали объект страницы Accordion
    accordion_page.visit()  # Переход на страницу demoqa.com/accordian
    assert accordion_page.text_what_is_lorem_ipsum.visible()  # Проверка на то, что элемент виден.


def test_not_visible_accordion(browser):
    # Проверка, что элемент "What is Lorem Ipsum?" на странице demoqa.com/accordian НЕ виден (после клика).
    accordion_page = AccordionPage(browser)  # Создали объект страницы Accordion
    accordion_page.visit()  # Переход на страницу demoqa.com/accordian
    accordion_page.card_what_is_lorem_ipsum.click()  # Кликаем по карте - она сворачивается.
    time.sleep(2)  # Ждём 2 секунды
    assert not accordion_page.text_what_is_lorem_ipsum.visible()  # Проверка на то, что элемент НЕ виден.
