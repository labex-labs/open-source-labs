# 跨站脚本攻击（XSS）

跨站脚本攻击（XSS）是一种漏洞，攻击者可借此将恶意脚本注入用户查看的网页中。要在 Flask 中防止 XSS 攻击，请遵循以下准则：

- 始终对文本进行转义，以防止包含任意 HTML 标签。
- 在没有 Jinja2 模板帮助的情况下生成 HTML 时要谨慎。
- 使用 `Markup` 类对用户提交的数据进行转义。
- 避免从上传的文件中发送 HTML 或文本文件。

示例代码：

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

要运行此代码，请将其保存在名为 `app.py` 的文件中，并执行命令 `flask run`。
