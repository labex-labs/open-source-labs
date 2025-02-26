# Enregistrement des sous-classes

Essayez l'expérience suivante et observez :

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

Modifiez la classe de base `TableFormatter` en ajoutant un dictionnaire et une méthode `__init_subclass__()` :

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

Cela permet à la classe parente de suivre toutes ses sous-classes. Vérifions :

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

Modifiez la fonction `create_formatter()` pour rechercher la classe dans ce dictionnaire à la place :

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

Exécutez le programme `stock.py`. Assurez-vous qu'il fonctionne toujours après avoir effectué ces modifications. Juste une note, toutes les instructions d'importation sont toujours là. Vous avez essentiellement juste nettoyé un peu le code et éliminé les noms de classes codés en dur.
