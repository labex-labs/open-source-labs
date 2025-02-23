# Inicialización de la base de datos

A continuación, agregaremos funciones de Python que ejecutarán los comandos SQL para crear las tablas. Agrega las siguientes funciones al archivo `db.py`:

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
