# Criar uma Aplicação Flask

Crie um novo arquivo Python chamado `app.py` e adicione o seguinte código para criar uma aplicação Flask básica:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run()
```

Salve o arquivo e execute-o usando o seguinte comando no seu terminal:

```
python app.py
```
