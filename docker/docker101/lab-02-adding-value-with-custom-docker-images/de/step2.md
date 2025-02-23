# Erstellen und Bauen des Docker-Images

Was passiert, wenn Sie Python lokal nicht installiert haben? Keine Sorge! Denn Sie brauchen es nicht. Einer der Vorteile der Verwendung von Containern ist, dass Sie Python innerhalb Ihrer Container bauen können, ohne Python auf Ihrem Hostcomputer zu installieren.

Erstellen Sie eine `Dockerfile`, indem Sie folgenden Befehl ausführen. (Kopieren und Einfügen des gesamten Codeblocks)

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Eine Dockerfile listet die Anweisungen auf, die erforderlich sind, um ein Docker-Image zu erstellen. Gehen wir Zeile für Zeile durch die obige Datei.

**FROM python:3.8-alpine**
Dies ist der Ausgangspunkt für Ihre Dockerfile. Jede Dockerfile muss mit einer `FROM`-Zeile beginnen, die das Ausgangsimage ist, auf dem Sie Ihre Schichten aufbauen.

In diesem Fall wählen wir die `python:3.8-alpine`-Basis-Schicht (siehe [Dockerfile für python3.8/alpine3.12](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)), da es bereits die Version von Python und pip hat, die wir benötigen, um unsere Anwendung auszuführen.

Die `alpine`-Version bedeutet, dass es die [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux)-Verteilung verwendet, die erheblich kleiner als viele alternative Linux-Flavoren ist, ca. 8 MB groß, während eine minimale Installation auf der Festplatte ca. 130 MB sein könnte. Ein kleineres Image bedeutet, dass es viel schneller heruntergeladen (deployed) wird, und es hat auch Vorteile für die Sicherheit, da es eine kleinere Angriffsfläche hat. [Alpine Linux](https://alpinelinux.org/downloads/) ist eine Linux-Verteilung, die auf musl und BusyBox basiert.

Wir verwenden hier das "3.8-alpine"-Tag für das Python-Image. Schauen Sie sich die verfügbaren Tags für das offizielle Python-Image auf dem [Docker Hub](https://hub.docker.com/_/python/) an. Es ist eine bewährte Praxis, einen spezifischen Tag zu verwenden, wenn Sie ein Elternimage erben, um die Änderungen an der Elternabhängigkeit zu kontrollieren. Wenn kein Tag angegeben wird, tritt der "latest"-Tag in Kraft, der als dynamischer Zeiger fungiert, der auf die neueste Version eines Images zeigt.

Aus Sicherheitsgründen ist es sehr wichtig, die Schichten zu verstehen, auf denen Sie Ihr Docker-Image aufbauen. Aus diesem Grund wird dringend empfohlen, nur "offizielle" Images aus dem [docker hub](https://hub.docker.com/) oder nicht-Community-Images aus dem docker-store zu verwenden. Diese Images werden [überprüft](https://docs.docker.com/docker-hub/official_repos/), um bestimmte Sicherheitsanforderungen zu erfüllen, und haben auch sehr gute Dokumentationen für die Benutzer zu folgen. Sie können weitere Informationen zu diesem [Python-Basisimage](https://hub.docker.com/_/python), sowie allen anderen Images, die Sie verwenden können, auf dem [docker hub](https://hub.docker.com) finden.

Für eine komplexere Anwendung können Sie möglicherweise die Verwendung eines `FROM`-Images benötigen, das höher in der Kette steht. Beispielsweise beginnt die Eltern-[Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) für unsere Python-Anwendung mit `FROM alpine`, und gibt dann eine Reihe von `CMD`- und `RUN`-Anweisungen für das Image an. Wenn Sie eine feinere Kontrolle benötigen, können Sie mit `FROM alpine` (oder einer anderen Verteilung) beginnen und diese Schritte selbst ausführen. Um zu beginnen, empfehle ich jedoch, ein offizielles Image zu verwenden, das Ihren Anforderungen möglichst genau entspricht.

**RUN pip install flask**
Der `RUN`-Befehl führt die erforderlichen Befehle aus, um Ihr Image für Ihre Anwendung einzurichten, wie z. B. das Installieren von Paketen, das Bearbeiten von Dateien oder das Ändern von Dateiberechtigungen. In diesem Fall installieren wir flask. Die `RUN`-Befehle werden zur Build-Zeit ausgeführt und werden zu den Schichten Ihres Images hinzugefügt.

**CMD ["python","app.py"]**
`CMD` ist der Befehl, der ausgeführt wird, wenn Sie einen Container starten. Hier verwenden wir `CMD`, um unsere Python-Anwendung auszuführen.

Es kann nur ein `CMD` pro Dockerfile geben. Wenn Sie mehr als einen `CMD` angeben, wird der letzte `CMD` wirksam. Die Eltern `python:3.8-alpine` gibt auch einen `CMD` (`CMD python3`) an. Sie können die Dockerfile für das offizielle `python:alpine`-Image [hier](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) finden.

Sie können das offizielle Python-Image direkt verwenden, um Python-Skripte auszuführen, ohne Python auf Ihrem Host zu installieren. Heute erstellen wir jedoch ein benutzerdefiniertes Image, um unsere Quelle zu integrieren, damit wir ein Image mit unserer Anwendung erstellen und es an andere Umgebungen weitergeben können.

**COPY app.py /app.py**
Dies kopiert die `app.py` im lokalen Verzeichnis (wo Sie `docker image build` ausführen werden) in eine neue Schicht des Images. Diese Anweisung ist die letzte Zeile in der Dockerfile. Schichten, die häufig geändert werden, wie das Kopieren von Quellcode in das Image, sollten am Ende der Datei platziert werden, um vollkommen von der Docker-Schichtcache zu profitieren. Dies ermöglicht es uns, die Neuerstellung von Schichten zu vermeiden, die anderweitig gecacht werden könnten. Wenn beispielsweise eine Änderung in der `FROM`-Anweisung erfolgt, wird der Cache für alle nachfolgenden Schichten dieses Images ungültig. Wir werden dies später in diesem Lab demonstrieren.

Es scheint gegen die Intuition zu verlaufen, dies nach der `CMD ["python","app.py"]`-Zeile zu platzieren. Denken Sie daran, die `CMD`-Zeile wird erst beim Starten des Containers ausgeführt, so dass wir hier keinen `file not found`-Fehler erhalten.

Und so haben Sie es: eine sehr einfache Dockerfile. Eine vollständige Liste der Befehle, die Sie in eine Dockerfile einfügen können, finden Sie [hier](https://docs.docker.com/engine/reference/builder/). Jetzt, da wir unsere Dockerfile definiert haben, verwenden wir es, um unser benutzerdefiniertes Docker-Image zu erstellen.

Bauen Sie das Docker-Image.

Geben Sie `-t` ein, um Ihr Image als `python-hello-world` zu benennen.

```bash
docker image build -t python-hello-world.
```

Vergewissern Sie sich, dass Ihr Image in Ihrer Imageliste angezeigt wird.

```bash
docker image ls
```

**Hinweis**: Ihr Basisimage `python:3.8-alpine` ist ebenfalls in Ihrer Liste.

Sie können einen History-Befehl ausführen, um die Geschichte eines Images und seiner Schichten anzuzeigen,

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
