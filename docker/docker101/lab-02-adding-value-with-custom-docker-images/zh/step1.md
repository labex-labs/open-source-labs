# 创建一个 `Python` 应用程序（不使用 Docker）

运行以下命令来创建一个名为 `app.py` 的文件，其中包含一个简单的 Python 程序。（复制粘贴整个代码块）

```bash
cd ~/project
```

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

这是一个简单的 Python 应用程序，它使用 Flask 在端口 5000 上暴露一个 HTTP 网络服务器（5000 是 Flask 的默认端口）。如果你对 Python 或 Flask 不太熟悉也不用担心，这些概念可以应用于用任何语言编写的应用程序。

**可选步骤**：如果你已经安装了 Python 和 pip，可以在本地运行此应用程序。如果没有，请继续下一步。

```bash
$ python3 --version
$ pip3 --version
$ pip3 install flask

$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

使用 `http://0.0.0.0:5000/` 在新的浏览器标签页中打开该应用程序。

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
