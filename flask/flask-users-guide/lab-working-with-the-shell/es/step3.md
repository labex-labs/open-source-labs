# Activando funciones antes/demás de la solicitud

Al crear un contexto de solicitud, el código que normalmente se ejecuta antes de una solicitud no se activa. Para simular la funcionalidad antes de la solicitud, llama al método `preprocess_request()`. Esto garantiza que las conexiones a la base de datos y otros recursos estén disponibles.

```python
# Archivo: shell.py
# Ejecución: python shell.py

from flask import Flask

app = Flask(__name__)

# Crea un contexto de solicitud
ctx = app.test_request_context()
ctx.push()

# Simula la funcionalidad antes de la solicitud
app.preprocess_request()

# Trabaja con el objeto de solicitud

# Quita el contexto de solicitud
ctx.pop()
```

Para simular la funcionalidad después de la solicitud, llama al método `process_response()` con un objeto de respuesta ficticio antes de quitar el contexto de solicitud.

```python
# Archivo: shell.py
# Ejecución: python shell.py

from flask import Flask

app = Flask(__name__)

# Crea un contexto de solicitud
ctx = app.test_request_context()
ctx.push()

# Simula la funcionalidad antes de la solicitud
app.preprocess_request()

# Trabaja con el objeto de solicitud

# Simula la funcionalidad después de la solicitud
app.process_response(app.response_class())

# Quita el contexto de solicitud
ctx.pop()
```
