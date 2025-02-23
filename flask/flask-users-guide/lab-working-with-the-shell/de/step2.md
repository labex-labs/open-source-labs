# Das Erstellen eines Anforderungskontexts

Um in der Shell einen geeigneten Anforderungskontext zu erstellen, verwenden Sie die Methode `test_request_context()`, die ein `RequestContext`-Objekt erstellt. In der Shell können Sie den Anforderungskontext manuell mit den Methoden `push()` und `pop()` auf- und abschieben.

```python
# Datei: shell.py
# Ausführung: python shell.py

from flask import Flask

app = Flask(__name__)

# Erstellen eines Anforderungskontexts
ctx = app.test_request_context()

# Abschieben des Anforderungskontexts
ctx.push()

# Arbeiten mit dem Anforderungsobjekt

# Aufschieben des Anforderungskontexts
ctx.pop()
```
