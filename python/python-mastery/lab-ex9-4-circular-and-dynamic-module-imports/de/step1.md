# Vorbereitung

Im letzten Übungsaufgabe haben Sie die Datei `tableformat.py` in Untermodule unterteilt. Der letzte Teil der resultierenden Datei `tableformat/formatter.py` ist zu einem Durcheinander von Imports geworden.

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

Die Imports in der Mitte der Datei sind erforderlich, weil die Funktion `create_formatter()` sie benötigt, um die passenden Klassen zu finden. Eigentlich ist das Ganze ein Durcheinander.
