# Umgebungsbasierte Konfiguration

Es ist üblich, unterschiedliche Konfigurationen für verschiedene Umgebungen wie Entwicklung, Produktion und Testing zu haben. Flask ermöglicht es dir, die Konfigurationen basierend auf Umgebungsvariablen zu wechseln. Erstelle eine neue Datei namens `config_dev.py` und füge folgenden Code hinzu:

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

Erstelle eine weitere Datei namens `config_prod.py` mit folgendem Code:

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

In der Datei `app.py` ersetze den vorherigen Konfigurationscode durch folgenden:

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

Die Umgebungsvariable `FLASK_ENV` wird verwendet, um die Umgebung zu bestimmen. Wenn sie auf `'production'` gesetzt ist, wird die Produktionskonfiguration geladen; andernfalls wird die Entwicklungs-Konfiguration geladen.

Setze die Umgebungsvariable `FLASK_ENV` auf `'production'` und starte die Flask-Anwendung neu. Besuche `http://localhost:5000`, um die aktualisierte Nachricht mit den Produktionskonfigurationswerten zu sehen.
