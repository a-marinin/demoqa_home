import time
from pages.form_page import FormPage


def test_login_form_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    time.sleep(2)

    # Проверка значения атрибутов у элементов.
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'

    var_email_pattern = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
    assert form_page.user_email.get_dom_attribute('pattern') == var_email_pattern

    # Проверка наличия класса “was-validated” у элемента формы, при попытке отправки пустой формы.
    time.sleep(2)
    form_page.btn_submit.click_force()  # Нажимаем на кнопку "Submit"
    time.sleep(2)

    assert form_page.form.get_dom_attribute('class')
