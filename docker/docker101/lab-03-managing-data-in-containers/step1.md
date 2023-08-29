# Volumes

A `data volume` or `volume` is a directory that bypasses the `Union File System` of Docker.

There are three types of volumes:

- anonymous volume,
- named volume, and
- host volume.

## Anonymous Volume

Let's create an instance of a popular open source NoSQL database called CouchDB and use an `anonymous volume` to store the data files for the database.

To run an instance of CouchDB, use the CouchDB image from Docker Hub at [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). The docs say that the default for CouchDB is to `write the database files to disk on the host system using its own internal volume management`.

Run the following command,

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB will create an anonymous volume and generated a hashed name. Check the volumes on your host system,

```bash
$ docker volume ls
DRIVER    VOLUME NAME
local    f543c5319ebd96b7701dc1f2d915f21b095dfb35adbb8dc851630e098d526a50
```

Set an environment variable `VOLUME` with the value of the generated name,

```bash
export VOLUME=<VOLUME NAME>
```

And inspect the volume that was created, use the hash name that was generated for the volume,

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

You see that Docker has created and manages a volume in the Docker host filesystem under `/var/lib/docker/volumes/$VOLUME_NAME/_data`. Note that this is not a path on the host machine, but a part of the Docker managed filesystem.

Create a new database `mydb` and insert a new document with a `hello world` message.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Stop the container and start the container again,

```bash
docker stop my-couchdb
docker start my-couchdb
```

Retrieve the document in the database to test that the data was persisted,

```bash
$ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

$ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Sharing Volumes

You can share an anonymous volume with another container by using the `--volumes-from` option.

Create a `busybox` container with an anonymous volume mounted to a directory `/data` in the container, and using shell commands, write a message to a log file.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Make sure the container `busybox1` is stopped but not removed.

```bash
$ docker ps -a
CONTAINER ID    IMAGE    COMMAND    CREATED    STATUS    PORTS    NAMES
437fb4a271c1    busybox    "sh"    18 seconds ago    Exited (0) 4 seconds ago    busybox1
```

Then create a second `busybox` container named `busybox2` using the `--volumes-from` option to share the volume created by `busybox1`,

```bash
$ docker run --rm -it --name busybox2 --volumes-from busybox1 busybox sh
/ # ls -al /data
/ # cat /data/hi.log
hello from busybox1
/ # exit
```

Docker created the anynomous volume that you were able to share using the `--volumes-from` option, and created a new anonymous volume.

```bash
$ docker volume ls
DRIVER    VOLUME NAME
local    83a3275e889506f3e8ff12cd50f7d5b501c1ace95672334597f9a071df439493
local    f4e6b9f9568eeb165a56b2946847035414f5f9c2cad9ff79f18e800277ae1ebd
```

Cleanup the existing volumes and container.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Named Volume

A `named volume` and `anonymous volume` are similar in that Docker manages where they are located. However, a `named volume` can be referenced by name when mounting it to a container directory. This is helpful if you want to share a volume across multiple containers.

First, create a `named volume`,

```bash
docker volume create my-couchdb-data-volume
```

Verify the volume was created,

```bash
$ docker volume ls
DRIVER    VOLUME NAME
local    my-couchdb-data-volume
```

Now create the CouchDB container using the `named volume`,

```bash
docker run -d -p 5984:5984 --name my-couchdb -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Wait until the CouchDB container is running and the instance is available.

Create a new database `mydb` and insert a new document with a `hello world` message.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

It now is easy to share the volume with another container. For instance, read the content of the volume using the `busybox` image, and share the `my-couchdb-data-volume` volume by mounting the volume to a directory in the `busybox` container.

```bash
$ docker run --rm -it --name busybox -v my-couchdb-data-volume:/myvolume busybox sh
/ # ls -al /myvolume/
total 40
drwxr-xr-x    4 5984    5984    4096 Sep 24 17:11 .
drwxr-xr-x    1 root    root    4096 Sep 24 17:14 ..
drwxr-xr-x    2 5984    5984    4096 Sep 24 17:11 .delete
-rw-r--r--    1 5984    5984    8388 Sep 24 17:11 _dbs.couch
-rw-r--r--    1 5984    5984    8385 Sep 24 17:11 _nodes.couch
drwxr-xr-x    4 5984    5984    4096 Sep 24 17:11 shards
/ # exit
```

You can check the Docker managed filesystem for volumes by running a busybox container with privileged permission and set the process id to `host` to inspect the host system, and browse to the Docker managed directories.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw-------    1 root     root         32768 Nov 10 15:54 metadata.db
drwxr-xr-x    3 root     root          4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Cleanup,

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Host Volume

When you want to access the volume directory easily from the host machine directly instead of using the Docker managed directories, you can create a `host volume`.

Let's use a directory in the current working directory (indicated with the command `pwd`) called `data`, or choose your own data directory on the host machine, e.g. `/home/couchdb/data`. We let docker create the `$(pwd)/data` directory if it does not exist yet. We mount the `host volume` inside the CouchDB container to the container directory `/opt/couchdb/data`, which is the default data directory for CouchDB.

Run the following command,

```bash
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Verify that a directory `data` was created,

```bash
$ ls -al
total 20
drwxrwxr-x  3 labex labex 4096 Aug 29 14:14 .
drwxr-x--- 25 labex labex 4096 Aug 29 14:14 ..
-rw-r--r--  1 labex labex  169 Aug 29 14:04 app.py
drwxr-xr-x  3  5984  5984 4096 Aug 29 14:14 data
-rw-r--r--  1 labex labex   98 Aug 29 13:52 Dockerfile
```

and that CouchDB has created data files here,

```bash
$ ls -al data
total 32
drwxr-xr-x 3  5984  5984 4096 Aug 29 14:14 .
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 ..
-rw-r--r-- 1  5984  5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2  5984  5984 4096 Aug 29 14:14 .delete
-rw-r--r-- 1  5984  5984 8385 Aug 29 14:14 _nodes.couch
```

Also check that now, no managed volume was created by docker, because we are now using a `host volume`.

```bash
docker volume ls
```

and

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 24
-rw-------    1 root     root         32768 Nov 10 16:00 metadata.db
/ # exit
```

Create a new database `mydb` and insert a new document with a `hello world` message.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Note that CouchDB created a folder `shards`,

```bash
$ ls -al data
total 40
drwxr-xr-x 4  5984  5984 4096 Aug 29 14:15 .
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 ..
-rw-r--r-- 1  5984  5984 8388 Aug 29 14:15 _dbs.couch
drwxr-xr-x 2  5984  5984 4096 Aug 29 14:14 .delete
-rw-r--r-- 1  5984  5984 8385 Aug 29 14:14 _nodes.couch
drwxr-xr-x 4  5984  5984 4096 Aug 29 14:15 shards
```

List the content of the `shards` directory,

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

and the first shard,

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

A [shard](https://docs.couchdb.org/en/stable/cluster/sharding.html) is a horizontal partition of data in a database. Partitioning data into shards and distributing copies of each shard to different nodes in a cluster gives the data greater durability against node loss. CouchDB automatically shards databases and distributes the subsets of documents among nodes.

Cleanup,

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
