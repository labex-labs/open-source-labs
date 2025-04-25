# 跨站请求伪造（CSRF）

跨站请求伪造（CSRF）是一种攻击方式，它会诱使用户在网站上执行非预期的操作。要在 Flask 中防止 CSRF 攻击，请遵循以下准则：

- 使用一次性令牌来验证修改服务器内容的请求。
- 将令牌存储在 Cookie 中，并随表单数据一起传输。
- 将服务器接收到的令牌与存储在 Cookie 中的令牌进行比较。

示例代码：

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # 删除用户资料
            return redirect(url_for('index'))
    return '无效请求'

if __name__ == '__main__':
    app.run()
```

要运行此代码，请将其保存在名为 `app.py` 的文件中，并执行命令 `flask run`。
