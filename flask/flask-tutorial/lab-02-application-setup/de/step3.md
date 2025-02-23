# Konfigurieren der Anwendung

In derselben Datei `__init__.py` fügen Sie die erforderlichen Konfigurationsdetails für Ihre Anwendung hinzu. Dies umfasst das Festlegen eines Geheimschlüssels und die Angabe des Speicherorts Ihrer Datenbankdatei.

```python
# flaskr/__init__.py

# Mehr Code oben...

if test_config is None:
    # laden Sie die Instanzkonfiguration, wenn vorhanden, wenn nicht getestet
    app.config.from_pyfile('config.py', silent=True)
else:
    # laden Sie die Testkonfiguration, wenn sie übergeben wird
    app.config.from_mapping(test_config)

# stellen Sie sicher, dass das Instanzverzeichnis existiert
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# eine einfache Seite, die Hallo sagt
@app.route('/')
def hello():
    return 'Hello, World!'
```
