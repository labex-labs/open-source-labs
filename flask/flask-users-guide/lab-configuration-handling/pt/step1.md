# Criar uma Aplicação Flask

Primeiramente, vamos criar uma aplicação Flask básica. Crie um arquivo chamado `app.py` e adicione o seguinte código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'
```

Para executar a aplicação, execute o seguinte comando no seu terminal:

```shell
python app.py
```

Abra seu navegador web e visite `http://localhost:5000` para ver a mensagem "Hello, Flask!".
