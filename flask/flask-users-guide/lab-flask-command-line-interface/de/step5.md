# Registriere Befehle bei der Flask-Anwendung

Um Ihre benutzerdefinierten Befehle über die Flask CLI verfügbar zu machen, müssen Sie sie bei Ihrer Flask-Anwendung registrieren. Öffnen Sie die Datei `app.py` und ändern Sie sie wie folgt:

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Speichern Sie die Datei und starten Sie den Flask-Entwicklungsserver neu, indem Sie den Befehl `flask run` verwenden. Jetzt können Sie Ihren benutzerdefinierten Befehl `greet` von der Befehlszeile ausführen:

```
flask greet John
```

Sie sollten die Nachricht "Hello, John!" in der Konsole sehen.
