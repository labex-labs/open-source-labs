# 设置应用程序工厂

接下来，在 `flaskr` 目录中创建一个 `__init__.py` 文件。此文件有两个作用：它将包含应用程序工厂，并且向 Python 表明 `flaskr` 目录应被视为一个包。

在你的 `__init__.py` 文件中，导入必要的模块并定义一个函数 `create_app()`，该函数将实例化并配置你的应用程序。

```python
# flaskr/__init__.py

import os
from flask import Flask

def create_app(test_config=None):
    # 创建并配置应用程序
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # 更多代码将在此处添加...

    return app
```
