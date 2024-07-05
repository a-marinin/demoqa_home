## Домашнее задание №7

### Задание №1

1. Создайте директорию tests_hw в папке tests все домашние тесты создавайте в ней
   1. в классе компонентов создайте метод для получения текста с элементов get_text(self).  
      текст из элемента считывайте так str(self.find_element().text)
   2. в файле test_check_text.py реализуйте таст кейс:
      1. перейти на страницу 'https://demoqa.com/'
      2. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’
   3. в файле test_check_text.py реализуйте таст кейс:
      1. перейти на страницу 'https://demoqa.com/'
      2. через кнопку перейти на страницу 'https://demoqa.com/elements'
      3. проверить что текст по центру == 'Please select an item from left to start practice.'

 
### Решения
1. Задача №1: 