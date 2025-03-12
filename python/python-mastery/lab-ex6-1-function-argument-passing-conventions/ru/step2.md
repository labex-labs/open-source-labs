# Создание базового класса структуры

Теперь, когда мы хорошо понимаем передачу аргументов функций, мы создадим переиспользуемый базовый класс для структур данных. Этот шаг является важным, так как он помогает нам избежать повторного написания одного и того же кода при создании простых классов, которые хранят данные. Используя базовый класс, мы можем упростить наш код и сделать его более эффективным.

## Проблема с повторяющимся кодом

В предыдущих упражнениях вы определили класс `Stock`, как показано ниже:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Внимательно посмотрите на метод `__init__`. Вы заметите, что он довольно повторяющийся. Вам приходится вручную присваивать каждое атрибут по отдельности. Это может стать очень утомительным и затратным по времени, особенно когда у вас есть много классов с большим количеством атрибутов.

## Создание гибкого базового класса

Давайте создадим базовый класс `Structure`, который может автоматически обрабатывать назначение атрибутов. Сначала откройте WebIDE и создайте новый файл с именем `structure.py`. Затем добавьте следующий код в этот файл:

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

Этот базовый класс имеет несколько важных особенностей:

1. Он определяет переменную класса `_fields`. По умолчанию эта переменная пуста. Эта переменная будет хранить имена атрибутов, которые будет иметь класс.
2. Он проверяет, совпадает ли количество аргументов, переданных в конструктор, с количеством полей, определенных в `_fields`. Если они не совпадают, он вызывает исключение `TypeError`. Это помогает нам выявлять ошибки на ранней стадии.
3. Он устанавливает атрибуты объекта, используя имена полей и значения, предоставленные в качестве аргументов. Функция `setattr` используется для динамического установки атрибутов.

## Тестирование нашего базового класса структуры

Теперь давайте создадим несколько примеров классов, которые наследуются от базового класса `Structure`. Добавьте следующий код в файл `structure.py`:

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

Чтобы проверить, работает ли наша реализация правильно, мы создадим тестовый файл с именем `test_structure.py`. Добавьте следующий код в этот файл:

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Чтобы запустить тест, откройте терминал и выполните следующую команду:

```bash
python3 test_structure.py
```

Вы должны увидеть следующий вывод:

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Как вы можете видеть, наш базовый класс работает как ожидалось. Он значительно упростил определение новых структур данных без необходимости повторно писать один и тот же шаблонный код.
