# Configurar la aplicación Flask

Antes de poder ejecutar el servidor de desarrollo, necesitamos configurar una aplicación Flask. Cree un nuevo archivo de Python llamado `app.py` y agregue el siguiente código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

En este código, creamos una aplicación Flask y definimos una ruta que devuelve un simple mensaje "Hello, Flask!". El bloque `if __name__ == "__main__":` asegura de que la aplicación Flask solo se ejecute cuando se ejecuta el script directamente, no cuando se importa como un módulo.
