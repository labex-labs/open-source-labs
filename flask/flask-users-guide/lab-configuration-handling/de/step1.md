# Erstelle eine Flask-Anwendung

Zunächst erstellen wir eine einfache Flask-Anwendung. Erstelle eine Datei namens `app.py` und füge den folgenden Code hinzu:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

Um die Anwendung auszuführen, führe den folgenden Befehl in deiner Konsole aus:

```shell
python app.py
```

Öffne deinen Webbrowser und besuche `http://localhost:5000`, um die Nachricht "Hello, Flask!" zu sehen.
