# Flask Testing Lab

## Introduction

In this lab, we will learn how to write unit tests for a Flask application. We will use `pytest` and `coverage` to test and measure our code. By the end of this lab, you will understand how to ensure your application works as expected and identify areas that need improvement.

## Steps

### Step 1: Install Pytest and Coverage

Firstly, we need to install `pytest` and `coverage`. These are testing and code measurement tools respectively. Run the following command in your terminal to install:

```bash
pip install pytest coverage
```

### Step 2: Setup and Fixtures

Next, we will set up test fixtures in a file called `conftest.py`. A fixture is a function that is run before each test function to which it is applied.

In this step, we will create a temporary database and populate it with some data for testing.

Here is the code to add in `tests/conftest.py`:

```python
# tests/conftest.py

import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

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

### Step 3: Write Tests for Factory

Next, we will write tests for the factory function which is responsible for creating the Flask application. These tests ensure that the application behaves as expected based on the configuration passed to it.

Here is the code to add in `tests/test_factory.py`:

```python
# tests/test_factory.py

from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

### Step 4: Test Database Connection

After testing the factory, we will test the database connection. These tests ensure that the database connection is established and closed as expected.

Here is the code to add in `tests/test_db.py`:

```python
# tests/test_db.py

import sqlite3
import pytest
from flaskr.db import get_db

def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')

    assert 'closed' in str(e.value)
```

### Step 5: Test Authentication

Next, we will write tests for user authentication. These tests ensure that users can log in and log out as expected, and that appropriate error messages are displayed when necessary.

Here is the code to add in `tests/test_auth.py`:

```python
# tests/test_auth.py

import pytest
from flask import g, session
from flaskr.db import get_db

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'
```

### Step 6: Test Blog Posts

Finally, we will write tests for blog posts. These tests ensure that users can create, update, and delete blog posts as expected.

Here is the code to add in `tests/test_blog.py`:

```python
# tests/test_blog.py

import pytest
from flaskr.db import get_db

def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2
```

### Step 7: Run the Tests

Now that we have written our tests, we can run them using the `pytest` command:

```bash
pytest
```

To measure the code coverage of your tests, use the `coverage` command to run pytest:

```bash
coverage run -m pytest
```

You can view a simple coverage report in the terminal with the following command:

```bash
coverage report
```

## Summary

In this lab, we have learnt how to write unit tests for a Flask application using `pytest` and `coverage`. These tools help us ensure our application works as expected and identify areas that need improvement. Writing tests for your code is a good practice as it helps you catch bugs before they become a problem.
