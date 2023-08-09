# Write Tests for Factory

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
