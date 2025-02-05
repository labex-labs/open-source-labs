# 创建一个Flask应用程序

创建一个名为`app.py`的新文件，并导入必要的模块：

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

在这段代码中，我们创建了一个新的Flask应用程序，并为根URL（“/”）定义了一个路由。当用户访问根URL时，`index()`函数将被调用，它将渲染`index.html`模板。
