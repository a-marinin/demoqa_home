# from pages.demoqa import DemoQa
# from pages.elements_page import ElementsPage
from pages.accordion import AccordionPage

# Тест-файл домашнего задания №8.


def test_visible_accordion(browser):
    # Проверка видимости элемента "What is Lorem Ipsum?" на странице demoqa.com/accordian
    accordion_page = AccordionPage(browser)  # Создали объект страницы Accordion
    accordion_page.visit()  # Переход на страницу demoqa.com/accordian

    assert accordion_page.text_what_is_lorem_ipsum.visible()  # Проверка элемента на видимость.
