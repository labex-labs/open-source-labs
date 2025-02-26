# Preparación

En el último ejercicio, dividiste el archivo `tableformat.py` en submódulos. La última parte del archivo resultante `tableformat/formatter.py` se ha convertido en un desorden de importaciones.

```python
# tableformat.py
...

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from.formats.text import TextTableFormatter
from.formats.csv import CSVTableFormatter
from.formats.html import HTMLTableFormatter

...

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Las importaciones en medio del archivo son necesarias porque la función `create_formatter()` las necesita para encontrar las clases adecuadas. En realidad, todo esto es un desastre.
