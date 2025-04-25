# 向 Flask 应用程序注册命令

要通过 Flask CLI 使你的自定义命令可用，你需要将它们注册到你的 Flask 应用程序中。打开 `app.py` 文件并按如下方式修改：

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

保存文件并使用 `flask run` 命令重启 Flask 开发服务器。现在你可以从命令行执行你的自定义命令 `greet`：

```
flask greet John
```

你应该会在终端中看到“Hello, John!”这条消息被打印出来。
