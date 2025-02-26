# Problem: Imports

Imports zwischen Dateien im selben Paket _müssen jetzt den Paketnamen im Import enthalten_. Denken Sie sich die Struktur ein.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Verändertes Importbeispiel.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Alle Imports sind _absolut_, nicht relativ.

```python
import fileparse    # Bricht. fileparse nicht gefunden

...
```
