# Grundlegende Konfiguration

Fügen wir nun einigen grundlegenden Konfigurationen zu unserer Flask-Anwendung hinzu. In derselben Datei `app.py` fügen wir folgenden Code hinzu:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

Die `DEBUG`-Konfiguration aktiviert den Debug-Modus, der während der Entwicklung hilfreiche Fehlermeldungen liefert. Die `SECRET_KEY`-Konfiguration wird verwendet, um Sitzungscookies sicher zu signieren und andere sicherheitsrelevante Anforderungen zu erfüllen.

Um auf die Konfigurationswerte zuzugreifen, kannst du das `app.config`-Dictionary verwenden. Beispielsweise um den Wert von `SECRET_KEY` auszugeben, füge folgenden Code der `hello`-Route hinzu:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Starte die Flask-Anwendung neu und besuche `http://localhost:5000`, um die aktualisierte Nachricht mit dem Geheimschlüssel zu sehen.
