# Crea una aplicación de `Python` (sin usar Docker)

Ejecuta el siguiente comando para crear un archivo llamado `app.py` con un programa de Python simple. (Copiar y pegar todo el bloque de código)

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

Esta es una simple aplicación de Python que utiliza Flask para exponer un servidor web HTTP en el puerto 5000 (5000 es el puerto predeterminado de Flask). No te preocupes si no estás muy familiarizado con Python o Flask, estos conceptos se pueden aplicar a una aplicación escrita en cualquier lenguaje.

**Opcional**: Si tienes Python y pip instalados, puedes ejecutar esta aplicación localmente. Si no, pasa al siguiente paso.

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

Abre la aplicación en una nueva pestaña del navegador usando `http://0.0.0.0:5000/`.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
