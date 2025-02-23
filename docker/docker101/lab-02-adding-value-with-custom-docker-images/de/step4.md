# Push to a Central Registry

Navigieren Sie zu [Docker Hub](https://hub.docker.com) und erstellen Sie ein Konto, wenn Sie es noch nicht getan haben. Alternativ können Sie auch [https://quay.io](https://quay.io) verwenden, zum Beispiel.

Für dieses Lab verwenden wir den Docker Hub als unseren zentralen Registrierungsdienst. Der Docker Hub ist ein kostenloser Dienst, um öffentlich verfügbare Bilder zu speichern, oder Sie können bezahlen, um private Bilder zu speichern. Gehen Sie zur [Docker Hub](https://hub.docker.com)-Website und erstellen Sie ein kostenloses Konto.

Die meisten Organisationen, die stark Docker verwenden, werden intern ihren eigenen Registrierungsdienst einrichten. Um die Dinge zu vereinfachen, verwenden wir den Docker Hub, aber die folgenden Konzepte gelten für jeden Registrierungsdienst.

Anmeldung

Sie können sich bei Ihrem Imagerregistrierungskonto anmelden, indem Sie `docker login` in Ihrem Terminal eingeben, oder wenn Sie Podman verwenden, geben Sie `podman login` ein.

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Password:
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

Bezeichnen Sie Ihr Image mit Ihrem Benutzernamen

Die Docker Hub-Namenskonvention besteht darin, Ihr Image mit [dockerhub Benutzername]/[Image Name] zu bezeichnen. Dazu werden wir unser zuvor erstelltes Image `python-hello-world` so bezeichnen, dass es diesem Format entspricht.

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

Pushen Sie Ihr Image an den Registrierungsdienst

Sobald wir ein richtig bezeichnetes Image haben, können wir den Befehl `docker push` verwenden, um unser Image an den Docker Hub-Registrierungsdienst zu pushen.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

Überprüfen Sie Ihr Image im Browser auf dem Docker Hub

Navigieren Sie zu [Docker Hub](https://hub.docker.com) und wechseln Sie zu Ihrem Profil, um Ihr neu hochgeladenes Image unter `https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world` zu sehen.

Jetzt, da Ihr Image auf dem Docker Hub ist, können andere Entwickler und Betreiber den Befehl `docker pull` verwenden, um Ihr Image in andere Umgebungen bereitzustellen.

**Hinweis**: Docker-Images enthalten alle Abhängigkeiten, die erforderlich sind, um eine Anwendung innerhalb des Images auszuführen. Dies ist nützlich, da wir keine Umgebungsabweichungen (Versionsunterschiede) mehr berücksichtigen müssen, wenn wir von Abhängigkeiten abhängen, die auf jeder Umgebung installiert sind, auf die wir bereitstellen. Wir müssen auch keine zusätzlichen Schritte durchführen, um diese Umgebungen bereitzustellen. Ein einziger Schritt: Installieren Sie Docker, und Sie sind fertig.
