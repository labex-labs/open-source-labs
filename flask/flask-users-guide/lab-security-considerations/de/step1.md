# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) ist eine Schwachstelle, die Angreifern ermöglicht, böswillige Skripte in von Benutzern angesehene Webanwendungen einzufügen. Um XSS-Angriffe in Flask zu verhindern, folgen Sie diesen Richtlinien:

- Entfernen Sie immer Sonderzeichen, um die Einbindung beliebiger HTML-Tags zu vermeiden.
- Seien Sie vorsichtig, wenn Sie HTML ohne die Hilfe von Jinja2-Vorlagen generieren.
- Verwenden Sie die `Markup`-Klasse, um benutzerdefinierte Daten zu filtern.
- Vermeiden Sie das Senden von HTML- oder Textdateien aus hochgeladenen Dateien.

Beispielcode:

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

Um den Code auszuführen, speichern Sie ihn in einer Datei namens `app.py` und führen Sie den Befehl `flask run` aus.
