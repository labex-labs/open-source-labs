# Улучшение опыта работы с оболочкой

Для улучшения опыта работы с оболочкой создайте модуль (`shelltools.py`), содержащий вспомогательные методы, которые можно импортировать в интерактивную сессию. Этот модуль может содержать дополнительные вспомогательные методы для задач, таких как инициализация базы данных или удаление таблиц.

```python
# File: shelltools.py

def initialize_database():
    # Код для инициализации базы данных
    pass

def drop_tables():
    # Код для удаления таблиц
    pass
```

В интерактивной оболочке импортируйте нужные методы из модуля `shelltools`.

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# Импортируйте нужные методы из модуля shelltools
from shelltools import *

# Используйте импортированные методы
initialize_database()
drop_tables()
```
