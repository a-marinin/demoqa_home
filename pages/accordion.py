from pages.base_page import BasePage
from components.components import WebElement

# Это новый файл для домашнего задания №8.


class AccordionPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        # Текст, содержащийся в 1-м аккордеоне "What is Lorem Ipsum?" на странице demoqa.com/accordian
        self.text_what_is_lorem_ipsum = WebElement(driver, '#section1Content > p')
