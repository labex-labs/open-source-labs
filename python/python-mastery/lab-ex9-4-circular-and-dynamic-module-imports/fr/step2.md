# Importations circulaires

Essayez de déplacer les instructions d'importation suivantes en haut du fichier `formatter.py` :

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

Remarquez que rien ne fonctionne plus. Essayez d'exécuter le programme `stock.py` et remarquez l'erreur concernant le fait que `TableFormatter` n'est pas définie. L'ordre des instructions d'importation est important et vous ne pouvez pas simplement déplacer les importations n'importe où vous le voulez.

Replacez les instructions d'importation à leur emplacement initial. Sigh.
