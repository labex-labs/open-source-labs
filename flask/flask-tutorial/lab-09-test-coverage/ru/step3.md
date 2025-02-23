# Напишите тесты для фабрики

Далее, мы напишем тесты для фабричной функции, которая отвечает за создание веб - приложения Flask. Эти тесты гарантируют, что приложение ведет себя как ожидается в зависимости от конфигурации, переданной в него.

Вот код, который нужно добавить в `tests/test_factory.py`:

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
