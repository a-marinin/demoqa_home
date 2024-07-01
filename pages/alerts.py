from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        """ Class Work, 12th lesson """
        """ Для работы с Alert """
        self.alertButton = WebElement(driver, '#alertButton')  # Кнопка в алерте, которую мы будем нажимать

        """ Для работы с Confirm """
        self.confirmButton = WebElement(driver, '#confirmButton')  # Кнопка для вызова алерта Confirm
        self.confirmResult = WebElement(driver, '#confirmResult')  # Текст в алерте, появляющийся рядом с кнопкой

        """ Для работы с Prompt """
        self.promptButton = WebElement(driver, '#promtButton')  # Кнопка для вызова алерта Prompt
        self.promptResult = WebElement(driver, '#promptResult')  # Текстовое поле рядом с нашей кнопкой

        """ Home Work, 12th lesson """
        self.timerAlertButton = WebElement(driver, '#timerAlertButton')  # Кнопка для вызова алерта с таймером
