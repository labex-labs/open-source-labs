# Configurando la fábrica de aplicaciones

A continuación, crea un archivo `__init__.py` en el directorio `flaskr`. Este archivo tiene dos propósitos: contendrá la fábrica de aplicaciones y le indicará a Python que el directorio `flaskr` debe considerarse un paquete.

En tu archivo `__init__.py`, importa los módulos necesarios y define una función, `create_app()`, que instanciará y configurará tu aplicación.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # crea y configura la aplicación
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Se agregará más código aquí...

    return app
```
