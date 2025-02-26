# Dynamische Imports

Sie sind jetzt bereit für die letzte Herausforderung. Löschen Sie die folgenden Importanweisungen vollständig:

```python
# formatter.py
...

from.formats.text import TextTableFormatter     # DELETE
from.formats.csv import CSVTableFormatter       # DELETE
from.formats.html import HTMLTableFormatter     # DELETE
...
```

Führen Sie Ihren `stock.py`-Code erneut aus - es sollte mit einem Fehler fehlschlagen. Es weiß nichts über den Textformatter. Beheben Sie den Fehler, indem Sie diesen kleinen Codeausschnitt zu `create_formatter()` hinzufügen:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
  ...
```

Dieser Code versucht einen dynamischen Import eines Formatter-Moduls, wenn nichts über den Namen bekannt ist. Der Import allein (wenn er funktioniert) wird die Klasse im `_formats`-Wörterbuch registrieren und alles wird einfach funktionieren. Magie!

Versuchen Sie, den `stock.py`-Code auszuführen, und stellen Sie sicher, dass er danach funktioniert.
