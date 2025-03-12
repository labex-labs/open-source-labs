# Создание декоратора для принудительного применения типов с аргументами

В предыдущих шагах мы узнали о декораторе `@validated`. Этот декоратор используется для принудительного применения аннотаций типов в функциях Python. Аннотации типов - это способ указать ожидаемые типы аргументов функции и возвращаемого значения. Теперь мы пойдем дальше. Мы создадим более гибкий декоратор, который может принимать спецификации типов в качестве аргументов. Это означает, что мы можем определить типы, которые мы хотим для каждого аргумента и возвращаемого значения, более явно.

## Понимание цели

Наша цель - создать декоратор `@enforce()`. Этот декоратор позволит нам задавать ограничения типов с использованием именованных аргументов. Вот пример того, как он будет работать:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

В этом примере мы используем декоратор `@enforce` для указания того, что аргументы `x` и `y` функции `add` должны быть типа `Integer`, а возвращаемое значение также должно быть типа `Integer`. Этот декоратор будет вести себя аналогично нашему предыдущему декоратору `@validated`, но он дает нам больше контроля над спецификациями типов.

## Создание декоратора enforce

1. Сначала откройте файл `validate.py` в WebIDE. Мы добавим наш новый декоратор в этот файл. Вот код, который мы добавим:

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

Давайте разберем, что делает этот код. Класс `Integer` используется для определения пользовательского типа. Декоратор `validated` проверяет типы аргументов функции и возвращаемого значения на основе аннотаций типов функции. Декоратор `enforce` - это новый, который мы создаем. Он принимает именованные аргументы, которые задают типы для каждого аргумента и возвращаемого значения. Внутри функции `wrapper` декоратора `enforce` мы проверяем, соответствуют ли типы аргументов и возвращаемого значения указанным типам. Если нет, мы вызываем исключение `TypeError`.

2. Теперь давайте протестируем наш новый декоратор `@enforce`. Мы запустим несколько тестовых случаев, чтобы проверить, работает ли он как ожидается. Вот код для запуска тестов:

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

В этом тестовом коде мы сначала определяем функцию `add` с декоратором `@enforce`. Затем мы вызываем функцию `add` с допустимыми аргументами, что должно работать без ошибок. Далее мы вызываем функцию `add` с недопустимым аргументом, что должно вызвать исключение `TypeError`. Наконец, мы определяем функцию `bad_add`, которая возвращает значение неправильного типа, что также должно вызвать исключение `TypeError`.

При запуске этого тестового кода вы должны увидеть вывод, похожий на следующий:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

Этот вывод показывает, что наш декоратор `@enforce` работает правильно. Он вызывает исключение `TypeError`, когда типы аргументов или возвращаемого значения не соответствуют указанным типам.

## Сравнение двух подходов

Декораторы `@validated` и `@enforce` достигают одной и той же цели - принудительного применения ограничений типов, но они делают это разными способами.

1. Декоратор `@validated` использует встроенные аннотации типов Python. Вот пример:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   С помощью этого подхода мы задаем типы непосредственно в определении функции с использованием аннотаций типов. Это встроенная функция Python, и она обеспечивает лучшую поддержку в интегрированных средах разработки (IDE). IDE могут использовать эти аннотации типов для предоставления автодополнения кода, проверки типов и других полезных функций.

2. С другой стороны, декоратор `@enforce` использует именованные аргументы для указания типов. Вот пример:

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   Этот подход более явный, так как мы напрямую передаем спецификации типов в качестве аргументов декоратора. Он может быть полезен при работе с библиотеками, которые используют другие системы аннотаций.

Каждый подход имеет свои преимущества. Аннотации типов являются частью языка Python и обеспечивают лучшую поддержку в IDE, в то время как подход с `@enforce` дает нам больше гибкости и явности. Вы можете выбрать подход, который лучше всего подходит для ваших нужд, в зависимости от проекта, над которым вы работаете.
