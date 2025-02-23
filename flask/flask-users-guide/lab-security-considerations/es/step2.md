# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) es un ataque que engaña a los usuarios para que realicen acciones no intencionadas en un sitio web. Para prevenir ataques CSRF en Flask, siga estas pautas:

- Utilice tokens de un solo uso para validar las solicitudes que modifican el contenido del servidor.
- Almacene el token en la cookie y transmítalo con los datos del formulario.
- Compare el token recibido en el servidor con el almacenado en la cookie.

Código de ejemplo:

```python
# app.py

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete_user():
    if request.method == 'POST':
        token = request.form.get('token')
        if token and token == session.get('csrf_token'):
            # Eliminar perfil de usuario
            return redirect(url_for('index'))
    return 'Solicitud no válida'

if __name__ == '__main__':
    app.run()
```

Para ejecutar el código, guárdelo en un archivo llamado `app.py` y ejecute el comando `flask run`.
