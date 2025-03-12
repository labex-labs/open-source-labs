# Устранение имен свойств с использованием дескрипторов

На предыдущем этапе при создании типизированных свойств нам приходилось явно указывать имена свойств. Это избыточно, так как имена свойств уже указаны в определении класса. На этом этапе мы используем дескрипторы (descriptors), чтобы избавиться от этой избыточности.

Дескриптор в Python — это специальный объект, который контролирует, как происходит доступ к атрибутам. Когда вы реализуете метод `__set_name__` в дескрипторе, он может автоматически получить имя атрибута из определения класса.

Начнем с создания нового файла.

1. Создайте новый файл с именем `improved_typedproperty.py` со следующим кодом:

```python
# improved_typedproperty.py

class TypedProperty:
    """
    A descriptor that performs type checking.

    This descriptor automatically captures the attribute name from the class definition.
    """
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        # This method is called when the descriptor is assigned to a class attribute
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

# Convenience functions
def String():
    """Create a string property with type checking."""
    return TypedProperty(str)

def Integer():
    """Create an integer property with type checking."""
    return TypedProperty(int)

def Float():
    """Create a float property with type checking."""
    return TypedProperty(float)
```

В этом коде определен класс-дескриптор `TypedProperty`, который проверяет тип значений, присваиваемых атрибутам. Метод `__set_name__` вызывается автоматически, когда дескриптор присваивается атрибуту класса. Это позволяет дескриптору получить имя атрибута без необходимости вручную его указывать.

Далее создадим класс, который использует эти улучшенные типизированные свойства.

2. Создайте новый файл с именем `stock_improved.py`, который использует улучшенные типизированные свойства:

```python
from improved_typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    # No need to specify property names anymore
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Обратите внимание, что при создании типизированных свойств нам больше не нужно указывать имена свойств. Дескриптор автоматически получит имя атрибута из определения класса.

Теперь протестируем наш улучшенный класс.

3. Создайте тестовый файл `test_stock_improved.py` для тестирования улучшенной версии:

```python
from stock_improved import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try setting attributes with wrong types
try:
    s.name = 123  # Should raise TypeError
    print("Name type check failed")
except TypeError as e:
    print(f"Name type check succeeded: {e}")

try:
    s.shares = "hundred"  # Should raise TypeError
    print("Shares type check failed")
except TypeError as e:
    print(f"Shares type check succeeded: {e}")

try:
    s.price = "490.1"  # Should raise TypeError
    print("Price type check failed")
except TypeError as e:
    print(f"Price type check succeeded: {e}")
```

Наконец, запустим тест, чтобы убедиться, что все работает как ожидается.

4. Запустите тест:

```bash
python3 test_stock_improved.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Name type check succeeded: Expected <class 'str'>
Shares type check succeeded: Expected <class 'int'>
Price type check succeeded: Expected <class 'float'>
```

На этом этапе мы улучшили нашу систему проверки типов, используя дескрипторы и метод `__set_name__`. Это избавило нас от избыточной спецификации имен свойств, сделав код короче и менее подверженным ошибкам.

Метод `__set_name__` является очень полезной функцией дескрипторов. Он позволяет им автоматически собирать информацию о том, как они используются в определении класса. Это можно использовать для создания API, которые легче понять и использовать.
