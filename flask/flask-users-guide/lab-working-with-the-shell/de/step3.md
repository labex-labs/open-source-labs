# Auslösen von Funktionen vor/nach der Anforderung

Durch das Erstellen eines Anforderungskontexts wird der Code, der normalerweise vor einer Anforderung ausgeführt wird, nicht ausgelöst. Um die Funktionalität vor der Anforderung zu simulieren, rufen Sie die Methode `preprocess_request()` auf. Dadurch wird sichergestellt, dass Datenbankverbindungen und andere Ressourcen verfügbar sind.

```python
# Datei: shell.py
# Ausführung: python shell.py

from flask import Flask

app = Flask(__name__)

# Erstellen eines Anforderungskontexts
ctx = app.test_request_context()
ctx.push()

# Simulieren der Funktionalität vor der Anforderung
app.preprocess_request()

# Arbeiten mit dem Anforderungsobjekt

# Aufschieben des Anforderungskontexts
ctx.pop()
```

Um die Funktionalität nach der Anforderung zu simulieren, rufen Sie die Methode `process_response()` mit einem Platzhalter-Response-Objekt auf, bevor Sie den Anforderungskontext aufschieben.

```python
# Datei: shell.py
# Ausführung: python shell.py

from flask import Flask

app = Flask(__name__)

# Erstellen eines Anforderungskontexts
ctx = app.test_request_context()
ctx.push()

# Simulieren der Funktionalität vor der Anforderung
app.preprocess_request()

# Arbeiten mit dem Anforderungsobjekt

# Simulieren der Funktionalität nach der Anforderung
app.process_response(app.response_class())

# Aufschieben des Anforderungskontexts
ctx.pop()
```
