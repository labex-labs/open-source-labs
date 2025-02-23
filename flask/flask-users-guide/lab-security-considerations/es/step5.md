# Opciones de Set-Cookie

Al configurar cookies en Flask, es importante considerar opciones de seguridad para proteger datos sensibles. Algunas opciones recomendadas son:

- Secure: Limita las cookies solo al tráfico HTTPS.
- HttpOnly: Protege el contenido de las cookies para que no se pueda leer con JavaScript.
- SameSite: Restringe cómo se envían las cookies con solicitudes de sitios externos.

Código de ejemplo:

```python
# app.py

from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('Hello, world!')
    response.set_cookie('username', 'flask', secure=True, httponly=True, samesite='Lax')
    return response

if __name__ == '__main__':
    app.run()
```

Para ejecutar el código, guárdelo en un archivo llamado `app.py` y ejecute el comando `flask run`.
