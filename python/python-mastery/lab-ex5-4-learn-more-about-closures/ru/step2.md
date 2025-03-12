# Замыкания как генератор кода

На этом этапе мы узнаем, как замыкания (closures) можно использовать для динамического генерации кода. В частности, мы создадим систему проверки типов для атрибутов класса с использованием замыканий.

Сначала разберемся, что такое замыкания. Замыкание — это объект функции, который запоминает значения из внешней области видимости, даже если они больше не находятся в памяти. В Python замыкания создаются, когда вложенная функция ссылается на значение из внешней функции.

Теперь приступим к реализации нашей системы проверки типов.

1. Создайте новый файл с именем `typedproperty.py` в директории `/home/labex/project` со следующим кодом:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    """
    Create a property with type checking.

    Args:
        name: The name of the property
        expected_type: The expected type of the property value

    Returns:
        A property object that performs type checking
    """
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

В этом коде функция `typedproperty` является замыканием. Она принимает два аргумента: `name` и `expected_type`. Декоратор `@property` используется для создания метода-геттера для свойства, который извлекает значение приватного атрибута. Декоратор `@value.setter` создает метод-сеттер, который проверяет, является ли устанавливаемое значение ожидаемого типа. Если нет, он вызывает исключение `TypeError`.

2. Теперь создадим класс, который использует эти типизированные свойства. Создайте файл с именем `stock.py` со следующим кодом:

```python
from typedproperty import typedproperty

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

В классе `Stock` мы используем функцию `typedproperty` для создания атрибутов с проверкой типов для `name`, `shares` и `price`. Когда мы создаем экземпляр класса `Stock`, проверка типов будет автоматически применена.

3. Создадим тестовый файл, чтобы увидеть это в действии. Создайте файл с именем `test_stock.py` со следующим кодом:

```python
from stock import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.shares = "hundred"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

В этом тестовом файле мы сначала создаем объект `Stock` с правильными типами. Затем мы пытаемся установить атрибут `shares` в строку, что должно вызвать исключение `TypeError`, так как ожидаемый тип — целое число.

4. Запустите тестовый файл:

```bash
python3 test_stock.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'int'>
```

Этот вывод показывает, что проверка типов работает правильно.

5. Теперь усовершенствуем файл `typedproperty.py`, добавив удобные функции для общих типов. Добавьте следующий код в конец файла:

```python
def String(name):
    """Create a string property with type checking."""
    return typedproperty(name, str)

def Integer(name):
    """Create an integer property with type checking."""
    return typedproperty(name, int)

def Float(name):
    """Create a float property with type checking."""
    return typedproperty(name, float)
```

Эти функции являются обертками вокруг функции `typedproperty`, что упрощает создание свойств общих типов.

6. Создайте новый файл с именем `stock_enhanced.py`, который использует эти удобные функции:

```python
from typedproperty import String, Integer, Float

class Stock:
    """A class representing a stock with type-checked attributes."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

В этом классе `Stock` используются удобные функции для создания атрибутов с проверкой типов, что делает код более читаемым.

7. Создайте тестовый файл `test_stock_enhanced.py` для тестирования усовершенствованной версии:

```python
from stock_enhanced import Stock

# Create a stock with correct types
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}")
print(f"Stock shares: {s.shares}")
print(f"Stock price: {s.price}")

# Try to set an attribute with the wrong type
try:
    s.price = "490.1"  # This should raise a TypeError
    print("Type check failed")
except TypeError as e:
    print(f"Type check succeeded: {e}")
```

Этот тестовый файл похож на предыдущий, но он тестирует усовершенствованный класс `Stock`.

8. Запустите тест:

```bash
python3 test_stock_enhanced.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Stock name: GOOG
Stock shares: 100
Stock price: 490.1
Type check succeeded: Expected <class 'float'>
```

На этом этапе мы продемонстрировали, как замыкания можно использовать для генерации кода. Функция `typedproperty` создает объекты свойств, которые выполняют проверку типов, а функции `String`, `Integer` и `Float` создают специализированные свойства для общих типов.
