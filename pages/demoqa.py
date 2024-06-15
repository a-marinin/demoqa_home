from pages.base_page import BasePage
from components.components import WebElement

"""
В файле base_page.py создан класс DemoQa - это домашняя страница нашего сайта (demoqa.com).
Класс DemoQa наследуется от родительского класс BasePage. 
В классе DemoQa описаны web-элементы (и их CSS-локаторы), находящиеся только на этой странице:
    1. text_footer - Это текст, находящийся в футере домашней страницы.
    2. btn_elements - Это кнопка "Elements", ведущая на страницу demoqa.com/elements 
"""


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.text_footer = WebElement(driver, '#app > footer > span')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
