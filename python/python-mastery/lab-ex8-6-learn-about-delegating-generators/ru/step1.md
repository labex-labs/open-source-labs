# Пример: Прием сообщений

В упражнении 8.3 мы рассматривали определения корутин. Корутины были функциями, в которые вы отправляли данные. Например:

```python
>>> from cofollow import consumer
>>> @consumer
    def printer():
        while True:
            item = yield
            print('Получено:', item)

>>> p = printer()
>>> p.send('Hello')
Получено: Hello
>>> p.send('World')
Получено: World
>>>
```

В то время было бы интересно использовать `yield` для приема значения. Однако, если вы внимательно посмотрите на код, он выглядит довольно странно - простой `yield`? Что здесь происходит?

В файле `cofollow.py` определите следующую функцию:

```python
def receive(expected_type):
    msg = yield
    assert isinstance(msg, expected_type), 'Ожидаемый тип %s' % (expected_type)
    return msg
```

Эта функция получает сообщение, а затем проверяет, что оно имеет ожидаемый тип. Попробуйте ее:

```python
>>> from cofollow import consumer, receive
>>> @consumer
    def print_ints():
        while True:
             val = yield from receive(int)
             print('Получено:', val)

>>> p = print_ints()
>>> p.send(42)
Получено: 42
>>> p.send(13)
Получено: 13
>>> p.send('13')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
...
AssertionError: Ожидаемый тип <class 'int'>
>>>
```

Из точки зрения читаемости, выражение `yield from receive(int)` более информативно - оно показывает, что функция будет приостанавливаться, пока не получит сообщение заданного типа.

Теперь измените все корутины в `coticker.py`, чтобы использовать новую функцию `receive()` и убедитесь, что код из упражнения 8.3 по-прежнему работает.
