# from pages.swag_labs import SwagLabs
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time

# TODO Селектор футера (сайта demoqa) - #app > footer > span
# TODO 1й Селетор кнопки "Elements" (сайта demoqa) - #app > div > div > div.home-body > div > div:nth-child(1) > div > div.avatar.mx-auto.white > svg
# TODO 2й Селетор кнопки "Elements" (сайта demoqa) - #app > div > div > div.home-body > div > div:nth-child(1) > div > div.card-body
# TODO Селектор текста на стринице "Elements" -#Ad\.Plus-970x250-1


def test_check_footer_text(browser):  # Проверка текста в футере на главной странице сайте demoqa.com
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_element_text(browser):  # Проверка текста по центру на странице demoqa.com/elements
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()  # Это лишнее (E   RecursionError: maximum recursion depth exceeded)
    # assert demo_qa_page.btn_elements.exist()  # Работает
    demo_qa_page.btn_elements.click()  # FAIL!!!
    assert elements_page.equal_url()
    assert elements_page.text_center.get_text() == 'Please select an item from left to start practice.'

    # FAILED tests/tests_hw/test_check_text.py::test_check_element_text - selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="None"]"}
