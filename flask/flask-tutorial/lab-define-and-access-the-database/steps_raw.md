# Flask Database Lab

## Introduction

In this lab, we will learn how to define and access a SQLite database using the Python Flask framework. We will set up a SQLite database, establish a connection with it, create tables, and initialize the database.

## Steps

### Step 1: Setting up the Database

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

### Step 2: Creating Tables

In SQLite, data is stored in tables and columns. We need to create these before we can store and retrieve data. Our application will store users in the `user` table, and posts in the `post` table.

Create a new SQL file `schema.sql` and add the following code:

```sql
# flaskr/schema.sql

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
```

### Step 3: Initializing the Database

Next, we will add Python functions that will run the SQL commands to create the tables. Add the following functions to the `db.py` file:

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

### Step 4: Registering with the Application

The `close_db` and `init_db_command` functions need to be registered with the application instance to be used by the application. Since we're using a factory function, we will write a function that takes an application and does the registration.

Add the following function to the `db.py` file:

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

Then, import and call this function from the factory. Add the following code to the `__init__.py` file:

```python
# flaskr/__init__.py

def create_app():
    app = ...
    # existing code omitted

    from . import db
    db.init_app(app)

    return app
```

### Step 5: Initializing the Database File

Now that `init-db` has been registered with the app, it can be called using the `flask` command.

Run the `init-db` command:

```shell
flask --app flaskr init-db
Initialized the database.
```

## Summary

In this lab, we have learned how to define and access a SQLite database using the Python Flask framework. We created a connection to the database, created tables, and initialized the database. This is fundamental for any web application that needs to store and retrieve data from a database.
