# Flask-Anwendung einrichten

Bevor wir den Entwicklungsserver starten können, müssen wir eine Flask-Anwendung einrichten. Erstellen Sie eine neue Python-Datei namens `app.py` und fügen Sie den folgenden Code hinzu:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

In diesem Code erstellen wir eine Flask-Anwendung und definieren einen Endpunkt, der eine einfache Nachricht "Hello, Flask!" zurückgibt. Der Block `if __name__ == "__main__":` stellt sicher, dass die Flask-Anwendung nur ausgeführt wird, wenn das Skript direkt ausgeführt wird, nicht wenn es als Modul importiert wird.
