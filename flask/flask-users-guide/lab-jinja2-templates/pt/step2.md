# Criar uma Aplicação Flask

Crie um novo arquivo chamado `app.py` e importe os módulos necessários:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

Neste código, criamos uma nova aplicação Flask e definimos uma rota para a URL raiz ("/"). Quando um usuário visita a URL raiz, a função `index()` será chamada e renderizará o template `index.html`.
