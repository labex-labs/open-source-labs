# Préparation

Dans l'exercice précédent, vous avez divisé le fichier `tableformat.py` en sous-modules. La dernière partie du fichier `tableformat/formatter.py` résultant est devenue un véritable bordel d'importations.

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

Les importations au milieu du fichier sont nécessaires car la fonction `create_formatter()` en a besoin pour trouver les classes appropriées. En réalité, tout ça est un vrai bordel.
