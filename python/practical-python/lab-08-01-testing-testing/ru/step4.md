# Модуль `unittest`

Предположим, у вас есть некоторый код в `simple.py`.

```python
# simple.py

def add(x, y):
    return x + y
```

Теперь, предположим, вы хотите протестировать его. Создайте отдельный файл для тестирования, например, в `/home/labex/project/test_simple.py`, следующим образом.

```python
# test_simple.py

import simple
import unittest
```

Затем определите класс для тестирования.

```python
# test_simple.py

import simple
import unittest

# Обратите внимание, что он наследуется от unittest.TestCase
class TestAdd(unittest.TestCase):
  ...
```

Класс для тестирования должен наследоваться от `unittest.TestCase`.

В классе для тестирования вы определяете методы для тестирования.

```python
# test_simple.py

import simple
import unittest

# Обратите внимание, что он наследуется от unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Тестирование с простыми целыми аргументами
        r = simple.add(2, 2)
        self.assertEqual(r, 5)
    def test_str(self):
        # Тестирование со строками
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')
```

\*Важно: Каждый метод должен начинаться с `test`.
