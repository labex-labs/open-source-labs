# 创建一个 Flask 应用程序

首先，让我们创建一个基本的 Flask 应用程序。创建一个名为 `app.py` 的文件，并添加以下代码：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

要运行该应用程序，请在终端中执行以下命令：

```shell
python app.py
```

打开你的网页浏览器，访问 `http://localhost:5000` 以查看“Hello, Flask!”消息。
