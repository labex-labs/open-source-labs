# 创建一个 Flask 应用程序

创建一个名为 `app.py` 的新 Python 文件，并添加以下代码以创建一个基本的 Flask 应用程序：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

保存文件，并在终端中使用以下命令执行它：

```
python app.py
```
