# Datenbank einrichten

Zunächst müssen wir eine SQLite-Datenbank einrichten, um Benutzer und Beiträge zu speichern. SQLite ist eine bequeme Wahl, da es keinen separaten Datenbankserver erfordert und in Python integriert ist.

In unserer Flask-Anwendung werden wir eine Verbindung zur SQLite-Datenbank herstellen. Diese Verbindung ist in Webanwendungen typischerweise an der Anfrage gebunden und wird nach Abschluss der Arbeit geschlossen.

Die Verbindung wird mit der `sqlite3.connect`-Funktion hergestellt, und wir verwenden das spezielle Flask-Objekt `g`, um die Verbindung zu speichern und wiederzuverwenden.

Erstellen Sie eine neue Python-Datei `db.py` und fügen Sie den folgenden Code hinzu:

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # Überprüfen, ob 'db' nicht in 'g' ist
    if 'db' not in g:
        # Herstellen einer Verbindung zur Datenbank
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Rückgabe von Zeilen, die wie Dicts verhalten
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Entfernen von 'db' aus 'g' und Schließen der Verbindung, wenn sie existiert
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
