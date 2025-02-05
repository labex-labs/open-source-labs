# 基本配置

现在让我们为 Flask 应用添加一些基本配置。在同一个 `app.py` 文件中，添加以下代码：

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

`DEBUG` 配置启用调试模式，在开发过程中会提供有用的错误消息。`SECRET_KEY` 配置用于安全地对会话 cookie 进行签名以及满足其他与安全相关的需求。

要访问配置值，可以使用 `app.config` 字典。例如，要打印 `SECRET_KEY` 的值，在 `hello` 路由中添加以下代码：

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

重启 Flask 应用，然后访问 `http://localhost:5000` 以查看包含密钥的更新后的消息。
