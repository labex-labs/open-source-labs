# Registrierung bei der Anwendung

Die Funktionen `close_db` und `init_db_command` müssen bei der Anwendungsinstanz registriert werden, damit die Anwendung darauf zugreifen kann. Da wir eine Factory-Funktion verwenden, werden wir eine Funktion schreiben, die eine Anwendung nimmt und die Registrierung vornimmt.

Fügen Sie die folgende Funktion zur `db.py`-Datei hinzu:

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Dann importieren und rufen Sie diese Funktion aus der Factory auf. Fügen Sie den folgenden Code zur `__init__.py`-Datei hinzu:

```python
# flaskr/__init__.py

def create_app():
    app =...
    # vorhandener Code weggelassen

    from. import db
    db.init_app(app)

    return app
```
