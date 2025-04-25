# Set-Cookie 选项

在 Flask 中设置 Cookie 时，考虑安全选项以保护敏感数据非常重要。一些推荐的选项如下：

- Secure：将 Cookie 限制为仅通过 HTTPS 流量传输。
- HttpOnly：保护 Cookie 的内容不被 JavaScript 读取。
- SameSite：限制从外部站点发送请求时如何发送 Cookie。

示例代码：

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

要运行此代码，请将其保存在名为 `app.py` 的文件中，并执行命令 `flask run`。
