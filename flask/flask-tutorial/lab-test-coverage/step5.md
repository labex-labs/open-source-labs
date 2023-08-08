# Test Authentication

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
