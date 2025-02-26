# Относительные импорты

Вместо прямого использования имени пакета можно использовать `.` для ссылки на текущий пакет.

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Синтаксис:

```python
from. import modname
```

Это упрощает переименование пакета.
