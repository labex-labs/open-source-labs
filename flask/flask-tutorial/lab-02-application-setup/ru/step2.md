# Настройка фабрики приложения

Далее, создайте файл `__init__.py` в директории `flaskr`. Этот файл имеет две цели: в нем будет находиться фабрика приложения, и он сигнализирует Python, что директория `flaskr` должна быть обработана как пакет.

В файле `__init__.py` импортируйте необходимые модули и определите функцию `create_app()`, которая будет инициализировать и настраивать ваше приложение.

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
