# Criando um Contexto de Requisição

Para criar um contexto de requisição adequado no shell, use o método `test_request_context()`, que cria um objeto `RequestContext`. No shell, faça o push e o pop manualmente do contexto de requisição usando os métodos `push()` e `pop()`.

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
