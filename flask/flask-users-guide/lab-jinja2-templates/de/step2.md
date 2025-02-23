# Erstelle eine Flask-Anwendung

Erstelle eine neue Datei namens `app.py` und importiere die erforderlichen Module:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

In diesem Code erstellen wir eine neue Flask-Anwendung und definieren eine Route für die Stamm-URL ("/"). Wenn ein Benutzer die Stamm-URL besucht, wird die `index()`-Funktion aufgerufen und die `index.html`-Vorlage gerendert.
