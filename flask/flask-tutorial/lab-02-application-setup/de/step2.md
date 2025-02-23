# Einrichten der Anwendungsfabrik

Als nächstes erstellen Sie eine Datei `__init__.py` im Verzeichnis `flaskr`. Diese Datei hat zwei Zwecke: Sie enthält die Anwendungsfabrik und signalisiert Python, dass das Verzeichnis `flaskr` als Paket behandelt werden soll.

In Ihrer Datei `__init__.py` importieren Sie die erforderlichen Module und definieren eine Funktion `create_app()`, die Ihre Anwendung instanziiert und konfiguriert.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Weitere Codezeilen werden hier hinzugefügt...

    return app
```
