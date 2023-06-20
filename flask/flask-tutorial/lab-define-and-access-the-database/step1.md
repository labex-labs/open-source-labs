# Setting up the Database

First, we need to set up a SQLite database to store users and posts. SQLite is a convenient choice as it doesn't require a separate database server and is in-built in Python.

In our Flask application, we will create a connection to the SQLite database. This connection is typically tied to the request in web applications, and it is closed after the work is finished.

The connection is established using the `sqlite3.connect` function and we use the Flask's special object `g` to store and reuse the connection.

Create a new Python file `db.py` and add the following code:

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
