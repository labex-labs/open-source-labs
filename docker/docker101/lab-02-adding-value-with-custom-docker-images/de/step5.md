# Deploying a Change

Die "Hello World!"-Anwendung wird überbewertet. Lassen Sie uns die App aktualisieren, sodass sie stattdessen "Hello Beautiful World!" sagt.

## Update `app.py`

Ersetzen Sie die Zeichenfolge "Hello World" durch "Hello Beautiful World!" in `app.py`. Sie können die Datei mit dem folgenden Befehl aktualisieren. (Kopieren und Einfügen des gesamten Codeblocks)

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## Rebuild and Push Your Image

Jetzt, da Ihre App aktualisiert ist, müssen Sie die obigen Schritte wiederholen, um Ihre App neu zu bauen und sie an den Docker Hub-Registrierungsdienst zu pushen.

Zuerst bauen Sie erneut, diesmal verwenden Sie Ihren Docker Hub-Benutzernamen im Build-Befehl:

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world.
```

Beachten Sie die "Using cache" für Schritte 1-3. Diese Schichten des Docker-Images wurden bereits gebaut, und `docker image build` wird diese Schichten aus dem Cache verwenden, anstatt sie erneut zu bauen.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Es gibt auch einen Caching-Mechanismus für das Pushen von Schichten. Der Docker Hub hat bereits alle Schichten außer einer aus einem früheren Push, daher pusht er nur die eine geänderte Schicht.

Wenn Sie eine Schicht ändern, müssen alle darauf aufgebauten Schichten erneut gebaut werden. Jede Zeile in einer Dockerfile baut eine neue Schicht auf, die auf der Schicht basiert, die aus den Zeilen zuvor erstellt wurde. Deshalb ist die Reihenfolge der Zeilen in unserer Dockerfile wichtig. Wir haben unsere Dockerfile optimiert, sodass die Schicht, die am wahrscheinlichsten geändert wird (`COPY app.py /app.py`), die letzte Zeile der Dockerfile ist. Im Allgemeinen ändert sich für eine Anwendung Ihr Code am häufigsten. Diese Optimierung ist besonders wichtig für CI/CD-Prozesse, bei denen Sie möchten, dass Ihre Automatisierung so schnell wie möglich läuft.
