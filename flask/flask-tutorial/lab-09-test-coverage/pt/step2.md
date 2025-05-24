# Configuração e Fixtures

Em seguida, configuraremos as _fixtures_ de teste em um arquivo chamado `conftest.py`. Uma _fixture_ é uma função que é executada antes de cada função de teste à qual ela é aplicada.

Nesta etapa, criaremos um banco de dados temporário e o preencheremos com alguns dados para teste.

Aqui está o código a ser adicionado em `tests/conftest.py`:

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
