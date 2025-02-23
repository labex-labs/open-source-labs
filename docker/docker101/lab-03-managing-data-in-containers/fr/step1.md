# Volumes

Un `data volume` ou `volume` est un répertoire qui circule le `Union File System` de Docker.

Il existe trois types de volumes :

- volume anonyme,
- volume nommé, et
- volume hôte.

## Volume anonyme

Créons une instance d'une base de données NoSQL open source populaire appelée CouchDB et utilisons un `volume anonyme` pour stocker les fichiers de données de la base de données.

Pour exécuter une instance de CouchDB, utilisez l'image CouchDB sur Docker Hub à [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). Les docs disent que la valeur par défaut pour CouchDB est d'`écrire les fichiers de base de données sur le disque du système hôte en utilisant sa propre gestion de volume interne`.

Exécutez la commande suivante :

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB créera un volume anonyme et générera un nom haché. Vérifiez les volumes sur votre système hôte :

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Définissez une variable d'environnement `VOLUME` avec la valeur du nom généré :

```bash
export VOLUME=<VOLUME NAME>
```

Et inspectez le volume qui a été créé, utilisez le nom haché généré pour le volume :

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

Vous voyez que Docker a créé et gère un volume dans le système de fichiers hôte Docker sous `/var/lib/docker/volumes/$VOLUME_NAME/_data`. Notez que ce n'est pas un chemin sur la machine hôte, mais une partie du système de fichiers géré par Docker.

Créez une nouvelle base de données `mydb` et insérez un nouveau document avec un message `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Arrêtez le conteneur et redémarrez le conteneur :

```bash
docker stop my-couchdb
docker start my-couchdb
```

Récupérez le document dans la base de données pour tester que les données ont été conservées.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

Sortie :

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Partage de volumes

Vous pouvez partager un volume anonyme avec un autre conteneur en utilisant l'option `--volumes-from`.

Créez un conteneur `busybox` avec un volume anonyme monté sur un répertoire `/data` dans le conteneur et, en utilisant des commandes shell, écrivez un message dans un fichier de journal.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Vérifiez que le conteneur `busybox1` est arrêté mais pas supprimé.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

Ensuite, créez un deuxième conteneur `busybox` nommé `busybox2` en utilisant l'option `--volumes-from` pour partager le volume créé par `busybox1` :

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

Docker a créé le volume anonyme que vous avez pu partager en utilisant l'option `--volumes-from` et a créé un nouveau volume anonyme.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Nettoyez les volumes et les conteneurs existants.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Volume nommé

Un `volume nommé` et un `volume anonyme` sont similaires en ce sens que Docker gère où ils sont situés. Cependant, un `volume nommé` peut être référencé par son nom lors de son montage sur un répertoire de conteneur. Cela est utile si vous voulez partager un volume entre plusieurs conteneurs.

Tout d'abord, créez un `volume nommé` :

```bash
docker volume create my-couchdb-data-volume
```

Vérifiez que le volume a été créé :

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

Maintenant, créez le conteneur CouchDB nommé `my-couchdb-name-vol` en utilisant le `volume nommé` :

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Attendez que le conteneur CouchDB soit en cours d'exécution et que l'instance soit disponible.

Créez une nouvelle base de données `mydb` et insérez un nouveau document avec un message `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

Il est maintenant facile de partager le volume avec un autre conteneur. Par exemple, lisez le contenu du volume en utilisant l'image `busybox` et partagez le volume `my-couchdb-data-volume` en montant le volume sur un répertoire dans le conteneur `busybox`.

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

Vous pouvez vérifier le système de fichiers géré par Docker pour les volumes en exécutant un conteneur `busybox` avec des autorisations privilégiées et en définissant l'identifiant de processus sur `host` pour inspecter le système hôte et naviguer vers les répertoires gérés par Docker.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Nettoyage :

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Volume hôte

Lorsque vous voulez accéder facilement au répertoire de volume depuis la machine hôte directement au lieu d'utiliser les répertoires gérés par Docker, vous pouvez créer un `volume hôte`.

Utilisons un répertoire dans le répertoire de travail actuel (indiqué avec la commande `pwd`) appelé `data`, ou choisissez votre propre répertoire de données sur la machine hôte, par exemple `/home/couchdb/data`. Nous laissons Docker créer le répertoire `$(pwd)/data` s'il n'existe pas encore. Nous montons le `volume hôte` à l'intérieur du conteneur CouchDB sur le répertoire de conteneur `/opt/couchdb/data`, qui est le répertoire de données par défaut pour CouchDB.

Exécutez la commande suivante :

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Vérifiez qu'un répertoire `data` a été créé :

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

et que CouchDB a créé des fichiers de données ici :

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

Vérifiez également qu'aucun volume géré n'a été créé par docker, car nous utilisons maintenant un `volume hôte`.

```bash
docker volume ls
```

et

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

Créez une nouvelle base de données `mydb` et insérez un nouveau document avec un message `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Notez que CouchDB a créé un dossier `shards` :

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

Liste le contenu du répertoire `shards` :

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

et le premier shard :

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

Un [shard](https://docs.couchdb.org/en/stable/cluster/sharding.html) est une partition horizontale des données dans une base de données. La partitionnement des données en shards et la distribution des copies de chaque shard sur différents nœuds dans un cluster confère une plus grande durabilité aux données face à la perte d'un nœud. CouchDB sharde automatiquement les bases de données et distribue les sous-ensembles de documents entre les nœuds.

Nettoyage :

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
