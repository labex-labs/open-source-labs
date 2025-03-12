# Реализация валидаторов с использованием дескрипторов

На этом этапе мы создадим систему валидации с использованием дескрипторов. Но сначала разберемся, что такое дескрипторы и почему мы их используем. Дескрипторы - это объекты Python, реализующие протокол дескрипторов, который включает методы `__get__`, `__set__` или `__delete__`. Они позволяют настроить, как осуществляется доступ к атрибуту объекта, как он устанавливается или удаляется. В нашем случае мы используем дескрипторы для создания системы валидации, которая обеспечивает целостность данных. Это означает, что данные, хранящиеся в наших объектах, всегда будут соответствовать определенным критериям, например, иметь определенный тип или быть положительными значениями.

Теперь приступим к созданию нашей системы валидации. Создадим новый файл с именем `validate.py` в директории проекта. Этот файл будет содержать классы, реализующие наши валидаторы.

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class String(Validator):
    expected_type = str

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return value


class PositiveInteger(Validator):
    expected_type = int

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        if value < 0:
            raise ValueError('Expected a positive value')
        return value


class PositiveFloat(Validator):
    expected_type = float

    @classmethod
    def check(cls, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected a number')
        if value < 0:
            raise ValueError('Expected a positive value')
        return float(value)
```

В файле `validate.py` мы сначала определяем базовый класс `Validator`. Этот класс имеет метод `__init__`, который принимает параметр `name`, который будет использоваться для идентификации атрибута, подлежащего валидации. Метод `check` - это метод класса, который просто возвращает переданное ему значение. Метод `__set__` - это метод дескриптора, который вызывается при установке атрибута объекта. Он вызывает метод `check` для валидации значения, а затем сохраняет валидированное значение в словаре объекта.

Затем мы определяем три подкласса `Validator`: `String`, `PositiveInteger` и `PositiveFloat`. Каждый из этих подклассов переопределяет метод `check` для выполнения конкретных проверок валидации. Класс `String` проверяет, является ли значение строкой, класс `PositiveInteger` проверяет, является ли значение положительным целым числом, а класс `PositiveFloat` проверяет, является ли значение положительным числом (целым или вещественным).

Теперь, когда мы определили наши валидаторы, изменим наш класс `Stock`, чтобы использовать эти валидаторы. Создадим новый файл с именем `stock_with_validators.py` и импортируем валидаторы из файла `validate.py`.

```python
# stock_with_validators.py

from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'
```

В файле `stock_with_validators.py` мы определяем класс `Stock` и используем валидаторы в качестве атрибутов класса. Это означает, что каждый раз, когда устанавливается атрибут объекта `Stock`, будет вызван метод `__set__` соответствующего валидатора для валидации значения. Метод `__init__` инициализирует атрибуты объекта `Stock`, а методы `cost`, `sell` и `__repr__` предоставляют дополнительную функциональность.

Теперь протестируем наш класс `Stock`, основанный на валидаторах. Откроем терминал, перейдем в директорию проекта и запустим файл `stock_with_validators.py` в интерактивном режиме.

```bash
cd ~/project
python3 -i stock_with_validators.py
```

После запуска интерпретатора Python мы можем попробовать несколько команд для тестирования системы валидации.

```python
# Create a stock with valid values
s = Stock('GOOG', 100, 490.10)
print(s.name)    # Should return 'GOOG'
print(s.shares)  # Should return 100
print(s.price)   # Should return 490.1

# Try changing to valid values
s.shares = 75
print(s.shares)  # Should return 75

# Try setting invalid values
try:
    s.shares = '75'  # Should raise TypeError
except TypeError as e:
    print(f"Error setting shares to string: {e}")

try:
    s.shares = -50  # Should raise ValueError
except ValueError as e:
    print(f"Error setting negative shares: {e}")

exit()
```

В тестовом коде мы сначала создаем объект `Stock` с допустимыми значениями и выводим его атрибуты, чтобы убедиться, что они установлены правильно. Затем мы пытаемся изменить атрибут `shares` на допустимое значение и выводим его снова, чтобы подтвердить изменение. Наконец, мы пытаемся установить атрибут `shares` в недопустимое значение (строку и отрицательное число) и перехватываем исключения, которые вызываются валидаторами.

Обратите внимание, как наш код стал намного чище. Класс `Stock` больше не нуждается в реализации всех этих методов-свойств - валидаторы обрабатывают все проверки типов и ограничения.

Дескрипторы позволили нам создать повторно используемую систему валидации, которая может быть применена к любому атрибуту класса. Это мощный шаблон для обеспечения целостности данных в вашем приложении.
