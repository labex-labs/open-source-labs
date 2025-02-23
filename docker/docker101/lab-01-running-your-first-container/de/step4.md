# Bereinigen

Wenn Sie dieses Lab abschließen, verbleiben auf Ihrem Host eine Reihe von laufenden Containern. Lassen Sie uns diese bereinigen.

Zunächst erhalten Sie eine Liste der laufenden Container mit `docker container ls`.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." 3 Minuten ago Up 3 Minuten 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 Minuten ago Up 3 Minuten 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 Minuten ago Up 8 Minuten priceless_kepler
```

Als nächstes führen Sie `docker container stop [container id]` für jeden Container in der Liste aus. Sie können auch die Namen der Container verwenden, die Sie zuvor angegeben haben.

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**Hinweis**: Sie müssen nur so viele Ziffern der ID angeben, dass sie eindeutig ist. Drei Ziffern reichen in der Regel aus.

Entfernen Sie die gestoppten Container

`docker system prune` ist ein wirklich praktischer Befehl, um Ihr System zu bereinigen. Er wird alle gestoppten Container, nicht genutzte Volumes und Netzwerke sowie hängende Bilder entfernen.

```bash
$ docker system prune
WARNING! This will remove:
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Total reclaimed space: 12B
```
