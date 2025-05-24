# Disparando Funções Before/After Request

Ao criar um contexto de requisição, o código que normalmente é executado antes de uma requisição não é acionado. Para simular a funcionalidade before-request, chame o método `preprocess_request()`. Isso garante que as conexões com o banco de dados e outros recursos estejam disponíveis.

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

Para simular a funcionalidade after-request, chame o método `process_response()` com um objeto de resposta fictício antes de fazer o pop do contexto de requisição.

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
