# Реализация валидации типов с использованием аннотаций функций

В Python вы можете добавлять аннотации типов к параметрам функций. Эти аннотации служат для указания ожидаемых типов данных параметров и возвращаемого значения функции. По умолчанию они не обеспечивают соблюдение типов во время выполнения, но их можно использовать для валидации.

Давайте посмотрим на пример:

```python
def add(x: int, y: int) -> int:
    return x + y
```

В этом коде `x: int` и `y: int` сообщают, что параметры `x` и `y` должны быть целыми числами. `-> int` в конце указывает, что функция `add` возвращает целое число. Эти аннотации типов хранятся в атрибуте `__annotations__` функции, который представляет собой словарь, отображающий имена параметров на их аннотированные типы.

Теперь мы улучшим наш класс `ValidatedFunction`, чтобы он использовал эти аннотации типов для валидации. Для этого нам понадобится модуль `inspect` Python. Этот модуль предоставляет полезные функции для получения информации о живых объектах, таких как модули, классы, методы, функции и т.д. В нашем случае мы используем его для сопоставления аргументов функции с соответствующими именами параметров.

Сначала нам нужно изменить класс `ValidatedFunction` в файле `validate.py`. Вы можете открыть этот файл с помощью следующей команды:

```bash
code /home/labex/project/validate.py
```

Замените существующий класс `ValidatedFunction` на следующую улучшенную версию:

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

Вот что делает эта улучшенная версия:

1. Она использует `inspect.signature()`, чтобы получить информацию о параметрах функции, таких как их имена, значения по умолчанию и аннотированные типы.
2. Метод `bind()` сигнатуры используется для сопоставления предоставленных аргументов с соответствующими именами параметров. Это помогает нам связать каждый аргумент с правильным параметром в функции.
3. Она проверяет каждый аргумент на соответствие его аннотации типа (если таковая существует). Если аннотация найдена, она извлекает класс валидатора из аннотации и применяет валидацию с помощью метода `check()`.
4. Наконец, она вызывает исходную функцию с валидированными аргументами.

Теперь давайте протестируем этот улучшенный класс `ValidatedFunction` с некоторыми функциями, которые используют наши классы валидаторов в своих аннотациях типов. Откройте файл `test_validation.py` с помощью следующей команды:

```bash
code /home/labex/project/test_validation.py
```

Добавьте следующий код в файл:

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

В этом коде мы определяем функцию `greet` с аннотациями типов `name: String` и `times: Integer`. Это означает, что параметр `name` должен быть валидирован с использованием класса `String`, а параметр `times` - с использованием класса `Integer`. Затем мы оборачиваем функцию `greet` в наш класс `ValidatedFunction`, чтобы включить валидацию типов.

Мы выполняем три тестовых случая: правильный вызов, неправильный вызов с неправильным типом для `name` и неправильный вызов с неправильным типом для `times`. Каждый вызов обернут в блок `try-except`, чтобы поймать любые исключения `TypeError`, которые могут быть возбуждены во время валидации.

Чтобы запустить тестовый файл, используйте следующую команду:

```bash
python3 /home/labex/project/test_validation.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

Этот вывод показывает, что наш вызываемый объект `ValidatedFunction` теперь обеспечивает валидацию типов на основе аннотаций функций. Когда мы передаем аргументы неправильного типа, классы валидаторов обнаруживают ошибку и возбуждают исключение `TypeError`. Таким образом, мы можем гарантировать, что функции вызываются с правильными типами данных, что помогает предотвратить ошибки и делает наш код более надежным.
