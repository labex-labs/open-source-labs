# Die Verbesserung der Shell-Erfahrung

Um die Shell-Erfahrung zu verbessern, erstellen Sie ein Modul (`shelltools.py`) mit Hilfsmethoden, die in die interaktive Sitzung importiert werden können. Dieses Modul kann zusätzliche Hilfsmethoden für Aufgaben wie die Initialisierung der Datenbank oder das Löschen von Tabellen enthalten.

```python
# Datei: shelltools.py

def initialize_database():
    # Code zur Initialisierung der Datenbank
    pass

def drop_tables():
    # Code zum Löschen von Tabellen
    pass
```

In der interaktiven Shell importieren Sie die gewünschten Methoden aus dem Modul `shelltools`.

```python
# Datei: shell.py
# Ausführung: python shell.py

from shelltools import initialize_database, drop_tables

# Importieren Sie die gewünschten Methoden aus dem Modul shelltools
from shelltools import *

# Verwenden Sie die importierten Methoden
initialize_database()
drop_tables()
```
