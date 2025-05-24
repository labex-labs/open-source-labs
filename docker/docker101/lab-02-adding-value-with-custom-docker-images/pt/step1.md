# Criar um App `Python` (sem usar Docker)

Execute o seguinte comando para criar um arquivo chamado `app.py` com um programa python simples. (copie e cole todo o bloco de código)

```bash
cd ~/project
```

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

Este é um aplicativo python simples que usa flask para expor um servidor web http na porta 5000 (5000 é a porta padrão para flask). Não se preocupe se você não estiver muito familiarizado com python ou flask, esses conceitos podem ser aplicados a um aplicativo escrito em qualquer linguagem.

**Opcional:** Se você tiver python e pip instalados, pode executar este aplicativo localmente. Caso contrário, vá para a próxima etapa.

```bash
$ python3 --version
$ pip3 --version
$ pip3 install flask

$ python3 app.py
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Abra o aplicativo em uma nova aba do navegador usando `http://0.0.0.0:5000/`.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
