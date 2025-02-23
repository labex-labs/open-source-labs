# Registrar comandos con la aplicación Flask

Para que sus comandos personalizados estén disponibles a través de la CLI de Flask, debe registrarlos con su aplicación Flask. Abra el archivo `app.py` y modifíquelo como sigue:

```python
from flask import Flask
from commands import greet

app = Flask(__name__)
app.cli.add_command(greet)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Guarde el archivo y reinicie el servidor de desarrollo de Flask usando el comando `flask run`. Ahora puede ejecutar su comando personalizado `greet` desde la línea de comandos:

```
flask greet John
```

Debería ver el mensaje "Hello, John!" impreso en la terminal.
