# Configurando a Application Factory (Fábrica de Aplicação)

Em seguida, crie um arquivo `__init__.py` no diretório `flaskr`. Este arquivo serve a dois propósitos: ele conterá a application factory (fábrica de aplicação) e sinaliza ao Python que o diretório `flaskr` deve ser tratado como um pacote.

No seu arquivo `__init__.py`, importe os módulos necessários e defina uma função, `create_app()`, que irá instanciar e configurar sua aplicação.

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # More code to be added here...

    return app
```
