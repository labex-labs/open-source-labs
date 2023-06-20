# Writing Tests for the Database

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
