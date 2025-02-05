# 基于环境的配置

针对不同的环境（如开发、生产和测试）采用不同的配置是很常见的。Flask 允许你根据环境变量来切换配置。创建一个名为 `config_dev.py` 的新文件，并添加以下代码：

```python
DEBUG = True
SECRET_KEY = 'devsecretkey'
```

创建另一个名为 `config_prod.py` 的文件，并添加以下代码：

```python
DEBUG = False
SECRET_KEY = 'prodsecretkey'
```

在 `app.py` 文件中，将之前的配置代码替换为以下内容：

```python
import os

if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object('config_prod')
else:
    app.config.from_object('config_dev')
```

`FLASK_ENV` 环境变量用于确定环境。如果将其设置为 `'production'`，则会加载生产环境配置；否则，将加载开发环境配置。

将 `FLASK_ENV` 环境变量设置为 `'production'`，然后重启 Flask 应用。访问 `http://localhost:5000` 以查看包含生产环境配置值的更新后的消息。
