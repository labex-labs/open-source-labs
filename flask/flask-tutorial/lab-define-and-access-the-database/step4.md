# Register with the Application

To ensure that the `close_db()` and `init_db()` functions are used by the application, we need to register them with the Flask application instance. We will define a function called `init_app()` to handle this registration.

```python
# flaskr/db.py

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
```

In this code, we use the `teardown_appcontext()` method to register the `close_db()` function to be called when cleaning up after returning the response. We also use the `cli.add_command()` method to add the `init_db_command` as a new command that can be called with the `flask` command.
