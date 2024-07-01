import time
from pages.webtables import WebTablesPage


def test_sorting_web_tables(browser):
    web_tables = WebTablesPage(browser)

    web_tables.visit()  # Посещаем страницу
    time.sleep(2)

    # Создаём лист с заголовка колонок, для упрощения работы и чтобы не повторять в коде одни и те же действия по 6 раз
    column_list = [web_tables.col_1, web_tables.col_2, web_tables.col_3, web_tables.col_4,
                   web_tables.col_5, web_tables.col_6]#, web_tables.col_7]

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
