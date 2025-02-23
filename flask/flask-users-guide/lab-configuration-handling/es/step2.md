# Configuración básica

Ahora agreguemos algunas configuraciones básicas a nuestra aplicación Flask. En el mismo archivo `app.py`, agrega el siguiente código:

```python
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'mysecretkey'
```

La configuración `DEBUG` habilita el modo de depuración, que proporciona mensajes de error útiles durante el desarrollo. La configuración `SECRET_KEY` se utiliza para firmar de manera segura las cookies de sesión y otras necesidades relacionadas con la seguridad.

Para acceder a los valores de configuración, puede usar el diccionario `app.config`. Por ejemplo, para imprimir el valor de la `SECRET_KEY`, agrega el siguiente código a la ruta `hello`:

```python
@app.route('/')
def hello():
    secret_key = app.config['SECRET_KEY']
    return f'Hello, Flask! Secret Key: {secret_key}'
```

Reinicie la aplicación Flask y visite `http://localhost:5000` para ver el mensaje actualizado con la clave secreta.
