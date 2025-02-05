# 实例文件夹

Flask 提供了一个实例文件夹，用于存储特定于某个部署的配置文件。这使你能够将特定于部署的配置与代码的其他部分分开。默认情况下，Flask 在与应用程序相同的目录中使用一个名为 `instance` 的文件夹。

在与 `app.py` 文件相同的目录中创建一个名为 `instance` 的新文件夹。在 `instance` 文件夹中，创建一个名为 `config.cfg` 的文件，并添加以下代码：

```
DEBUG = True
SECRET_KEY = 'instancekey'
```

在 `app.py` 文件中，在配置代码之前添加以下代码：

```python
app.instance_path = os.path.abspath(os.path.dirname(__file__))
app.config.from_pyfile('config.cfg')
```

`instance_path` 被设置为 `instance` 文件夹的绝对路径。`from_pyfile` 方法从实例文件夹中的 `config.cfg` 文件加载配置。

重启 Flask 应用，然后访问 `http://localhost:5000` 以查看包含实例配置值的更新后的消息。
