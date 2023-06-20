# Define and Access the Database

## Introduction

In this lab, you will learn how to define and access a database in a Flask application. We will be using SQLite as our database, which is a built-in database in Python. SQLite is convenient because it doesn't require setting up a separate database server. However, for larger applications, you may want to consider switching to a different database.

## Steps

### Step 1: Connect to the Database

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

### Step 2: Close the Database Connection

To ensure that the database connection is closed properly after each request, we need to define a function to close the connection. This function will be called `close_db()`.

```python
# flaskr/db.py

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

In this code, we check if a connection exists in the `g` object and close it if it does. We also remove the connection from the `g` object.

### Step 3: Initialize the Database

Next, we need to create the tables in the SQLite database. We will define the SQL commands to create the tables in a separate file called `schema.sql`.

```sql
-- flaskr/schema.sql

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

In this code, we drop any existing tables and then create two new tables: `user` and `post`.

To execute these SQL commands and initialize the database, we need to define the `init_db()` function.

```python
# flaskr/db.py

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
```

In this code, we use the `get_db()` function to get a database connection and then execute the SQL commands from the `schema.sql` file.

### Step 4: Register with the Application

To ensure that the `close_db()` and `init_db()` functions are used by the application, we need to register them with the Flask application instance. We will define a function called `init_app()` to handle this registration.

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

In this code, we use the `teardown_appcontext()` method to register the `close_db()` function to be called when cleaning up after returning the response. We also use the `cli.add_command()` method to add the `init_db_command` as a new command that can be called with the `flask` command.

### Step 5: Initialize the Database File

Now that we have registered the `init_db()` function with the app, we can use the `flask` command to initialize the database file.

```shell
$ flask --app flaskr init-db
Initialized the database.
```

This command will create a `flaskr.sqlite` file in the `instance` folder of your project.

## Summary

In this lab, you learned how to define and access a database in a Flask application using SQLite. You learned how to connect to the database, close the database connection, initialize the database tables, and register the database functions with the Flask application.
