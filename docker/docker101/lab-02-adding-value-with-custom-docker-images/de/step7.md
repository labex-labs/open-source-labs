# Clean up

Das Abschluss dieses Labs führt zu einer Reihe von laufenden Containern auf Ihrem Host. Lassen Sie uns diese aufräumen.

Führen Sie `docker container stop [container id]` für jeden laufenden Container aus

Zunächst erhalten Sie eine Liste der laufenden Container mit `docker container ls`.

```bash
$ docker container ls
```

Führen Sie dann den Befehl für jeden Container in der Liste aus.

```bash
$ docker container stop <container_id>
```

Entfernen Sie die gestoppten Container

`docker system prune` ist ein wirklich praktischer Befehl, um Ihr System aufzuräumen. Er wird alle gestoppten Container, nicht genutzte Volumes und Netze sowie hängende Bilder entfernen.

```bash
$ docker system prune
WARNING! This will remove:
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Total reclaimed space: 300.3kB
```
