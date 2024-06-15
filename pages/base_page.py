"""
В файл base_page.py вынесены однотипные действия, которые мы можем совершать с web-страницей.
Класс BasePage является родительским классом для всех наших web-страниц.
От класса BasePage наследуются все другие наши web-страницы. Например:
    - Класс DemoQa, в файле /pages/demoqa.py
    - Класс ElementsPage, в файле /pages/demoqa/elements_page.py
Класс BasePage при инициализации получает 2 атрибута:
    - driver
    - base_url - Адрес нашей web-страницы. Прокидывается из дочерних классов в родительскую через функцию super().
В классе BasePage реализованы следующие методы:
    1. Метод visit - Метод для перехода на web-страницу по URL.
    2. Метод get_url - Метод для определения текущего URL web-страницы.
    3. Метод equal_url - Метод для сравнения URL web-страницы на соответствие base_url.
"""


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        # Метод, возвращающий переход на web-страницу.
        return self.driver.get(self.base_url)

    def get_url(self):
        # Метод, возвращающий текущий URL web-страницы.
        return self.driver.current_url

    def equal_url(self):
        # Метод, проверяющий текущий URL web-страницы на соответствие атрибуту base_url web-страницы.
        if self.get_url() == self.base_url:
            return True
        else:
            return False
