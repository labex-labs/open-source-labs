# Initialisation de la base de données

Ensuite, nous allons ajouter des fonctions Python qui exécuteront les commandes SQL pour créer les tables. Ajoutez les fonctions suivantes au fichier `db.py` :

```python
# flaskr/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
```
