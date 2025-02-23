# Erstellen einer `Python`-App (ohne Verwendung von Docker)

Führen Sie den folgenden Befehl aus, um eine Datei namens `app.py` mit einem einfachen Python-Programm zu erstellen. (Kopieren und Einfügen des gesamten Codeblocks)

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

Dies ist eine einfache Python-App, die Flask verwendet, um einen HTTP-Webserver auf Port 5000 zu exportieren (5000 ist der Standardport für Flask). Sorgen Sie sich nicht, wenn Sie nicht sehr vertraut mit Python oder Flask sind, diese Konzepte können auf eine Anwendung in jeder Sprache angewendet werden.

**Optional:** Wenn Sie Python und pip installiert haben, können Sie diese App lokal ausführen. Wenn nicht, springen Sie zum nächsten Schritt.

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

Öffnen Sie die App in einem neuen Browser-Tab mit `http://0.0.0.0:5000/`.

![Flask app browser output](../assets/20230829-13-51-38-psaOqQ42.png)
