from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#userNumber')
        self.form = WebElement(driver, '#userForm')
        self.form_was_validated = WebElement(driver, '.userForm, .was-validated')  # temp
        self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        self.current_address = WebElement(driver, '#currentAddress')

        """ Элементы для дополнительного задания из ДЗ № 10. """
        # Выпадающие меню
        self.dropdown_state = WebElement(driver, '#state')  # Выпадающее меню №1 "state"
        self.dropdown_city = WebElement(driver, '#city')  # Выпадающее меню №2 "city"

        # Поля с выбранным из выдающего меню текстом
        self.dropdown_state_chosen_option = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')
        self.dropdown_city_chosen_option = WebElement(driver, '#city > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')

        """ Элементы из выпадающего меню "state", содержащие названия штатов. """
        self.select_state_option_0 = WebElement(driver, '#react-select-3-option-0')  # Штат NCR
        self.select_state_option_1 = WebElement(driver, '#react-select-3-option-1')  # Штат Uttar Pradesh
        self.select_state_option_2 = WebElement(driver, '#react-select-3-option-2')  # Штат Haryana
        self.select_state_option_3 = WebElement(driver, '#react-select-3-option-3')  # Штат Rajasthan

        """ 
        Элементы из выпадающего меню "city", содержащие названия городов. 
        Опция города select_city_option_0 применима для всех штатов (0, 1, 2 или 3).
            В зависимости от выбранного штата, её значения будут: Города Delhi, Agra, Karnal или Jaipur .
        Опция города select_city_option_1 применима для всех штатов (0, 1, 2 или 3).
            В зависимости от выбранного штата, её значения будут: Города Gurgaon, Lucknow, Panipat или Jaiselmer.
        Опция города select_city_option_2 применима только для штатов 0 и 1. Для штатов 2 и 3 - не применима.
            В зависимости от выбранного штата, её значения будут: Города Noida или Merrut.
        """

        self.select_city_option_0 = WebElement(driver, '#react-select-4-option-0')  # Город № 0
        self.select_city_option_1 = WebElement(driver, '#react-select-4-option-1')  # Город № 1
        self.select_city_option_2 = WebElement(driver, '#react-select-4-option-2')  # Город # 2
