import time
from pages.webtables import WebTablesPage


def test_sorting_web_tables(browser):
    """ Проверка сортировки колонок через класс элемента """
    web_tables = WebTablesPage(browser)

    web_tables.visit()  # Посещаем страницу
    time.sleep(2)

    # Создаём лист с заголовка колонок, для упрощения работы и чтобы не повторять в коде одни и те же действия по 6 раз
    column_list = [web_tables.col_1, web_tables.col_2, web_tables.col_3, web_tables.col_4,
                   web_tables.col_5, web_tables.col_6]

    for column in column_list:
        """ 1. Проверяем дефолтные значения колонок """
        # 1.1. Проверяем, что колонки существуют на странице
        assert column.exist()
        # 1.2. Проверяем, что у всех колонок отсутствует сортировка (стоит значение класса по-умолчанию)
        assert column.get_dom_attribute('class') == 'rt-th rt-resizable-header -cursor-pointer'

        """ 2. Кликаем на каждую колонку -> Сортируем по убыванию (Descending Order) """
        column.click()
        # 2.1. Проверяем, что колонка отсортирована по убыванию
        assert column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
        # 2.2. Также дополнительно проверяем, что колонка НЕ отсортирована по возрастанию
        assert not column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
        # 2.3. Также дополнительно, на всякий случай, проверяем, что значение класса по-умолчанию были изменено
        assert not column.get_dom_attribute('class') == 'rt-resizable-header-content'

        """ 3. Кликаем на каждую колонку ещё раз -> Сортируем по возрастанию (Ascending Order) """
        column.click()
        # 3.1. Проверяем, что колонка отсортирована по возрастанию
        assert column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
        # 3.2. Также дополнительно проверяем, что колонка НЕ отсортирована по убыванию
        assert not column.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
        # 3.3. Также дополнительно, на всякий случай, проверяем, что значение класса по-умолчанию были изменено
        assert not column.get_dom_attribute('class') == 'rt-resizable-header-content'


def test_advanced_sorting_web_tables(browser):
    """ Проверка сортировки колонок через значения колонок """
    web_tables = WebTablesPage(browser)

    web_tables.visit()  # Посещаем страницу
    time.sleep(2)

    # Создаём лист с дефолтными значениями для каждой колонки
    col_1_default_values = ['Cierra', 'Alden', 'Kierra']  # Колонка 'First Name'
    col_2_default_values = ['Vega', 'Cantrell', 'Gentry']  # Колонка 'Last Name'
    col_3_default_values = ['39', '45', '29']  # Колонка 'Age'
    col_4_default_values = ['cierra@example.com', 'alden@example.com', 'kierra@example.com']  # Колонка 'Email'
    col_5_default_values = ['10000', '12000', '2000']  # Колонка 'Salary'
    col_6_default_values = ['Insurance', 'Compliance', 'Legal']  # Колонка 'Department'

    """ 1. Проверяем дефолтные значения колонок (без сортировки) """
    # Создаём лист с текстом каждого элемент для каждой строки
    col_1_current_values = [web_tables.row_1_first_name.get_text(), web_tables.row_2_first_name.get_text(),
                            web_tables.row_3_first_name.get_text()]
    col_2_current_values = [web_tables.row_1_last_name.get_text(), web_tables.row_2_last_name.get_text(),
                            web_tables.row_3_last_name.get_text()]
    col_3_current_values = [web_tables.row_1_age.get_text(), web_tables.row_2_age.get_text(),
                            web_tables.row_3_age.get_text()]
    col_4_current_values = [web_tables.row_1_email.get_text(), web_tables.row_2_email.get_text(),
                            web_tables.row_3_email.get_text()]
    col_5_current_values = [web_tables.row_1_salary.get_text(), web_tables.row_2_salary.get_text(),
                            web_tables.row_3_salary.get_text()]
    col_6_current_values = [web_tables.row_1_departament.get_text(), web_tables.row_2_departament.get_text(),
                            web_tables.row_3_departament.get_text()]

    assert col_1_current_values == col_1_default_values  # Проверяем колонку 'First Name'
    assert col_2_current_values == col_2_default_values  # Проверяем колонку 'Last Name'
    assert col_3_current_values == col_3_default_values  # Проверяем колонку 'Age'
    assert col_4_current_values == col_4_default_values  # Проверяем колонку 'Email'
    assert col_5_current_values == col_5_default_values  # Проверяем колонку 'Salary'
    assert col_6_current_values == col_6_default_values  # Проверяем колонку 'Department'

    """ 2. Проверяем сортировку по возрастанию (Ascending Order) для каждой колонки """
    # Проверяем колонку 'First Name'
    web_tables.col_1.click()  # Кликаем на колонку 'First Name'
    # Создаём список с текущими значениями в колонке 'First Name'
    col_1_current_values = [web_tables.row_1_first_name.get_text(), web_tables.row_2_first_name.get_text(),
                            web_tables.row_3_first_name.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_1_current_values == sorted(col_1_default_values)

    # Проверяем колонку 'Last Name'
    web_tables.col_2.click()  # Кликаем на колонку 'Last Name'
    # Создаём список с текущими значениями в колонке 'Last Name'
    col_2_current_values = [web_tables.row_1_last_name.get_text(), web_tables.row_2_last_name.get_text(),
                            web_tables.row_3_last_name.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_2_current_values == sorted(col_2_default_values)

    # Проверяем колонку 'Age'
    web_tables.col_3.click()  # Кликаем на колонку 'Age'
    # Создаём список с текущими значениями в колонке 'Age'
    col_3_current_values = [web_tables.row_1_age.get_text(), web_tables.row_2_age.get_text(),
                            web_tables.row_3_age.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_3_current_values == sorted(col_3_default_values)

    # Проверяем колонку 'Email'
    web_tables.col_4.click()  # Кликаем на колонку 'Email'
    # Создаём список с текущими значениями в колонке 'Email'
    col_4_current_values = [web_tables.row_1_email.get_text(), web_tables.row_2_email.get_text(),
                            web_tables.row_3_email.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_4_current_values == sorted(col_4_default_values)

    # Проверяем колонку 'Salary'
    web_tables.col_5.click()  # Кликаем на колонку 'Salary'
    # Создаём список с текущими значениями в колонке 'Salary'
    col_5_current_values = [web_tables.row_1_salary.get_text(), web_tables.row_2_salary.get_text(),
                            web_tables.row_3_salary.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_5_current_values == sorted(col_5_default_values, key=int)

    # Проверяем колонку 'Department'
    web_tables.col_6.click()  # Кликаем на колонку 'Department'
    # Создаём список с текущими значениями в колонке 'Department'
    col_6_current_values = [web_tables.row_1_departament.get_text(), web_tables.row_2_departament.get_text(),
                            web_tables.row_3_departament.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_6_current_values == sorted(col_6_default_values)

    """ 3. Проверяем сортировку по по убыванию (Descending Order) для каждой колонки """
    # Проверяем колонку 'First Name'
    web_tables.col_1.click()  # Кликаем на колонку 'First Name'
    web_tables.col_1.click()  # Кликаем на колонку 'First Name' ещё раз
    # Создаём список с текущими значениями в колонке 'First Name'
    col_1_current_values = [web_tables.row_1_first_name.get_text(), web_tables.row_2_first_name.get_text(),
                            web_tables.row_3_first_name.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_1_current_values == sorted(col_1_default_values, reverse=True)

    # Проверяем колонку 'Last Name'
    web_tables.col_2.click()  # Кликаем на колонку 'Last Name'
    web_tables.col_2.click()  # Кликаем на колонку 'Last Name' ещё раз
    # Создаём список с текущими значениями в колонке 'Last Name'
    col_2_current_values = [web_tables.row_1_last_name.get_text(), web_tables.row_2_last_name.get_text(),
                            web_tables.row_3_last_name.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_2_current_values == sorted(col_2_default_values, reverse=True)

    # Проверяем колонку 'Age'
    web_tables.col_3.click()  # Кликаем на колонку 'Age'
    web_tables.col_3.click()  # Кликаем на колонку 'Age' ещё раз
    # Создаём список с текущими значениями в колонке 'Age'
    col_3_current_values = [web_tables.row_1_age.get_text(), web_tables.row_2_age.get_text(),
                            web_tables.row_3_age.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_3_current_values == sorted(col_3_default_values, reverse=True)

    # Проверяем колонку 'Email'
    web_tables.col_4.click()  # Кликаем на колонку 'Email'
    web_tables.col_4.click()  # Кликаем на колонку 'Email' ещё раз
    # Создаём список с текущими значениями в колонке 'Email'
    col_4_current_values = [web_tables.row_1_email.get_text(), web_tables.row_2_email.get_text(),
                            web_tables.row_3_email.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_4_current_values == sorted(col_4_default_values, reverse=True)

    # Проверяем колонку 'Salary'
    web_tables.col_5.click()  # Кликаем на колонку 'Salary'
    web_tables.col_5.click()  # Кликаем на колонку 'Salary' ещё раз
    # Создаём список с текущими значениями в колонке 'Salary'
    col_5_current_values = [web_tables.row_1_salary.get_text(), web_tables.row_2_salary.get_text(),
                            web_tables.row_3_salary.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_5_current_values == sorted(col_5_default_values, key=int, reverse=True)

    # Проверяем колонку 'Department'
    web_tables.col_6.click()  # Кликаем на колонку 'Department'
    web_tables.col_6.click()  # Кликаем на колонку 'Department' ещё раз
    # Создаём список с текущими значениями в колонке 'Department'
    col_6_current_values = [web_tables.row_1_departament.get_text(), web_tables.row_2_departament.get_text(),
                            web_tables.row_3_departament.get_text()]
    # Сверяем значения, отсортированные на сайте со значениями, отсортированными в Python
    assert col_6_current_values == sorted(col_6_default_values, reverse=True)
