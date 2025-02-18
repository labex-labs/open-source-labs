# Создание модульных тестов: базовые тесты

Теперь напишем несколько тестов, чтобы убедиться, что наша функция работает правильно. Мы будем использовать модуль `unittest` Python. Создайте новый файл с именем `test_key_of_max.py` и добавьте следующий код:

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Объяснение:

1.  **`import unittest`**: Импортирует фреймворк для тестирования.
2.  **`from key_of_max import key_of_max`**: Импортирует функцию, которую мы хотим протестировать.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: Определяет _тестовый класс_. Тестовые классы группируют связанные тесты.
4.  **`def test_basic_case(self):`**: Определяет _тестовый метод_. Каждый тестовый метод проверяет определенный аспект нашей функции. Имена тестовых методов _должны_ начинаться с `test_`.
5.  **`self.assertEqual(...)`**: Это _утверждение_ (assertion). Оно проверяет, равны ли два значения. Если они не равны, тест не проходит. В данном случае мы проверяем, возвращает ли `key_of_max({'a': 4, 'b': 0, 'c': 13})` `'c'`, как и должно быть.
6.  **`def test_another_case(self):`**: Добавлен еще один тестовый случай для проверки ключа максимального значения, которое может не быть уникальным.
7.  **`if __name__ == '__main__': unittest.main()`**: Этот стандартный идиом Python запускает тесты, когда вы выполняете скрипт напрямую (например, `python3 test_key_of_max.py`).

Запустите тесты из терминала: `python3 test_key_of_max.py`. Вы должны увидеть вывод, показывающий, что оба теста прошли успешно.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
