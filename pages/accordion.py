from pages.base_page import BasePage
from components.components import WebElement

"""
# Это новый файл для домашнего задания №8.
В файле accordion_page.py создан класс AccordionPage - это страница элементов нашего сайта (demoqa.com/accordian).
Класс AccordionPage наследуется от родительского класс BasePage. 

В классе ElementsPage описаны web-элементы (и их CSS-локаторы), находящиеся только на этой странице:
1. КАРТЫ:
    1.1. Карта №1 "What is Lorem Ipsum?" (card_what_is_lorem_ipsum):
        - Под ней скрыт 1 текст (text_what_is_lorem_ipsum).
    1.2. Карты №2 "Where does it come from?" (card_where_does_it_come_from):
        - Под ней скрыто 2 текста (text_where_does_it_come_from_1 и text_where_does_it_come_from_2).
    1.3. Карты №3 "Why do we use it?" (card_why_do_we_use_it):
        - Под ней скрыт 1 текст (text_why_do_we_use_it).
2. ТЕКСТЫ:
    2.1. Текст №1 (text_what_is_lorem_ipsum). 
        - Он скрыт за 1-м аккордеоном "What is Lorem Ipsum?" (card_what_is_lorem_ipsum). 
    2.2. Текст №2 (text_where_does_it_come_from_1). 
        - Он скрыт за 2-м аккордеоном "Where does it come from?" (card_where_does_it_come_from).
    2.3. Текст №3 (text_where_does_it_come_from_2). 
        - Он скрыт за 2-м аккордеоном "Where does it come from?" (card_where_does_it_come_from).
    2.4. Текст №4 (text_why_do_we_use_it). 
        - От скрыт за 3-м аккордеоном "Why do we use it?" (card_why_do_we_use_it).
"""


class AccordionPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        '''1. Карты (каждая разворачивает свою часть аккордеона)'''
        # Карта №1 "What is Lorem Ipsum?". Её нажатие показывает/скрывает 1-й текст.
        self.card_what_is_lorem_ipsum = WebElement(driver, '#section1Heading')
        # Карта №2 "Where does it come from?". Её нажатие показывает/скрывает 2-й и 3-й тексты.
        self.card_where_does_it_come_from = WebElement(driver, '#section2Heading')
        # Карта №3 "Why do we use it?". Её нажатие показывает/скрывает 4й текст.
        self.card_why_do_we_use_it = WebElement(driver, '#section3Heading')

        '''2. Тексты'''
        # Текст №1, содержащийся в 1-м аккордеоне "What is Lorem Ipsum?"
        self.text_what_is_lorem_ipsum = WebElement(driver, '#section1Content > p')
        # Текст №2, содержащийся во 2-м аккордеоне "Where does it come from?".
        self.text_where_does_it_come_from_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        # Текст №3, содержащийся во 2-м аккордеоне "Where does it come from?".
        self.text_where_does_it_come_from_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        # Текст №4, содержащийся в 3-м аккордеоне "Why do we use it?".
        self.text_why_do_we_use_it = WebElement(driver, '#section3Content > p')
