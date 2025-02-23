# Volumes

Ein `Data Volume` oder `Volume` ist ein Verzeichnis, das das `Union File System` von Docker umgeht.

Es gibt drei Arten von Volumes:

- anonymes Volume,
- benanntes Volume und
- Host-Volume.

## Anonymes Volume

Erstellen wir eine Instanz einer beliebten Open-Source NoSQL-Datenbank namens CouchDB und verwenden ein `anonymes Volume`, um die Datenfiles für die Datenbank zu speichern.

Um eine Instanz von CouchDB auszuführen, verwenden Sie das CouchDB-Image von Docker Hub unter [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). Die Dokumentation sagt, dass der Standard für CouchDB darin besteht, `die Datenbankfiles auf dem Hostsystem auf der Festplatte mit seiner eigenen internen Volumenverwaltung zu schreiben`.

Führen Sie den folgenden Befehl aus:

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB wird ein anonymes Volume erstellen und einen hashed Namen generieren. Überprüfen Sie die Volumes auf Ihrem Hostsystem:

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Legen Sie eine Umgebungsvariable `VOLUME` mit dem Wert des generierten Namens fest:

```bash
export VOLUME=<VOLUME NAME>
```

Und überprüfen Sie das erstellte Volume. Verwenden Sie den hashed Namen, der für das Volume generiert wurde:

```bash
$ docker volume inspect $VOLUME
[
{
  "CreatedAt": "2020-09-24T14:10:07Z",
  "Driver": "local",
  "Labels": null,
  "Mountpoint": "/var/lib/docker/volumes/f543c5319ebd96b7701dc1f2d915f21b095dfb35adbb8dc851630e098d526a50/_data",
  "Name": "f543c5319ebd96b7701dc1f2d915f21b095dfb35adbb8dc851630e098d526a50",
  "Options": null,
  "Scope": "local"
}
]
```

Sie sehen, dass Docker ein Volume im Docker-Hostdateisystem unter `/var/lib/docker/volumes/$VOLUME_NAME/_data` erstellt und verwaltet. Beachten Sie, dass dies kein Pfad auf dem Hostcomputer ist, sondern ein Teil des von Docker verwalteten Dateisystems.

Erstellen Sie eine neue Datenbank `mydb` und fügen Sie ein neues Dokument mit einer `hello world`-Nachricht hinzu.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Stoppen Sie den Container und starten Sie ihn erneut:

```bash
docker stop my-couchdb
docker start my-couchdb
```

Rufen Sie das Dokument in der Datenbank ab, um zu testen, ob die Daten persistent sind.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

Ausgabe:

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Teilen von Volumes

Sie können ein anonymes Volume mit einem anderen Container teilen, indem Sie die Option `--volumes-from` verwenden.

Erstellen Sie einen `busybox`-Container mit einem anonymen Volume, das an ein Verzeichnis `/data` im Container gemounted ist, und verwenden Sie Shell-Befehle, um eine Nachricht in eine Log-Datei zu schreiben.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Stellen Sie sicher, dass der Container `busybox1` gestoppt, aber nicht entfernt ist.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

Erstellen Sie dann einen zweiten `busybox`-Container namens `busybox2`, indem Sie die Option `--volumes-from` verwenden, um das von `busybox1` erstellte Volume zu teilen:

```bash
$ docker run --rm -it --name busybox2 --volumes-from busybox1 busybox sh
/ # ls -al /data
total 12
drwxr-xr-x 2 root root 4096 Jan 23 07:20.
drwxr-xr-x 1 root root 4096 Jan 23 07:24..
-rw-r--r-- 1 root root 20 Jan 23 07:20 hi.log
/ # cat /data/hi.log
hello from busybox1
/ # exit
```

Docker erstellte das anonyme Volume, das Sie mithilfe der Option `--volumes-from` teilen konnten, und erstellte ein neues anonymes Volume.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Bereinigen Sie die vorhandenen Volumes und Container.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Benanntes Volume

Ein `benanntes Volume` und ein `anonymes Volume` sind ähnlich darin, dass Docker bestimmt, wo sie sich befinden. Ein `benanntes Volume` kann jedoch beim Mounten an ein Containerverzeichnis per Namen referenziert werden. Dies ist hilfreich, wenn Sie ein Volume über mehrere Container hinweg teilen möchten.

Erstellen Sie zunächst ein `benanntes Volume`:

```bash
docker volume create my-couchdb-data-volume
```

Vergewissern Sie sich, dass das Volume erstellt wurde:

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

Erstellen Sie nun den CouchDB-Container namens `my-couchdb-name-vol`, indem Sie das `benannte Volume` verwenden:

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Warten Sie, bis der CouchDB-Container läuft und die Instanz verfügbar ist.

Erstellen Sie eine neue Datenbank `mydb` und fügen Sie ein neues Dokument mit einer `hello world`-Nachricht hinzu.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

Es ist jetzt einfach, das Volume mit einem anderen Container zu teilen. Lesen Sie beispielsweise den Inhalt des Volumes mithilfe des `busybox`-Images und teilen Sie das `my-couchdb-data-volume`-Volume, indem Sie das Volume an ein Verzeichnis im `busybox`-Container mounten.

```bash
labex:~/ $ docker run --rm -it --name busybox -v my-couchdb-data-volume:/myvolume busybox sh
/ #
/ # ls -al /myvolume
total 40
drwxr-xr-x 4 5984 5984 4096 Jan 23 07:30.
drwxr-xr-x 1 root root 4096 Jan 23 07:31..
drwxr-xr-x 2 5984 5984 4096 Jan 23 07:29.delete
-rw-r--r-- 1 5984 5984 8388 Jan 23 07:30 _dbs.couch
-rw-r--r-- 1 5984 5984 8385 Jan 23 07:29 _nodes.couch
drwxr-xr-x 4 5984 5984 4096 Jan 23 07:30 shards
/ # exit
```

Sie können das von Docker verwaltete Dateisystem für Volumes überprüfen, indem Sie einen `busybox`-Container mit privilegierten Rechten ausführen und die Prozess-ID auf `host` setzen, um das Hostsystem zu überprüfen, und zum Docker verwalteten Verzeichnissen navigieren.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Bereinigen:

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Host-Volume

Wenn Sie das Volumedirectory direkt von der Hostmaschine aus einfach zugreifen möchten, anstatt die von Docker verwalteten Verzeichnisse zu verwenden, können Sie ein `Host-Volume` erstellen.

Verwenden Sie ein Verzeichnis im aktuellen Arbeitsverzeichnis (angegeben mit dem Befehl `pwd`), das `data` heißt, oder wählen Sie Ihr eigenes Datenverzeichnis auf der Hostmaschine, z.B. `/home/couchdb/data`. Wir lassen Docker das Verzeichnis `$(pwd)/data` erstellen, wenn es noch nicht existiert. Wir mounten das `Host-Volume` innerhalb des CouchDB-Containers an das Containerverzeichnis `/opt/couchdb/data`, das das Standarddatenverzeichnis für CouchDB ist.

Führen Sie den folgenden Befehl aus:

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Vergewissern Sie sich, dass ein Verzeichnis `data` erstellt wurde:

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

und dass CouchDB hier Datenfiles erstellt hat:

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

Überprüfen Sie auch, dass jetzt kein verwaltetes Volume von Docker erstellt wurde, da wir jetzt ein `Host-Volume` verwenden.

```bash
docker volume ls
```

und

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

Erstellen Sie eine neue Datenbank `mydb` und fügen Sie ein neues Dokument mit einer `hello world`-Nachricht hinzu.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Beachten Sie, dass CouchDB einen Ordner `shards` erstellt hat:

```bash
$ ls -al data
total 40
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 8388 Aug 29 14:15 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 shards
```

Listen Sie den Inhalt des Ordners `shards` auf:

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

und das erste Shard:

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

Ein [Shard](https://docs.couchdb.org/en/stable/cluster/sharding.html) ist eine horizontale Partition von Daten in einer Datenbank. Die Aufteilung von Daten in Shards und die Verteilung von Kopien jedes Shards auf verschiedene Knoten in einem Cluster gewährleistet eine höhere Zuverlässigkeit der Daten bei einem Knotenausfall. CouchDB shardet Datenbanken automatisch und verteilt die Teilmengen von Dokumenten zwischen den Knoten.

Bereinigen:

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
