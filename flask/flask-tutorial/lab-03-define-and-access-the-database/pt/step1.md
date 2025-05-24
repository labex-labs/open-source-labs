# Configurando o Banco de Dados

Primeiramente, precisamos configurar um banco de dados SQLite para armazenar usuários e posts. SQLite é uma escolha conveniente, pois não requer um servidor de banco de dados separado e é embutido no Python.

Em nossa aplicação Flask, criaremos uma conexão com o banco de dados SQLite. Essa conexão é tipicamente atrelada à requisição em aplicações web, e é fechada após o trabalho ser finalizado.

A conexão é estabelecida usando a função `sqlite3.connect` e usamos o objeto especial do Flask `g` para armazenar e reutilizar a conexão.

Crie um novo arquivo Python `db.py` e adicione o seguinte código:

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    # Check if 'db' is not in 'g'
    if 'db' not in g:
        # Establish a connection to the database
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Return rows that behave like dicts
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    # Pop 'db' from 'g' and close the connection if it exists
    db = g.pop('db', None)

    if db is not None:
        db.close()
```
