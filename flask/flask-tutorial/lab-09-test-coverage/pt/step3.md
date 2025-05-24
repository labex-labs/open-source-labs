# Escrever Testes para a Factory

Em seguida, escreveremos testes para a função _factory_, que é responsável por criar a aplicação Flask. Estes testes garantem que a aplicação se comporte como esperado com base na configuração passada para ela.

Aqui está o código a ser adicionado em `tests/test_factory.py`:

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
