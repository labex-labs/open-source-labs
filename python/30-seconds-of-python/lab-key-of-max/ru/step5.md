# Тестирование со всеми отрицательными значениями

В качестве последнего теста давайте рассмотрим случай, когда все значения в словаре отрицательны. Добавьте этот метод в класс `TestKeyOfMax`:

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

Этот тест гарантирует, что наша функция правильно определяет _наименее отрицательное_ значение (которое в данном случае является максимальным) и возвращает соответствующий ключ.

Запустите тесты последний раз (`python3 test_key_of_max.py`). Все четыре теста должны пройти успешно. Это дает нам большую уверенность в том, что наша функция работает правильно.

Ваш полный файл `test_key_of_max.py` должен теперь выглядеть так:

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

Запустите тесты еще раз (`python3 test_key_of_max.py`). Все четыре теста должны пройти успешно. Это дает нам большую уверенность в том, что наша функция работает правильно.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
