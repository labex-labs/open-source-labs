# Создание декоратора для валидации

На этом этапе мы создадим более практичный декоратор. Декоратор в Python представляет собой особый тип функции, которая может изменять поведение другой функции. Создаваемый нами декоратор будет валидировать аргументы функции на основе аннотаций типов. Аннотации типов - это способ указать ожидаемые типы данных аргументов функции и возвращаемого значения. Это распространенный случай использования в реальных приложениях, так как помогает гарантировать, что функции получают правильные типы входных данных, что может предотвратить множество ошибок.

## Понимание классов валидации

Мы уже создали для вас файл с именем `validate.py`, который содержит некоторые классы валидации. Классы валидации используются для проверки, удовлетворяет ли значение определенным критериям. Чтобы посмотреть, что находится в этом файле, вам нужно открыть его в редакторе VSCode. Вы можете сделать это, выполнив следующие команды в терминале:

```bash
cd /home/labex/project
code validate.py
```

В файле есть три класса:

1. `Validator` - Это базовый класс. Базовый класс предоставляет общую структуру или каркас, от которого могут наследоваться другие классы. В данном случае он предоставляет базовую структуру для валидации.
2. `Integer` - Этот класс валидатора используется для проверки, является ли значение целым числом. Если вы передадите нецелое значение функции, которая использует этот валидатор, будет возбуждено исключение.
3. `PositiveInteger` - Этот класс валидатора гарантирует, что значение является положительным целым числом. Поэтому, если вы передадите отрицательное целое число или ноль, также будет возбуждено исключение.

## Добавление декоратора валидации

Теперь мы добавим функцию - декоратор с именем `validated` в файл `validate.py`. Этот декоратор будет выполнять несколько важных задач:

1. Он будет анализировать аннотации типов функции. Аннотации типов - это как небольшие заметки, которые сообщают нам, какого рода данные ожидает функция.
2. Он будет валидировать аргументы, переданные функции, на основе этих аннотаций типов. Это означает, что он проверит, являются ли значения, переданные функции, правильного типа.
3. Он также будет валидировать возвращаемое значение функции на основе ее аннотации. Таким образом, он гарантирует, что функция возвращает тип данных, который должна возвращать.
4. Если валидация не пройдена, он будет возбуждать информативные сообщения об ошибках. Эти сообщения будут точно сообщать вам, что пошло не так, например, какой аргумент имел неправильный тип.

Добавьте следующий код в конец файла `validate.py`:

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

Этот код использует модуль `inspect` Python. Модуль `inspect` позволяет получать информацию о живых объектах, таких как функции. Здесь мы используем его для анализа сигнатуры функции и валидации аргументов на основе аннотаций типов. Мы также используем `functools.wraps`. Это вспомогательная функция, которая сохраняет метаданные исходной функции, такие как ее имя и строка документации. Метаданные - это как дополнительная информация о функции, которая помогает нам понять, что она делает.

## Тестирование декоратора валидации

Создадим файл для тестирования нашего декоратора валидации. Мы создадим новый файл с именем `test_validate.py` и добавим в него следующий код:

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Теперь мы протестируем наш декоратор в интерпретаторе Python. Сначала перейдите в директорию проекта и запустите интерпретатор Python, выполнив следующие команды в терминале:

```bash
cd /home/labex/project
python3
```

Затем в интерпретаторе Python мы можем выполнить следующий код для тестирования нашего декоратора:

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

Как вы можете видеть, наш декоратор `validated` успешно осуществил проверку типов для аргументов функции и возвращаемых значений. Это очень полезно, так как делает наш код более надежным. Вместо того, чтобы позволять ошибкам типов распространяться глубже в код и вызывать трудновыявляемые ошибки, мы отлавливаем их на границах функций.
