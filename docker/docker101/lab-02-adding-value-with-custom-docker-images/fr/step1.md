# Créer une application `Python` (sans utiliser Docker)

Exécutez la commande suivante pour créer un fichier nommé `app.py` avec un programme Python simple. (Copiez/collez le bloc de code entier)

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

Il s'agit d'une simple application Python qui utilise Flask pour exposer un serveur web HTTP sur le port 5000 (5000 est le port par défaut pour Flask). Ne vous inquiétez pas si vous n'êtes pas très familier avec Python ou Flask, ces concepts peuvent s'appliquer à une application écrite dans n'importe quelle langue.

**Facultatif** : Si vous avez Python et pip installés, vous pouvez exécuter cette application localement. Sinon, passez à l'étape suivante.

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

Ouvrez l'application dans un nouvel onglet de navigateur en utilisant `http://0.0.0.0:5000/`.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
