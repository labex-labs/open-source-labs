# Захват нескольких ошибок

Вы можете ловить разные виды исключений с использованием нескольких блоков `except`.

```python
try:
...
except LookupError as e:
...
except RuntimeError as e:
...
except IOError as e:
...
except KeyboardInterrupt as e:
...
```

В альтернативном варианте, если инструкции для их обработки одинаковые, вы можете сгруппировать их:

```python
try:
...
except (IOError,LookupError,RuntimeError) as e:
...
```
