#Динамические импорты

Теперь вы готовы к последней fronteire. Удалите следующие инструкции импорта полностью:

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # DELETE
from.formats.csv import CSVTableFormatter       # DELETE
from.formats.html import HTMLTableFormatter     # DELETE
...
```

Запустите снова код `stock.py` - он должен завершиться с ошибкой. Он ничего не знает о текстовом форматировщике. Исправьте это, добавив этот кусочек кода в `create_formatter()`:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

Этот код пытается динамически импортировать модуль форматировщика, если ничего не известно о имени. Просто импорт (если он работает) зарегистрирует класс в словаре `_formats` и все будет работать. Волшебство!

Попробуйте запустить код `stock.py` и убедитесь, что он работает после этого.
