# Registering with the Application

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
