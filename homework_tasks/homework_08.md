## Домашнее задание №8

### Задание №1

1. реализуйте тест кейс
   1. В папке тесто домашнего задания создайте файл test_visible_hw.py
   2. в файле создайте тест кейс test_visible_accordion(browser) в нем реализуйте кейс:
      1. перейти на страницу https://demoqa.com/accordian
         1. для этого в папке pages создайте файл accordion.py
         2. в файле реализуйте класс страницы Accordion, по аналогии с классами DemoQa и ElementsPage
         3. Отличается только название, урл и элементы
         4. в тестовом файле (test_visible_hw.py)
            1. импортируйте новый класс
            2. создайте объект страницы
            3. вызовите метод входа
               1. проверьте, что элемент #section1Content > p виден
   3. в новом классе страницы добавьте элемент с указанным локатором
   4. в тестовом файле добавьте проверку на видимость элемента
      1. кликните на #section1Heading
   5. в новом классе страницы добавьте элемент с указанным локатором
   6. в тестовом файле вызовите метод .click() для созданного элемента
      1. После клика добавьте time.sleep(2)
      2. проверьте, что элемент #section1Content > p НЕ виден
         1. добавьте проверку на видимость элемента и добавьте отрицание (элемент уже есть)


### Задание №2

1. В файле test_visible_hw.py реализуйте второй тест кейс
   1. создайте тест кейс test_visible_accordion_default(browser) в нем реализуйте кейс:
      1. перейдите на страницу https://demoqa.com/accordian
   2. создайте объект страницы
   3. вызовите метод входа
      1. проверьте, что следующие элементы по умолчанию скрыты
         1. #section2Content > p:nth-child(1)
         2. #section2Content > p:nth-child(2)
         3. #section3Content > p
      2. Для этого:
         1. Создайте каждый элемент в классе страницы
         2. в тесте вызовите проверку видимости для каждого
         3. в каждую проверку добавьте отрицание

 
### Решения
1. Задача №1: 
2. Задача №2: 