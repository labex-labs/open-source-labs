# Inscription à l'application

Les fonctions `close_db` et `init_db_command` doivent être enregistrées avec l'instance de l'application pour être utilisées par l'application. Étant donné que nous utilisons une fonction de fabrique, nous allons écrire une fonction qui prend une application et effectue l'enregistrement.

Ajoutez la fonction suivante au fichier `db.py` :

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Ensuite, importez et appelez cette fonction à partir de la fabrique. Ajoutez le code suivant au fichier `__init__.py` :

```python
# flaskr/__init__.py

def create_app():
    app =...
    # code existant omis

    from. import db
    db.init_app(app)

    return app
```
