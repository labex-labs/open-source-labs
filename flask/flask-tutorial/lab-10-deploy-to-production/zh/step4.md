# 使用生产服务器运行应用程序

对于生产环境，你应该使用 WSGI 服务器而不是内置的开发服务器。我们将使用 Waitress 作为我们的 WSGI 服务器。

首先，安装 Waitress：

```bash
# 安装Waitress
pip install waitress
```

现在，告诉 Waitress 来运行你的应用程序：

```bash
# 使用Waitress运行应用程序
waitress-serve --call 'flaskr:create_app'
```
