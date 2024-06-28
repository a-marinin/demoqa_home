import time
from pages.form_page import FormPage


def test_dropdown_state_and_city_options(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)

    """ Проверяем выбор всех возможных городов для Штата №0 'NCR' """
    form_page.dropdown_state.click()  # Открываем drop-down меню для выбора штата
    form_page.select_state_option_0.click()  # Выбираем штат № 0
    assert form_page.dropdown_state_chosen_option.get_text() == 'NCR'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_0.click()  # Выбираем город № 0
    assert form_page.dropdown_city_chosen_option.get_text() == 'Delhi'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_1.click()  # Выбираем город № 1
    assert form_page.dropdown_city_chosen_option.get_text() == 'Gurgaon'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_2.click()  # Выбираем город № 2
    assert form_page.dropdown_city_chosen_option.get_text() == 'Noida'
    time.sleep(2)

    """ Проверяем выбор всех возможных городов для Штата №1 'Uttar Pradesh' """
    form_page.dropdown_state.click()  # Открываем drop-down меню для выбора штата
    form_page.select_state_option_1.click()  # Выбираем штат № 1
    assert form_page.dropdown_state_chosen_option.get_text() == 'Uttar Pradesh'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_0.click()  # Выбираем город № 0
    assert form_page.dropdown_city_chosen_option.get_text() == 'Agra'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_1.click()  # Выбираем город № 1
    assert form_page.dropdown_city_chosen_option.get_text() == 'Lucknow'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_2.click()  # Выбираем город № 2
    assert form_page.dropdown_city_chosen_option.get_text() == 'Merrut'
    time.sleep(2)

    """ Проверяем выбор всех возможных городов для Штата №2 'Haryana' """
    form_page.dropdown_state.click()  # Открываем drop-down меню для выбора штата
    form_page.select_state_option_2.click()  # Выбираем штат № 2
    assert form_page.dropdown_state_chosen_option.get_text() == 'Haryana'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_0.click()  # Выбираем город № 0
    assert form_page.dropdown_city_chosen_option.get_text() == 'Karnal'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_1.click()  # Выбираем город № 1
    assert form_page.dropdown_city_chosen_option.get_text() == 'Panipat'
    time.sleep(2)

    """ Проверяем выбор всех возможных городов для Штата №2 'Rajasthan' """
    form_page.dropdown_state.click()  # Открываем drop-down меню для выбора штата
    form_page.select_state_option_3.click()  # Выбираем штат № 3
    assert form_page.dropdown_state_chosen_option.get_text() == 'Rajasthan'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_0.click()  # Выбираем город № 0
    assert form_page.dropdown_city_chosen_option.get_text() == 'Jaipur'
    time.sleep(2)

    form_page.dropdown_city.click()  # Открываем drop-down меню для выбора города
    form_page.select_city_option_1.click()  # Выбираем город № 1
    assert form_page.dropdown_city_chosen_option.get_text() == 'Jaiselmer'
    time.sleep(2)
