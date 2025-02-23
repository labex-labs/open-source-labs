# Создание контекста запроса

Для создания правильного контекста запроса в оболочке используйте метод `test_request_context()`, который создает объект `RequestContext`. В оболочке вручную нажмите и отпустите контекст запроса с использованием методов `push()` и `pop()`.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Создайте контекст запроса
ctx = app.test_request_context()

# Нажмите контекст запроса
ctx.push()

# Работайте с объектом запроса

# Отпустите контекст запроса
ctx.pop()
```
