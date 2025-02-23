# Запуск функций до/после запроса

Создав контекст запроса, код, который обычно выполняется перед запросом, не срабатывает. Чтобы имитировать функциональность до запроса, вызовите метод `preprocess_request()`. Это гарантирует, что соединения с базой данных и другие ресурсы доступны.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Создайте контекст запроса
ctx = app.test_request_context()
ctx.push()

# Имитируйте функциональность до запроса
app.preprocess_request()

# Работайте с объектом запроса

# Отпустите контекст запроса
ctx.pop()
```

Чтобы имитировать функциональность после запроса, вызовите метод `process_response()` с фиктивным объектом ответа перед отпусканием контекста запроса.

```python
# File: shell.py
# Execution: python shell.py

from flask import Flask

app = Flask(__name__)

# Создайте контекст запроса
ctx = app.test_request_context()
ctx.push()

# Имитируйте функциональность до запроса
app.preprocess_request()

# Работайте с объектом запроса

# Имитируйте функциональность после запроса
app.process_response(app.response_class())

# Отпустите контекст запроса
ctx.pop()
```
