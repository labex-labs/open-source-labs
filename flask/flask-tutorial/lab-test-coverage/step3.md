# Creating Fixtures

Fixtures are setup functions that are used by your tests. They are responsible for creating a test environment, such as a temporary database, and setting up any necessary data.

In this step, you will create fixtures that will be used by your tests. These fixtures will create a temporary database and populate it with test data.

Create a file named `conftest.py` in the `tests` directory and add the following code:

```python
import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

# Define the test data
with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)
    os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
```

This code defines three fixtures: `app`, `client`, and `runner`. The `app` fixture creates the Flask application with the test configuration and sets up the database. The `client` fixture creates a test client that can make requests to the application. The `runner` fixture creates a test CLI runner that can call the Click commands registered with the application.
