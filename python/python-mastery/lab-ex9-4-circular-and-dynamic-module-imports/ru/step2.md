# Циклические импорты

Попробуйте перенести следующие инструкции импорта в начало файла `formatter.py`:

```python
# formatter.py

from.formats.text import TextTableFormatter
from.formats.csv import CSVTableFormatter
from.formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

...
```

Заметьте, что ничего не работает больше. Попробуйте запустить программу `stock.py` и обратите внимание на ошибку о том, что `TableFormatter` не определен. Порядок инструкций импорта имеет значение, и вы не можете просто перемещать импорты куда угодно.

Возвращайте инструкции импорта обратно на то место, где они были. Ах.
