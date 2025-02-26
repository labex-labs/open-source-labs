# Importaciones circulares

Intenta mover las siguientes declaraciones de importación al principio del archivo `formatter.py`:

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

Observa que nada funciona más. Intenta ejecutar el programa `stock.py` y fíjate en el error sobre `TableFormatter` no estar definido. El orden de las declaraciones de importación importa y no puedes simplemente mover las importaciones a donde quieras.

Mueve las declaraciones de importación de vuelta a donde estaban. Jaja.
