# Registrar Comandos com a Aplicação Flask

Para tornar seus comandos personalizados disponíveis através da CLI (Command Line Interface) do Flask, você precisa registrá-los com sua aplicação Flask. Abra o arquivo `app.py` e modifique-o da seguinte forma:

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

Salve o arquivo e reinicie o servidor de desenvolvimento Flask usando o comando `flask run`. Agora você pode executar seu comando personalizado `greet` a partir da linha de comando:

```
flask greet John
```

Você deverá ver a mensagem "Hello, John!" impressa no terminal.
