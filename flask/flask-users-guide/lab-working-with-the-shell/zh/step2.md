# 创建请求上下文

要在 shell 中创建合适的请求上下文，请使用 `test_request_context()` 方法，该方法会创建一个 `RequestContext` 对象。在 shell 中，使用 `push()` 和 `pop()` 方法手动推送和弹出请求上下文。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# 创建一个请求上下文
ctx = app.test_request_context()

# 推送请求上下文
ctx.push()

# 使用请求对象

# 弹出请求上下文
ctx.pop()
```
