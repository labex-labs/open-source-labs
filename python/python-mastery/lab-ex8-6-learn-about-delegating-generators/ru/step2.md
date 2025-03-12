# Использование `yield from` в корутинах

На этом этапе мы рассмотрим, как использовать оператор `yield from` с корутинами для более практических применений. Корутины - это мощная концепция в Python, и понимание того, как использовать `yield from` с ними, может значительно упростить ваш код.

## Корутины и передача сообщений

Корутины - это специальные функции, которые могут получать значения через оператор `yield`. Они чрезвычайно полезны для таких задач, как обработка данных и обработка событий. В файле `cofollow.py` есть декоратор `consumer`. Этот декоратор помогает настроить корутины, автоматически продвигая их до первой точки `yield`. Это означает, что вам не нужно вручную запускать корутину; декоратор делает это за вас.

Создадим корутину, которая получает значения и проверяет их типы. Вот как вы можете это сделать:

1. Сначала откройте файл `cofollow.py` в редакторе. Вы можете использовать следующую команду в терминале, чтобы перейти в правильную директорию:

```bash
cd /home/labex/project
```

2. Затем добавьте следующую функцию `receive` в конец файла `cofollow.py`. Эта функция представляет собой корутину, которая будет получать сообщение и проверять его тип.

```python
def receive(expected_type):
    """
    A coroutine that receives a message and validates its type.
    Returns the received message if it matches the expected type.
    """
    msg = yield
    assert isinstance(msg, expected_type), f'Expected type {expected_type}'
    return msg
```

Вот что делает эта функция:

- Она использует `yield` без выражения для получения значения. Когда в корутину отправляют значение, этот оператор `yield` захватывает его.
- Она проверяет, является ли полученное значение ожидаемого типа, используя функцию `isinstance`. Если типы не совпадают, она вызывает исключение `AssertionError`.
- Если проверка типа проходит успешно, она возвращает значение.

3. Теперь создадим корутину, которая использует `yield from` с нашей функцией `receive`. Эта новая корутина будет получать и выводить только целые числа.

```python
@consumer
def print_ints():
    """
    A coroutine that receives and prints integers only.
    Uses yield from to delegate to the receive coroutine.
    """
    while True:
        val = yield from receive(int)
        print('Got:', val)
```

4. Чтобы протестировать эту корутину, откройте оболочку Python и выполните следующий код:

```python
from cofollow import print_ints

p = print_ints()
p.send(42)
p.send(13)
try:
    p.send('13')  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Вы должны увидеть следующий вывод:

```
Got: 42
Got: 13
Error: Expected type <class 'int'>
```

## Понимание работы `yield from` с корутинами

Когда мы используем `yield from receive(int)` в корутине `print_ints`, происходят следующие шаги:

1. Управление делегируется корутине `receive`. Это означает, что корутина `print_ints` приостанавливается, и начинает выполняться корутина `receive`.
2. Корутина `receive` использует `yield` для получения значения. Она ожидает, пока в нее отправят значение.
3. Когда в `print_ints` отправляют значение, на самом деле его получает `receive`. Оператор `yield from` заботится о передаче значения из `print_ints` в `receive`.
4. Корутина `receive` проверяет тип полученного значения. Если тип правильный, она возвращает значение.
5. Возвращенное значение становится результатом выражения `yield from` в корутине `print_ints`. Это означает, что переменной `val` в `print_ints` присваивается значение, возвращаемое `receive`.

Использование `yield from` делает код более читаемым, чем если бы мы должны были напрямую обрабатывать выдачу и получение значений. Он абстрагирует сложность передачи значений между корутинами.

## Создание более сложных корутин для проверки типов

Расширим наши вспомогательные функции, чтобы они могли обрабатывать более сложную проверку типов. Вот как вы можете это сделать:

1. Добавьте следующие функции в файл `cofollow.py`:

```python
def receive_dict():
    """Receive and validate a dictionary"""
    result = yield from receive(dict)
    return result

def receive_str():
    """Receive and validate a string"""
    result = yield from receive(str)
    return result

@consumer
def process_data():
    """Process different types of data using the receive utilities"""
    while True:
        print("Waiting for a string...")
        name = yield from receive_str()
        print(f"Got string: {name}")

        print("Waiting for a dictionary...")
        data = yield from receive_dict()
        print(f"Got dictionary with {len(data)} items: {data}")

        print("Processing complete for this round.")
```

2. Чтобы протестировать новую корутину, откройте оболочку Python и выполните следующий код:

```python
from cofollow import process_data

proc = process_data()
proc.send("John Doe")
proc.send({"age": 30, "city": "New York"})
proc.send("Jane Smith")
try:
    proc.send(123)  # This should raise an AssertionError
except AssertionError as e:
    print(f"Error: {e}")
```

Вы должны увидеть такой вывод:

```
Waiting for a string...
Got string: John Doe
Waiting for a dictionary...
Got dictionary with 2 items: {'age': 30, 'city': 'New York'}
Processing complete for this round.
Waiting for a string...
Got string: Jane Smith
Waiting for a dictionary...
Error: Expected type <class 'dict'>
```

Оператор `yield from` делает код чище и более читаемым. Он позволяет нам сосредоточиться на высокоуровневой логике нашей программы, а не тратить время на детали передачи сообщений между корутинами.
