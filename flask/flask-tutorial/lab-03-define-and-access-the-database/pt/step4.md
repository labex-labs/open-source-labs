# Registrando com a Aplicação

As funções `close_db` e `init_db_command` precisam ser registradas com a instância da aplicação para serem usadas pela aplicação. Como estamos usando uma função factory (fábrica), escreveremos uma função que recebe uma aplicação e faz o registro.

Adicione a seguinte função ao arquivo `db.py`:

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Em seguida, importe e chame esta função da factory. Adicione o seguinte código ao arquivo `__init__.py`:

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```
