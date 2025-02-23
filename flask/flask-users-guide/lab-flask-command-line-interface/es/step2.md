# Crear una aplicación Flask

Cree un nuevo archivo de Python llamado `app.py` y agregue el siguiente código para crear una aplicación Flask básica:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Guarde el archivo y ejecútelo usando el siguiente comando en su terminal:

```
python app.py
```
