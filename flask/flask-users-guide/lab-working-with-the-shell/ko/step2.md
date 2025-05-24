# 요청 컨텍스트 생성하기

쉘에서 적절한 요청 컨텍스트를 생성하려면 `test_request_context()` 메서드를 사용하십시오. 이 메서드는 `RequestContext` 객체를 생성합니다. 쉘에서는 `push()` 및 `pop()` 메서드를 사용하여 요청 컨텍스트를 수동으로 푸시 (push) 하고 팝 (pop) 합니다.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()

# Push the request context
ctx.push()

# Work with the request object

# Pop the request context
ctx.pop()
```
