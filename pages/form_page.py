from components.components import WebElement
from pages.base_page import BasePage


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        # self.gender_radio_1 = WebElement(driver, '#gender-radio-1')
        # self.user_number = WebElement(driver, '#userNumber')
        self.btn_submit = WebElement(driver, '#userNumber')
        self.form = WebElement(driver, '#userForm')
        self.form_was_validated = WebElement(driver, '.userForm, .was-validated')  # temp
        # self.modal_dialog = WebElement(driver, 'body > div.fade.modal.show > div')
        # self.btn_close_modal = WebElement(driver, '#closeLargeModal')
        # self.hobbies = WebElement(driver, '#hobbies-checkbox-1')
        # self.current_address = WebElement(driver, '#currentAddress')

        """ Элементы для дополнительного задания из ДЗ № 10 """
        self.dropdown_state = WebElement(driver, '#state')  # Выпадающее меню "state"
        self.dropdown_city = WebElement(driver, '#city')  # Выпадающее меню "state"

        """ Не пригодилось """
        # self.hidden_menu = WebElement(driver, '#state > div.css-26l3qy-menu')
        # self.option_state_1 = WebElement(driver, 'NCR')
        # self.text_form_for_state = WebElement(driver, '#state > div > div.css-1hwfws3 > div.css-1uccc91-singleValue')


        # GOOD SELECTORS!
        self.select_state_option_0 = WebElement(driver, '#react-select-3-option-0')  # NCR
        self.select_state_option_1 = WebElement(driver, '#react-select-3-option-1')  # Uttar Pradesh
        self.select_state_option_2 = WebElement(driver, '#react-select-3-option-2')  # Haryana
        self.select_state_option_3 = WebElement(driver, '#react-select-3-option-3')  # Rajasthan
