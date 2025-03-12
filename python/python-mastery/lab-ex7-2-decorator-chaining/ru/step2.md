# Создание декораторов с аргументами

До сих пор мы использовали декоратор `@logged`, который всегда выводит фиксированное сообщение. Но что, если вы хотите настроить формат сообщения? В этом разделе мы научимся создавать новый декоратор, который может принимать аргументы, предоставляя вам больше гибкости в использовании декораторов.

## Понимание параметризованных декораторов

Параметризованный декоратор - это особый тип функции. Вместо того чтобы напрямую модифицировать другую функцию, он возвращает декоратор. Общая структура параметризованного декоратора выглядит следующим образом:

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

Когда вы используете `@decorator_with_args(value1, value2)` в своем коде, Python сначала вызывает `decorator_with_args(value1, value2)`. Этот вызов возвращает фактический декоратор, который затем применяется к функции, следующей за синтаксисом `@`. Этот двухшаговый процесс является ключом к тому, как работают параметризованные декораторы.

## Создание декоратора logformat

Давайте создадим декоратор `@logformat(fmt)`, который принимает строку формата в качестве аргумента. Это позволит нам настроить сообщение логгирования.

1. Откройте файл `logcall.py` в WebIDE и добавьте новый декоратор. Ниже приведен код, показывающий, как определить как существующий декоратор `logged`, так и новый декоратор `logformat`:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

В декораторе `logformat` внешняя функция `logformat` принимает строку формата `fmt` в качестве аргумента. Затем она возвращает функцию `decorator`, которая является фактическим декоратором, модифицирующим целевую функцию.

2. Теперь давайте протестируем наш новый декоратор, изменив файл `sample.py`. Следующий код показывает, как использовать как декоратор `logged`, так и декоратор `logformat` для разных функций:

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

Здесь функции `add` и `sub` используют декоратор `logged`, в то время как функция `mul` использует декоратор `logformat` с пользовательской строкой формата.

3. Запустите обновленный файл `sample.py`, чтобы увидеть результаты. Откройте терминал и выполните следующую команду:

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

Вы должны увидеть вывод, похожий на следующий:

```
Calling add
5
sample.py:mul
6
```

Этот вывод показывает, что декоратор `logged` выводит имя функции, как и ожидалось, а декоратор `logformat` использует пользовательскую строку формата для вывода имени файла и имени функции.

## Переопределение декоратора logged с использованием logformat

Теперь, когда у нас есть более гибкий декоратор `logformat`, мы можем переопределить наш исходный декоратор `logged`, используя его. Это поможет нам повторно использовать код и поддерживать единообразный формат логгирования.

1. Обновите файл `logcall.py` следующим кодом:

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

Здесь мы используем лямбда-функцию для определения декоратора `logged` на основе декоратора `logformat`. Лямбда-функция принимает функцию `func` и применяет декоратор `logformat` с определенной строкой формата.

2. Проверьте, что переопределенный декоратор `logged` по-прежнему работает. Откройте терминал и выполните следующую команду:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

Вы должны увидеть:

```
Calling greet
Hello, World
```

Это показывает, что переопределенный декоратор `logged` работает как ожидалось, и мы успешно повторно использовали декоратор `logformat` для достижения единообразного формата логгирования.
