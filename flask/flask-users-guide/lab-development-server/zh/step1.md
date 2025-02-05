# 设置 Flask 应用程序

在运行开发服务器之前，我们需要设置一个 Flask 应用程序。创建一个名为 `app.py` 的新 Python 文件，并添加以下代码：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

在这段代码中，我们创建了一个 Flask 应用程序，并定义了一个路由，该路由返回一条简单的 “Hello, Flask!” 消息。`if __name__ == "__main__":` 块确保只有在直接执行脚本时才运行 Flask 应用程序，而不是在作为模块导入时运行。
