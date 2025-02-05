# 触发请求前/后函数

通过创建请求上下文，通常在请求之前运行的代码不会被触发。要模拟请求前的功能，请调用 `preprocess_request()` 方法。这可确保数据库连接和其他资源可用。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# 创建一个请求上下文
ctx = app.test_request_context()
ctx.push()

# 模拟请求前的功能
app.preprocess_request()

# 使用请求对象

# 弹出请求上下文
ctx.pop()
```

要模拟请求后的功能，请在弹出请求上下文之前，使用一个虚拟响应对象调用 `process_response()` 方法。

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# 创建一个请求上下文
ctx = app.test_request_context()
ctx.push()

# 模拟请求前的功能
app.preprocess_request()

# 使用请求对象

# 模拟请求后的功能
app.process_response(app.response_class())

# 弹出请求上下文
ctx.pop()
```
