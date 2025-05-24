# Configurar a Aplicação Flask

Antes de podermos executar o servidor de desenvolvimento, precisamos configurar uma aplicação Flask. Crie um novo arquivo Python chamado `app.py` e adicione o seguinte código:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == "__main__":
    app.run(debug=True)
```

Neste código, criamos uma aplicação Flask e definimos uma rota que retorna uma simples mensagem "Hello, Flask!". O bloco `if __name__ == "__main__":` garante que a aplicação Flask seja executada apenas quando o script for executado diretamente, e não quando for importado como um módulo.
