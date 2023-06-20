# Initialize the Database

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
