import time
from pages.form_page import FormPage
from selenium import webdriver  # TEMP!
from selenium.webdriver.common.keys import Keys  # TEMP!!!


def test_state_and_city_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)

    # # РАБОТАЕТ
    # # assert form_page.dropdown_state.visible()  # Проверяем, что элемент "state" виден
    # # assert form_page.dropdown_city.visible()  # Проверяем, что элемент "city" виден
    #
    # # assert not form_page.hidden_menu.visible()
    #
    # form_page.dropdown_state.click()
    # time.sleep(3)
    # # assert not form_page.dropdown_state.visible()
    #
    # # form_page.dropdown_state.send_keys('NCR')
    # # form_page.dropdown_state.send_keys('Keys.ENTER')
    # # time.sleep(7)
    #
    # # assert form_page.hidden_menu.get_attribute() == 'test'  # НЕ РАБОТАЕТ
    # # assert form_page.hidden_menu.get_attribute2() == 'test2'  # НЕ РАБОТАЕТ
    # # assert form_page.dropdown_state.get_html_code() == 'test'  # НЕ РАБОТАЕТ
    #
    # # form_page.dropdown_state.get_html_code()
    #
    # # print(form_page.dropdown_state.get_html_code())
    # # assert form_page.dropdown_state.get_html_code() == 'test'
    #
    # # html_source = browser.page_source
    # # print(html_source)
    # # assert html_source == ' test '
    #
    # # assert form_page.hidden_menu.visible()  # РАБОТАЕТ
    # # form_page.hidden_menu.click_force()
    #
    # time.sleep(2)
    # # assert form_page.select_state_option_1.visible()  # РАБОТАЕТ
    # form_page.select_state_option_1.click()

    time.sleep(20)

    form_page.dropdown_state.click()
    time.sleep(2)
    form_page.select_state_option_0.click()
    time.sleep(2)

    form_page.dropdown_state.click()
    time.sleep(2)
    form_page.select_state_option_1.click()
    time.sleep(2)
    form_page.dropdown_state.click()
    time.sleep(2)
    form_page.select_state_option_2.click()
    time.sleep(2)
    form_page.dropdown_state.click()
    time.sleep(2)
    form_page.select_state_option_3.click()
    time.sleep(2)

    time.sleep(20)
