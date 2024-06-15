import pytest
from selenium import webdriver


'''В данном случае декоратор @pytest.fixture изменяет поведение функции browser'''
@pytest.fixture(scope="session") # Это декоратор (функция-обёртка, изменяющая поведение другой функции)
def browser():
    driver = webdriver.Chrome()  # Передали наш драйвер
    yield driver  # Чтобы наш драйвер мог использовать в функции
    driver.quit()  # Закрываем драйвер
