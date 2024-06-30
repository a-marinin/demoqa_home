from pages.base_page import BasePage
from components.components import WebElement


class WebTablesPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        """ Элементы диалогового окна "Registration Form". """
        # Само диалоговое окно "Registration Form"
        self.dialog_box_registration_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
        # Форма "userForm". В ней находятся поля для заполнения.
        self.user_form = WebElement(driver, '#userForm')
        # Поля для заполнения в диалоговом окне "Registration Form":
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.departament = WebElement(driver, '#department')
        # Кнопка "Submit". Расположена в диалоговом окне "Registration Form"
        self.btn_submit = WebElement(driver, '#submit')

        """ Элементы главной страницы "Web Tables". """
        self.btn_add_new_record = WebElement(driver, '#addNewRecordButton')  # Кнопка "Add"

        """ Элементы 4й добавленной записи """
        self.added_4th_first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.added_4th_last_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.added_4th_email = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.added_4th_departament = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.btn_edit_4th_record = WebElement(driver, '#edit-record-4 > svg')  # Кнопка изменить 4-й элемент
        self.btn_delete_4th_record = WebElement(driver, '#delete-record-4 > svg')  # Кнопка удалить 4-й элемент

        """ Элементы, необходимые для дополнительного задания. """
        # Выпадающее меню для выбора количества записей для отображения на странице
        self.option_dropdown_page_size = WebElement(driver, ' span.select-wrap.-pageSizeOptions')
        # Опция для отображения 5 элементов на странице
        self.option_page_size_show_5_elements = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')

        # Текущее количество записей на странице
        self.qty_current_rows_on_the_page = WebElement(driver, '.rt-tr-group')

        # Кнопки Вперёд (Next) и назад (Previous) для навигации по страницам
        self.btn_previous_page = WebElement(driver, 'div.-previous > button')
        self.btn_next_page = WebElement(driver, 'div.-next > button')

        # Кнопки изменить/удалить 1-й и 6-й элементы (чтобы понять, на какой странице мы находимся (1-й или 2-й)
        self.btn_edit_1st_record = WebElement(driver, '#edit-record-1 > svg')  # Кнопка изменить 1-й элемент
        self.btn_delete_1st_record = WebElement(driver, '#delete-record-1 > svg')  # Кнопка удалить 1-й элемент

        self.btn_edit_6th_record = WebElement(driver, '#edit-record-6 > svg')  # Кнопка изменить 6-й элемент
        self.btn_delete_6th_record = WebElement(driver, '#delete-record-6 > svg')  # Кнопка удалить 6-й элемент

        # Количество доступных страниц
        self.total_pages_qty = WebElement(driver, '.-totalPages')  # Количество доступных страниц

        # Поля для ввода номера страницы "Jump to page"
        self.field_jump_to_page = WebElement(driver, 'div > input[type=number]')
