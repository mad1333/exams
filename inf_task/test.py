import unittest
from main import palindrome_cheker

# Тесты функции проверки палиндрома
class TestPalindrome(unittest.TestCase):

    # Проверка простого палиндрома
    def test_simple(self):
        print("комок:", palindrome_cheker("комок"))
        self.assertTrue(palindrome_cheker("комок"))

    # Проверка с разными регистрами
    def test_uppercase(self):
        print("ШАлаш:", palindrome_cheker("ШАлаш"))
        self.assertTrue(palindrome_cheker("ШАлаш"))

    # Проверка если не палиндром
    def test_wrong(self):
        print("мир:", palindrome_cheker("мир"))
        self.assertFalse(palindrome_cheker("мир"))

    # Пустая строка
    def test_empty(self):
        print("Пустая строка:", palindrome_cheker(""))
        self.assertTrue(palindrome_cheker(""))

    # Несколько пробелов
    def test_spaces(self):
        text = "Я иду  с мечем  судия "
        print(text, ":", palindrome_cheker(text))
        self.assertTrue(palindrome_cheker(text))

    # Из примера
    def test_example(self):
        text = "Я иду с мечем судия"
        print(text, ":", palindrome_cheker(text))
        self.assertTrue(palindrome_cheker(text))

    # Еще один палиндром
    def test_another(self):
        text = "Нажал кабан на баклажан"
        print(text, ":", palindrome_cheker(text))
        self.assertTrue(palindrome_cheker(text))


if __name__ == "__main__":
    unittest.main()
