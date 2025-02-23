# Configuration de la base de données

Tout d'abord, nous devons configurer une base de données SQLite pour stocker les utilisateurs et les publications. SQLite est un choix pratique car il n'est pas nécessaire d'avoir un serveur de base de données séparé et est intégré à Python.

Dans notre application Flask, nous allons créer une connexion à la base de données SQLite. Cette connexion est généralement liée à la requête dans les applications web et est fermée une fois le travail terminé.

La connexion est établie à l'aide de la fonction `sqlite3.connect` et nous utilisons l'objet spécial Flask `g` pour stocker et réutiliser la connexion.

Créez un nouveau fichier Python `db.py` et ajoutez le code suivant :

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # Vérifiez si 'db' n'est pas dans 'g'
    if 'db' not in g:
        # Établissez une connexion à la base de données
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Retournez les lignes qui se comportent comme des dictionnaires
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Supprimez 'db' de 'g' et fermez la connexion s'il existe
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
