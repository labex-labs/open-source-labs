# Ausführen des Docker-Images

Jetzt, da Sie das Image gebaut haben, können Sie es ausführen, um zu überprüfen, ob es funktioniert.

Führen Sie das Docker-Image aus

```bash
docker run -p 5001:5000 -d python-hello-world
```

Das `-p`-Flag bildet einen Port, der innerhalb des Containers läuft, auf Ihren Host ab. In diesem Fall bilden wir den Python-Anwendung, die auf Port 5000 innerhalb des Containers läuft, auf Port 5001 Ihres Hosts ab. Beachten Sie, dass, wenn Port 5001 bereits von einer anderen Anwendung auf Ihrem Host verwendet wird, Sie möglicherweise 5001 durch einen anderen Wert wie 5002 ersetzen müssen.

Navigieren Sie zum Tab **PORTS** im Terminalfenster und klicken Sie auf den Link, um die App in einem neuen Browser-Tab zu öffnen.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

Führen Sie in einem Terminal `curl localhost:5001` aus, was `hello world!` zurückgibt.

Überprüfen Sie die Logausgabe des Containers.

Wenn Sie die Logs Ihrer Anwendung sehen möchten, können Sie den Befehl `docker container logs` verwenden. Standardmäßig druckt `docker container logs` die Ausgabe aus, die von Ihrer Anwendung an die Standardausgabe gesendet wird. Verwenden Sie `docker container ls`, um die ID Ihres laufenden Containers zu finden.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Die Dockerfile ist die Methode, um reproduzierbare Builds für Ihre Anwendung zu erstellen. Ein üblicher Workflow besteht darin, dass Ihre CI/CD-Automatisierung `docker image build` als Teil ihres Buildprozesses ausführt. Sobald die Bilder gebaut sind, werden sie an einen zentralen Registrierungsdienst gesendet, von dem alle Umgebungen (wie eine Testumgebung), die Instanzen dieser Anwendung ausführen müssen, darauf zugreifen können. Im nächsten Schritt werden wir unser benutzerdefiniertes Image in den öffentlichen Docker-Registrydienst: den Docker Hub pushen, wo es von anderen Entwicklern und Betreibern verwendet werden kann.
