# Instanzordner

Flask bietet einen Instanzordner zum Speichern von Konfigurationsdateien, die für eine bestimmte Bereitstellung spezifisch sind. Dadurch kannst du die für die Bereitstellung spezifischen Konfigurationen von dem Rest deines Codes trennen. Standardmäßig verwendet Flask einen Ordner namens `instance` im selben Verzeichnis wie deine Anwendung.

Erstelle einen neuen Ordner namens `instance` im selben Verzeichnis wie deine `app.py`-Datei. Im `instance`-Ordner erstelle eine Datei namens `config.cfg` und füge folgenden Code hinzu:

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

In der `app.py`-Datei füge folgenden Code vor dem Konfigurationscode hinzu:

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

Der `instance_path` wird auf den absoluten Pfad des `instance`-Ordners gesetzt. Die `from_pyfile`-Methode lädt die Konfiguration aus der `config.cfg`-Datei im Instanzordner.

Starte die Flask-Anwendung neu und besuche `http://localhost:5000`, um die aktualisierte Nachricht mit den Instanz-Konfigurationswerten zu sehen.
