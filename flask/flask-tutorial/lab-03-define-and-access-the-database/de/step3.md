# Datenbank initialisieren

Als nächstes werden wir Python-Funktionen hinzufügen, die die SQL-Befehle ausführen, um die Tabellen zu erstellen. Fügen Sie die folgenden Funktionen zur `db.py`-Datei hinzu:

```python
# flaskr/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
