# Crear una aplicación Flask

Cree un nuevo archivo llamado `app.py` e importe los módulos necesarios:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

En este código, creamos una nueva aplicación Flask y definimos una ruta para la URL raíz ("/"). Cuando un usuario visita la URL raíz, la función `index()` se llamará y renderizará la plantilla `index.html`.
