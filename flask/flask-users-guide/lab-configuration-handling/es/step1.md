# Crea una aplicación Flask

Primero, creemos una aplicación Flask básica. Crea un archivo llamado `app.py` y agrega el siguiente código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

Para ejecutar la aplicación, ejecuta el siguiente comando en tu terminal:

```shell
python app.py
```

Abre tu navegador web y visita `http://localhost:5000` para ver el mensaje "Hello, Flask!".
