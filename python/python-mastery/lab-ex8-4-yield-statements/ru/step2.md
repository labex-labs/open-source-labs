# Генерация исключений

В файле `cofollow.py` вы создали сопрограмму `printer()`. Измените код, чтобы ловить и сообщать об исключениях следующим образом:

```python
# cofollow.py
...
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

Теперь проведите эксперимент:

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')
hello
>>> p.send(42)
42
>>> p.throw(ValueError('It failed'))
ERROR: ValueError('It failed',)
>>> try:
        int('n/a')
    except ValueError as e:
        p.throw(e)

ERROR: ValueError("invalid literal for int() with base 10: 'n/a'",)
>>>
```

Заметьте, как работающий генератор не завершается из-за исключения. Это просто позволяет оператору `yield` сигнализировать об ошибке вместо приема значения.
