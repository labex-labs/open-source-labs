# Connect to the Database

The first step is to create a connection to the SQLite database. We will use the `sqlite3` module, which is built-in to Python. The connection will be created within the `get_db()` function.

```python
# flaskr/db.py

import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db
```

In this code, we first check if a connection to the database already exists in the `g` object, which is unique for each request. If it doesn't exist, we create a new connection using the `sqlite3.connect()` method. We also set the `row_factory` to `sqlite3.Row` to allow accessing the columns by name.
