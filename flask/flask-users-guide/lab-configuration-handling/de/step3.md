# Konfiguration aus Dateien

Das Hardcodieren von Konfigurationswerten im Code ist nicht ideal, insbesondere für sensible Informationen. Flask bietet eine Möglichkeit, die Konfiguration aus separaten Dateien zu laden. Erstelle eine neue Datei namens `config.py` und füge folgenden Code hinzu:

```python
DEBUG = False
SECRET_KEY ='myothersecretkey'
```

In der Datei `app.py` ersetze den vorherigen Konfigurationscode durch folgenden:

```python
app.config.from_object('config')
```

Die `from_object`-Methode lädt die Konfiguration aus dem `config`-Modul. Jetzt werden die `DEBUG`- und `SECRET_KEY`-Werte aus der `config.py`-Datei geladen.

Starte die Flask-Anwendung neu und besuche `http://localhost:5000`, um die aktualisierte Nachricht mit den neuen Konfigurationswerten zu sehen.
