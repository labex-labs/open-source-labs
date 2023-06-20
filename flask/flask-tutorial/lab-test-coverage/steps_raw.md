# Test Coverage

## Introduction

In this lab, you will learn about test coverage in Flask applications. Test coverage is a measure of how much of your code is covered by your tests. It helps ensure that your code works as expected and can help identify areas of your code that are not being tested.

## Steps

### Step 1: Setting up the Test Environment

To get started, you need to set up the test environment. Install the necessary packages by running the following command:

```bash
$ pip install pytest coverage
```

### Step 2: Writing Unit Tests

Unit tests are used to check that individual parts of your code work as expected. In Flask, you can use the test client provided by Flask to simulate requests to your application and verify the response data.

You should aim to test as much of your code as possible. This includes testing different branches of your code, such as if statements, to ensure that all possible paths are covered.

### Step 3: Creating Fixtures

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

### Step 4: Writing Tests for the Factory

The factory is responsible for creating the Flask application. In this step, you will write tests for the factory to ensure that it works correctly.

Create a file named `test_factory.py` in the `tests` directory and add the following code:

```python
from flaskr import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
```

This code defines two test functions: `test_config` and `test_hello`. The `test_config` function checks that the application is correctly configured based on the configuration passed to the factory. The `test_hello` function sends a GET request to the `/hello` route and checks that the response data is "Hello, World!".

### Step 5: Writing Tests for the Database

The database is responsible for storing and retrieving data in the application. In this step, you will write tests for the database to ensure that it functions correctly.

Create a file named `test_db.py` in the `tests` directory and add the following code:

```python
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


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('flaskr.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called
```

This code defines two test functions: `test_get_close_db` and `test_init_db_command`. The `test_get_close_db` function checks that the `get_db` function returns the same connection within an application context and raises an error when accessed outside of the context. The `test_init_db_command` function checks that the `init-db` command calls the `init_db` function and outputs the expected message.

### Step 6: Writing Tests for Authentication

Authentication is responsible for user login and registration. In this step, you will write tests for the authentication views to ensure that they function correctly.

Create a file named `test_auth.py` in the `tests` directory and add the following code:

```python
import pytest
from flask import g, session
from flaskr.db import get_db


def test_register(client, app):
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert response.headers["Location"] == "/auth/login"

    with app.app_context():
        assert get_db().execute(
            "SELECT * FROM user WHERE username = 'a'",
        ).fetchone() is not None


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Username is required.'),
    ('a', '', b'Password is required.'),
    ('test', 'test', b'already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers["Location"] == "/"

    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'a', b'Incorrect password.'),
))
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data


def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session
```

This code defines six test functions: `test_register`, `test_register_validate_input`, `test_login`, `test_login_validate_input`, `test_logout`. These functions test the registration, login, and logout functionality of the application, as well as validation of input data.

### Step 7: Writing Tests for the Blog Views

The blog views are responsible for displaying and managing blog posts. In this step, you will write tests for the blog views to ensure that they function correctly.

Create a file named `test_blog.py` in the `tests` directory and add the following code:

```python
import pytest
from flaskr.db import get_db


def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test title' in response.data
    assert b'by test on 2018-01-01' in response.data
    assert b'test\nbody' in response.data
    assert b'href="/1/update"' in response.data


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
    '/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"


def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE post SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/1/update').status_code == 403
    assert client.post('/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/1/update"' not in client.get('/').data


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, auth, path):
    auth.login()
    assert client.post(path).status_code == 404


def test_create(client, auth, app):
    auth.login()
    assert client.get('/create').status_code == 200
    client.post('/create', data={'title': 'created', 'body': ''})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM post').fetchone()[0]
        assert count == 2


def test_update(client, auth, app):
    auth.login()
    assert client.get('/1/update').status_code == 200
    client.post('/1/update', data={'title': 'updated', 'body': ''})

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post['title'] == 'updated'


@pytest.mark.parametrize('path', (
    '/create',
    '/1/update',
))
def test_create_update_validate(client, auth, path):
    auth.login()
    response = client.post(path, data={'title': '', 'body': ''})
    assert b'Title is required.' in response.data


def test_delete(client, auth, app):
    auth.login()
    response = client.post('/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
        assert post is None
```

This code defines nine test functions that test the blog views. These functions test the index page, login required, author required, exists required, create, update, delete views, as well as validation of input data.

### Step 8: Running the Tests

To run the tests, use the following command:

```bash
$ pytest
```

This will run all the test functions you've written and display the results. If any tests fail, pytest will show the error that was raised.

To measure the code coverage of your tests, use the following command:

```bash
$ coverage run -m pytest
```

This will run pytest with coverage measurement enabled. You can then generate a coverage report by running the following command:

```bash
$ coverage report
```

This will display a report showing the coverage of your code.

### Summary

In this lab, you learned about test coverage in Flask applications. You wrote unit tests for different parts of the application, including the factory, database, authentication, and blog views. You also learned how to run the tests and measure the code coverage. Test coverage is an important tool for ensuring the quality of your code and identifying areas that need improvement.
