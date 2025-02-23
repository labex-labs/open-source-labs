# Erstellen einer Flask-Anwendung

Erstellen Sie eine neue Python-Datei mit dem Namen `app.py` und fügen Sie den folgenden Code hinzu, um eine einfache Flask-Anwendung zu erstellen:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Speichern Sie die Datei und führen Sie sie im Terminal mit dem folgenden Befehl aus:

```
python app.py
```
