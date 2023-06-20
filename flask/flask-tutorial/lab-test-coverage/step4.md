# Writing Tests for the Factory

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
