# 从文件中配置

在代码中硬编码配置值并不理想，尤其是对于敏感信息。Flask 提供了一种从单独文件加载配置的方法。创建一个名为 `config.py` 的新文件，并添加以下代码：

```python
DEBUG = False
SECRET_KEY ='myothersecretkey'
```

在 `app.py` 文件中，将之前的配置代码替换为以下内容：

```python
app.config.from_object('config')
```

`from_object` 方法从 `config` 模块加载配置。现在，`DEBUG` 和 `SECRET_KEY` 值将从 `config.py` 文件中加载。

重启 Flask 应用，然后访问 `http://localhost:5000` 以查看包含新配置值的更新后的消息。
