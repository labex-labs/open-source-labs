# 卷

「数据卷」（data volume）或「卷」（volume）是绕过 Docker 的「联合文件系统」的目录。

卷有三种类型：

- 匿名卷
- 命名卷
- 主机卷

## 匿名卷

让我们创建一个流行的开源 NoSQL 数据库 CouchDB 的实例，并使用「匿名卷」来存储数据库的数据文件。

要运行 CouchDB 实例，请使用 Docker Hub 上的 CouchDB 镜像，网址为[https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb)。文档中提到，CouchDB 的默认设置是「使用其自己的内部卷管理将数据库文件写入主机系统的磁盘」。

运行以下命令：

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB 将创建一个匿名卷并生成一个哈希名称。检查主机系统上的卷：

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

设置一个环境变量`VOLUME`，其值为生成的名称：

```bash
export VOLUME=<VOLUME NAME>
```

然后检查创建的卷，使用为该卷生成的哈希名称：

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

你会看到 Docker 已经在 Docker 主机文件系统的`/var/lib/docker/volumes/$VOLUME_NAME/_data`下创建并管理了一个卷。请注意，这不是主机上的路径，而是 Docker 管理的文件系统的一部分。

创建一个新数据库`mydb`，并插入一条带有「hello world」消息的新文档。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

停止容器并再次启动：

```bash
docker stop my-couchdb
docker start my-couchdb
```

检索数据库中的文档，以测试数据是否已持久保存。

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

输出：

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## 共享卷

你可以使用`--volumes-from`选项与另一个容器共享匿名卷。

创建一个`busybox`容器，将一个匿名卷挂载到容器中的`/data`目录，并使用 shell 命令将一条消息写入日志文件。

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

确保容器`busybox1`已停止但未删除。

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

然后使用`--volumes-from`选项创建第二个名为`busybox2`的`busybox`容器，以共享`busybox1`创建的卷：

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

Docker 创建了你能够使用`--volumes-from`选项共享的匿名卷，并创建了一个新的匿名卷。

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

清理现有的卷和容器。

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## 命名卷

「命名卷」和「匿名卷」的相似之处在于，Docker 管理它们的位置。然而，「命名卷」在挂载到容器目录时可以通过名称引用。如果你想在多个容器之间共享一个卷，这会很有帮助。

首先，创建一个「命名卷」：

```bash
docker volume create my-couchdb-data-volume
```

验证卷是否已创建：

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

现在使用「命名卷」创建名为`my-couchdb-name-vol`的 CouchDB 容器：

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

等待 CouchDB 容器运行并实例可用。

创建一个新数据库`mydb`，并插入一条带有「hello world」消息的新文档。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

现在很容易与另一个容器共享该卷。例如，使用`busybox`镜像读取卷的内容，并通过将卷挂载到`busybox`容器中的一个目录来共享`my-couchdb-data-volume`卷。

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

你可以通过以特权权限运行`busybox`容器并将进程 ID 设置为`host`来检查 Docker 管理的文件系统中的卷，以检查主机系统，并浏览到 Docker 管理的目录。

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

清理：

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## 主机卷

当你希望直接从主机轻松访问卷目录，而不是使用 Docker 管理的目录时，可以创建一个「主机卷」。

让我们使用当前工作目录（通过命令`pwd`指示）中的一个名为`data`的目录，或者在主机上选择你自己的数据目录，例如`/home/couchdb/data`。如果`$(pwd)/data`目录尚不存在，我们让 Docker 创建它。我们将 CouchDB 容器内的「主机卷」挂载到容器目录`/opt/couchdb/data`，这是 CouchDB 的默认数据目录。

运行以下命令：

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

验证是否创建了一个`data`目录：

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

并且 CouchDB 已在此处创建数据文件：

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

还要检查现在 Docker 没有创建管理卷，因为我们现在使用的是「主机卷」。

```bash
docker volume ls
```

以及：

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

创建一个新数据库`mydb`，并插入一条带有「hello world」消息的新文档。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

请注意，CouchDB 创建了一个`shards`文件夹：

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

列出`shards`目录的内容：

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

以及第一个分片：

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

[分片](https://docs.couchdb.org/en/stable/cluster/sharding.html)是数据库中数据的水平分区。将数据划分为分片并将每个分片的副本分布到集群中的不同节点，可以使数据在节点丢失时具有更高的耐久性。CouchDB 会自动对数据库进行分片，并在节点之间分布文档子集。

清理：

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
