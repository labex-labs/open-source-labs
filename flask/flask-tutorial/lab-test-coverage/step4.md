# Test Database Connection

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
