# Сохранение метаданных функций в декораторах

В Python декораторы - это мощный инструмент, который позволяет изменять поведение функций. Однако, когда вы используете декоратор для обертывания функции, возникает небольшая проблема. По умолчанию метаданные исходной функции, такие как ее имя, строка документации (docstring) и аннотации, теряются. Метаданные важны, так как они помогают в интроспекции (исследовании структуры кода) и создании документации. Давайте сначала проверим эту проблему.

Откройте терминал в WebIDE. Мы выполним несколько команд Python, чтобы увидеть, что происходит, когда мы используем декоратор. Следующие команды создадут простую функцию `add`, обернутую в декоратор, а затем напечатают функцию и ее строку документации.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Когда вы выполните эти команды, вы увидите вывод, похожий на следующий:

```
<function wrapper at 0x...>
None
```

Обратите внимание, что вместо названия функции `add` выводится `wrapper`. А строка документации, которая должна быть `'Adds two things'`, равна `None`. Это может стать большой проблемой, когда вы используете инструменты, которые зависят от этих метаданных, таких как инструменты интроспекции или генераторы документации.

## Исправление проблемы с помощью functools.wraps

Модуль `functools` в Python приходит на помощь. Он предоставляет декоратор `wraps`, который может помочь нам сохранить метаданные функции. Давайте посмотрим, как мы можем изменить наш декоратор `logged` для использования `wraps`.

1. Сначала откройте файл `logcall.py` в WebIDE. Вы можете перейти в директорию проекта, используя следующую команду в терминале:

```bash
cd ~/project
```

2. Теперь обновите декоратор `logged` в файле `logcall.py` следующим кодом. Декоратор `@wraps(func)` здесь является ключевым. Он копирует все метаданные из исходной функции `func` в обертку (wrapper) функции.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. Декоратор `@wraps(func)` выполняет важную работу. Он берет все метаданные (например, имя, строку документации и аннотации) из исходной функции `func` и присоединяет их к функции-обертке `wrapper`. Таким образом, когда мы используем декорированную функцию, она будет иметь правильные метаданные.

4. Давайте протестируем наш улучшенный декоратор. Выполните следующие команды в терминале:

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Теперь вы должны увидеть:

```
<function add at 0x...>
Adds two things
```

Отлично! Имя функции и строка документации сохранены. Это означает, что наш декоратор теперь работает как ожидалось, и метаданные исходной функции не повреждены.

## Исправление декоратора в validate.py

Теперь давайте применим то же исправление к декоратору `validated` в файле `validate.py`. Этот декоратор используется для проверки типов аргументов функции и возвращаемого значения на основе аннотаций функции.

1. Откройте файл `validate.py` в WebIDE.

2. Обновите декоратор `validated` с использованием декоратора `@wraps`. Следующий код показывает, как это сделать. Декоратор `@wraps(func)` добавляется к функции-обертке `wrapper` внутри декоратора `validated` для сохранения метаданных.

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
```

3. Давайте проверим, что наш декоратор `validated` теперь сохраняет метаданные. Выполните следующие команды в терминале:

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

Вы должны увидеть:

```
<function multiply at 0......>
Multiplies two integers
```

Теперь оба декоратора, `logged` и `validated`, правильно сохраняют метаданные функций, которые они декорируют. Это гарантирует, что при использовании этих декораторов функции будут по-прежнему иметь свои исходные имена, строки документации и аннотации, что очень полезно для читаемости и поддерживаемости кода.
