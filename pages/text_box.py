from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.input_name = WebElement(driver, '#userName')  # Поле Full Name
        self.input_current_address = WebElement(driver, '#currentAddress')  # Поле Current Address
        self.btn_submit = WebElement(driver, '#submit')  # Кнопка Submit

        self.output_name = WebElement(driver, '#output > div > #name')  # Name в поле вывода
        self.output_current_address = WebElement(driver, '#output > div > #currentAddress')  # Address в поле вывода
