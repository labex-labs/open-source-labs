# Close the Database Connection

To ensure that the database connection is closed properly after each request, we need to define a function to close the connection. This function will be called `close_db()`.

```python
# flaskr/db.py

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
```

In this code, we check if a connection exists in the `g` object and close it if it does. We also remove the connection from the `g` object.
