# Subklassenregistrierung

Versuchen Sie das folgende Experiment und beobachten Sie:

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

Ändern Sie die Basisklasse `TableFormatter` indem Sie ein Wörterbuch und eine `__init_subclass__()`-Methode hinzufügen:

```python
class TableFormatter(ABC):
    _formats = { }

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

Dadurch lässt die Elternklasse alle ihre Unterklassen verfolgen. Überprüfen Sie es:

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

Ändern Sie die `create_formatter()`-Funktion, um die Klasse stattdessen in diesem Wörterbuch zu suchen:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Führen Sie das `stock.py`-Programm aus. Stellen Sie sicher, dass es nach diesen Änderungen immer noch funktioniert. Ein Hinweis: Alle Importanweisungen sind immer noch vorhanden. Sie haben hauptsächlich nur den Code etwas aufgeräumt und die hartcodierten Klassennamen eliminiert.
