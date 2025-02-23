# Führen Sie mehrere Container aus

## Entdecken Sie den Docker Hub

Der [Docker Hub](https://hub.docker.com/explore/) ist das zentrale öffentliche Registrierungssystem für Docker-Images, das Community- und offizielle Images enthält.

Wenn Sie nach Images suchen, finden Sie Filter für "Docker Certified", "Verified Publisher" und "Official Images". Wählen Sie den Filter "Docker Certified", um Images zu finden, die als enterprise-fähig angesehen werden und mit dem Docker Enterprise Edition-Produkt getestet wurden. Es ist wichtig, unverifizierten Inhalt aus dem Docker Store zu vermeiden, wenn Sie eigene Images entwickeln, die in die Produktionsumgebung bereitgestellt werden sollen. Diese unverifizierten Images können Sicherheitslücken oder sogar Schadsoftware enthalten.

Im zweiten Schritt dieses Labs werden wir einige Container starten, die von verifizierten Images aus dem Docker Hub stammen: einen Nginx-Webserver und eine MongoDB-Datenbank.

## Führen Sie einen Nginx-Server aus

Lassen Sie uns einen Container mit dem [offiziellen Nginx-Image](https://hub.docker.com/_/nginx) aus dem Docker Hub starten.

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

Wir verwenden hier einige neue Flags. Das Flag `--detach` wird diesen Container im Hintergrund ausführen. Das `publish`-Flag veröffentlicht den Port 80 im Container (der Standardport für Nginx) über den Port 8080 auf unserem Host. Denken Sie daran, dass der NET-Namespace den Prozessen des Containers einen eigenen Netzwerkstack gibt. Das `--publish`-Flag ist eine Funktion, die uns ermöglicht, das Netzwerk durch den Container auf den Host zu exponieren.

Wie wissen Sie, dass Port 80 der Standardport für Nginx ist? Weil er in der [Dokumentation](https://hub.docker.com/_/nginx) auf dem Docker Hub aufgeführt ist. Im Allgemeinen ist die Dokumentation für die verifizierten Images sehr gut, und Sie sollten sich auf sie beziehen, wenn Sie Container mit diesen Images ausführen.

Wir geben auch das `--name`-Flag an, das den Container benennt. Jeder Container hat einen Namen. Wenn Sie keinen angeben, wird Ihnen Docker einen zufällig zuweisen. Die Angabe Ihres eigenen Namens erleichtert es Ihnen, spätere Befehle auf Ihrem Container auszuführen, da Sie den Namen statt der ID des Containers referenzieren können. Beispielsweise: `docker container inspect nginx` statt `docker container inspect 5e1`.

Da dies der erste Versuch ist, den Nginx-Container auszuführen, wird das Nginx-Image aus dem Docker Store heruntergeladen. Später erstellte Container aus dem Nginx-Image werden das vorhandene Image auf Ihrem Host verwenden.

Nginx ist ein leichter Webserver. Sie können den Nginx-Server auf der Registerkarte **Web 8080** der LabEx VM zugreifen. Wechseln Sie zu ihr und aktualisieren Sie die Seite, um die Ausgabe von Nginx zu sehen.

![Schritt 2 Nginx](../assets/20230829-11-16-04-BazUogDa.png)

## Führen Sie einen `mongo`-DB-Server aus

Jetzt starten wir einen MongoDB-Server. Wir werden das [offizielle MongoDB-Image](https://hub.docker.com/_/mongo) aus dem Docker Hub verwenden. Anstatt das `latest`-Tag zu verwenden (der Standard ist, wenn kein Tag angegeben wird), verwenden wir eine bestimmte Version des mongo-Images: 4.4.

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

Auch hier wird das mongo-Image aus dem Docker Store heruntergeladen, da es der erste Versuch ist, einen mongo-Container auszuführen. Wir verwenden das `--publish`-Flag, um den mongo-Port 27017 auf unserem Host zu exponieren. Wir müssen einen anderen Port als 8080 für die Hostzuordnung verwenden, da dieser Port bereits auf unserem Host exponiert ist. Wenden Sie sich erneut an die [offiziellen Dokumentationen](https://hub.docker.com/_/mongo) auf dem Docker Hub, um weitere Details zur Verwendung des mongo-Images zu erhalten.

Sehen Sie die Ausgabe von MongoDB im Webbrowser unter `0.0.0.0:8081`. Sie sollten eine Meldung sehen, die eine Warnung von MongoDB zurückgibt.

![MongoDB-Serverausgabe - Warnung](../assets/20230829-11-19-23-PkodKK48.png)

Überprüfen Sie Ihre laufenden Container mit `docker container ls`

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." Weniger als eine Sekunde ago Up 2 Sekunden 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 17 Sekunden ago Up 19 Sekunden 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 5 Minuten ago Up 5 Minuten priceless_kepler
```

Sie sollten sehen, dass Sie einen Nginx-Webserver-Container und einen MongoDB-Container auf Ihrem Host ausführen. Beachten Sie, dass wir diese Container nicht so konfiguriert haben, dass sie miteinander kommunizieren.

Sie können die Namen "nginx" und "mongo" sehen, die wir unseren Containern gegeben haben, und den zufälligen Namen (in meinem Fall "priceless_kepler"), der für den ubuntu-Container generiert wurde. Sie können auch sehen, die Portzuordnungen, die wir mit dem `--publish`-Flag angegeben haben. Für weitere Details zu diesen laufenden Containern können Sie den Befehl `docker container inspect [container id` verwenden.

Eines, das Sie vielleicht bemerken, ist, dass der mongo-Container die `docker-entrypoint`-Befehl ausführt. Dies ist der Name des ausführbaren Programms, das beim Start des Containers ausgeführt wird. Das mongo-Image erfordert einige Vorkonfiguration, bevor der Datenbankprozess gestartet wird. Sie können genau sehen, was das Skript macht, indem Sie es auf [github](https://github.com/docker-library/mongo) ansehen. Normalerweise können Sie den Link zur github-Quelle von der Bildbeschreibungsseite auf der Docker Store-Website finden.

Container sind selbst enthalten und isoliert, was bedeutet, dass wir potenzielle Konflikte zwischen Containern mit unterschiedlichen System- oder Laufzeitabhängigkeiten vermeiden können. Beispielsweise: die Bereitstellung einer App, die Java 7 verwendet, und einer anderen App, die Java 8 verwendet, auf dem gleichen Host. Oder das Ausführen mehrerer Nginx-Container, die alle Port 80 als Standardhörtport haben (wenn Sie ihn auf dem Host mit dem `--publish`-Flag exponieren, müssen die für den Host ausgewählten Ports eindeutig sein). Die Isolationsvorteile sind möglich aufgrund von Linux-Namespaces.

**Hinweis**: Sie mussten nichts auf Ihrem Host installieren (außer Docker), um diese Prozesse auszuführen! Jeder Container enthält die Abhängigkeiten, die er innerhalb des Containers benötigt, so dass Sie nichts direkt auf Ihrem Host installieren müssen.

Das Ausführen mehrerer Container auf demselben Host ermöglicht es uns, die verfügbaren Ressourcen (CPU, Arbeitsspeicher usw.) auf einem einzelnen Host optimal zu nutzen. Dies kann zu erheblichen Kosteneinsparungen für ein Unternehmen führen.

Während das direkte Ausführen von Images aus dem Docker Hub manchmal nützlich sein kann, ist es nützlicher, eigene benutzerdefinierte Images zu erstellen und auf offizielle Images als Ausgangspunkt für diese Bilder zu verweisen. Wir werden uns in Lab 2 mit dem Erstellen unserer eigenen benutzerdefinierten Images befassen.
