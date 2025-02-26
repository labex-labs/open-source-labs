# Registro de subclases

Intenta el siguiente experimento y observa:

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

Modifica la clase base `TableFormatter` agregando un diccionario y un método `__init_subclass__()`:

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

Esto hace que la clase padre registre todas sus subclases. Echa un vistazo:

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

Modifica la función `create_formatter()` para buscar la clase en este diccionario en lugar de hacerlo de otra manera:

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

Ejecuta el programa `stock.py`. Asegúrate de que todavía funcione después de hacer estos cambios. Solo para anotar que todas las declaraciones de importación todavía están ahí. Simplemente has limpiado un poco el código y eliminado los nombres de clase fijos.
