# Creando un contexto de solicitud

Para crear un contexto de solicitud adecuado en la shell, utiliza el método `test_request_context()`, que crea un objeto `RequestContext`. En la shell, empuja y quita manualmente el contexto de solicitud utilizando los métodos `push()` y `pop()`.

```python
# Archivo: shell.py
# Ejecución: python shell.py

from flask import Flask

app = Flask(__name__)

# Crea un contexto de solicitud
ctx = app.test_request_context()

# Empuja el contexto de solicitud
ctx.push()

# Trabaja con el objeto de solicitud

# Quita el contexto de solicitud
ctx.pop()
```
