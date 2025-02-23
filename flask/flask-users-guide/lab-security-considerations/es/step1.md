# Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) es una vulnerabilidad que permite a los atacantes inyectar scripts maliciosos en las páginas web vistas por los usuarios. Para prevenir ataques XSS en Flask, siga estas pautas:

- Siempre escapen el texto para evitar la inclusión de etiquetas HTML arbitrarias.
- Tenga cuidado al generar HTML sin la ayuda de plantillas Jinja2.
- Utilice la clase `Markup` para escapar los datos enviados por el usuario.
- Evite enviar archivos HTML o de texto a partir de archivos cargados.

Código de ejemplo:

```python
# app.py

from flask import Flask, render_template_string, Markup

app = Flask(__name__)

@app.route('/')
def index():
    value = '<script>alert("XSS Attack")</script>'
    safe_value = Markup.escape(value)
    return render_template_string('<input value="{{ value }}">', value=safe_value)
```

Para ejecutar el código, guárdelo en un archivo llamado `app.py` y ejecute el comando `flask run`.
