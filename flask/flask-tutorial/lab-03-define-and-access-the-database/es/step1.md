# Configuración de la base de datos

En primer lugar, necesitamos configurar una base de datos SQLite para almacenar usuarios y publicaciones. SQLite es una buena opción ya que no requiere un servidor de base de datos separado y está integrado en Python.

En nuestra aplicación Flask, crearemos una conexión a la base de datos SQLite. Esta conexión generalmente está vinculada a la solicitud en aplicaciones web y se cierra una vez que se ha terminado el trabajo.

La conexión se establece utilizando la función `sqlite3.connect` y utilizamos el objeto especial `g` de Flask para almacenar y reutilizar la conexión.

Crea un nuevo archivo de Python `db.py` y agrega el siguiente código:

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # Verifica si 'db' no está en 'g'
    if 'db' not in g:
        # Establece una conexión a la base de datos
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Devuelve filas que se comportan como diccionarios
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Elimina 'db' de 'g' y cierra la conexión si existe
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
