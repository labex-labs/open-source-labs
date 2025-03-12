# Эффективное создание классов

Теперь, когда вы понимаете, как создавать классы с использованием функции `type()`, мы рассмотрим более эффективный способ создания нескольких похожих классов. Этот метод сэкономит вам время и уменьшит дублирование кода, сделав процесс программирования более плавным.

## Понимание существующих классов валидаторов

Сначала нам нужно открыть файл `validate.py` в WebIDE. Этот файл уже содержит несколько классов валидаторов, которые используются для проверки, удовлетворяют ли значения определенным условиям. Эти классы включают `Validator`, `Positive`, `PositiveInteger` и `PositiveFloat`. Мы добавим базовый класс `Typed` и несколько валидаторов, специфичных для определенных типов, в этот файл.

Для открытия файла выполните следующую команду в терминале:

```bash
cd ~/project
```

## Добавление класса валидатора Typed

Начнем с добавления класса валидатора `Typed`. Этот класс будет использоваться для проверки, является ли значение ожидаемого типа.

```python
class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)
```

В этом коде `expected_type` по умолчанию установлен на `object`. Подклассы переопределят это значением конкретного типа, который они проверяют. Метод `check` использует функцию `isinstance` для проверки, является ли значение ожидаемого типа. Если нет, он вызывает исключение `TypeError`.

Традиционно мы бы создали валидаторы, специфичные для определенных типов, следующим образом:

```python
class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Однако этот подход является повторяющимся. Мы можем сделать лучше, используя конструктор `type()` для динамического создания этих классов.

## Динамическое создание валидаторов типов

Мы заменим отдельные определения классов более эффективным подходом.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

Вот что делает этот код:

1. Он определяет список кортежей. Каждый кортеж содержит имя класса и соответствующий тип Python.
2. Он использует генераторное выражение с функцией `type()` для создания каждого класса. Функция `type()` принимает три аргумента: имя класса, кортеж базовых классов и словарь атрибутов класса.
3. Он использует `globals().update()` для добавления только что созданных классов в глобальное пространство имен. Это делает классы доступными в рамках всего модуля.

Ваш завершенный файл `validate.py` должен выглядеть приблизительно так:

```python
# Basic validator classes

class Validator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value <= 0:
            raise ValueError('Expected a positive value')
        super().check(value)

class PositiveInteger(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, int):
            raise TypeError('Expected an integer')
        super().check(value)

class PositiveFloat(Positive):
    @classmethod
    def check(cls, value):
        if not isinstance(value, float):
            raise TypeError('Expected a float')
        super().check(value)

class Typed(Validator):
    expected_type = object  # Default, will be overridden in subclasses

    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        super().check(value)

# Generate type validators dynamically
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str)
]

globals().update((name, type(name, (Typed,), {'expected_type': ty}))
                 for name, ty in _typed_classes)
```

## Тестирование динамически созданных классов

Теперь давайте протестируем наши динамически созданные классы валидаторов. Сначала откройте интерактивную оболочку Python.

```bash
cd ~/project
python3
```

Как только вы окажетесь в оболочке Python, импортируйте и протестируйте наши валидаторы.

```python
from validate import Integer, Float, String

# Test the Integer validator
i = Integer()
i.__set_name__(None, 'test_int')
try:
    i.check("not an integer")
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"Integer validation: {e}")

# Test the String validator
s = String()
s.__set_name__(None, 'test_str')
try:
    s.check(123)
    print("Error: Check passed when it should have failed")
except TypeError as e:
    print(f"String validation: {e}")

# Add a new validator class to the list
import sys
print("Current validator classes:", [cls for cls in dir() if cls in ['Integer', 'Float', 'String']])
```

Вы должны увидеть вывод, показывающий ошибки валидации типов. Это указывает на то, что наши динамически созданные классы работают правильно.

После завершения тестирования выйдите из оболочки Python:

```python
exit()
```

## Расширение динамического создания классов

Если вы хотите добавить больше валидаторов типов, вы можете просто обновить список `_typed_classes` в файле `validate.py`.

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str),
    ('List', list),
    ('Dict', dict),
    ('Bool', bool)
]
```

Этот подход предоставляет мощный и эффективный способ создания нескольких похожих классов без написания повторяющегося кода. Он позволяет легко масштабировать ваше приложение по мере роста требований.
