# Проблема: Импорты

Импорты между файлами в одном пакете _теперь должны включать имя пакета в импорте_. Помните структуру.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Измененный пример импорта.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Все импорты _абсолютные_, а не относительные.

```python
import fileparse    # BREAKS. fileparse не найден

...
```
