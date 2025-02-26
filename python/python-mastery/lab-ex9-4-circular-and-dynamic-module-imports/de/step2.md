# Kreisimporte

Versuchen Sie, die folgenden Importanweisungen nach oben in die Datei `formatter.py` zu verschieben:

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

Beobachten Sie, dass nichts mehr funktioniert. Versuchen Sie, das Programm `stock.py` auszuführen, und bemerken Sie den Fehler, dass `TableFormatter` nicht definiert ist. Die Reihenfolge der Importanweisungen spielt eine Rolle, und Sie können die Imports nicht einfach an einen beliebigen Ort verschieben.

Bewegen Sie die Importanweisungen wieder an ihren ursprünglichen Ort. Ach.
