# Registrarse en la aplicación

Las funciones `close_db` e `init_db_command` deben registrarse con la instancia de la aplicación para que la aplicación las pueda utilizar. Dado que estamos utilizando una función de fábrica, escribiremos una función que tome una aplicación y realice el registro.

Agrega la siguiente función al archivo `db.py`:

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Luego, importa y llama a esta función desde la fábrica. Agrega el siguiente código al archivo `__init__.py`:

```python
# flaskr/__init__.py

def create_app():
    app =...
    # código existente omitido

    from. import db
    db.init_app(app)

    return app
```
