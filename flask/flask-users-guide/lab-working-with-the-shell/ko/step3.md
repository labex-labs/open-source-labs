# 요청 전/후 함수 실행하기

요청 컨텍스트를 생성하면 일반적으로 요청 전에 실행되는 코드가 트리거되지 않습니다. before-request 기능을 시뮬레이션하려면 `preprocess_request()` 메서드를 호출하십시오. 이렇게 하면 데이터베이스 연결 및 기타 리소스를 사용할 수 있습니다.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()
ctx.push()

# Simulate the before-request functionality
app.preprocess_request()

# Work with the request object

# Pop the request context
ctx.pop()
```

after-request 기능을 시뮬레이션하려면 요청 컨텍스트를 팝하기 전에 더미 응답 객체와 함께 `process_response()` 메서드를 호출하십시오.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Create a request context
ctx = app.test_request_context()
ctx.push()

# Simulate the before-request functionality
app.preprocess_request()

# Work with the request object

# Simulate the after-request functionality
app.process_response(app.response_class())

# Pop the request context
ctx.pop()
```
