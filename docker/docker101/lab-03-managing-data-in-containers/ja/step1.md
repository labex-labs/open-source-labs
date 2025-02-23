# ボリューム

「データボリューム」または「ボリューム」は、Dockerの「ユニオンファイルシステム」を迂回するディレクトリです。

ボリュームには3種類あります。

- 匿名ボリューム
- 名前付きボリューム
- ホストボリューム

## 匿名ボリューム

人気のあるオープンソースのNoSQLデータベースであるCouchDBのインスタンスを作成し、データベースのデータファイルを保存するために「匿名ボリューム」を使用しましょう。

CouchDBのインスタンスを実行するには、Docker HubのCouchDBイメージを[https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb)から使用します。ドキュメントによると、CouchDBの既定値は、「独自の内部ボリューム管理を使用して、ホストシステムのディスクにデータベースファイルを書き込む」ことです。

次のコマンドを実行します。

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDBは匿名ボリュームを作成し、ハッシュ付きの名前を生成します。ホストシステムのボリュームを確認します。

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

生成された名前の値を持つ環境変数「VOLUME」を設定します。

```bash
export VOLUME=<VOLUME NAME>
```

そして、ボリュームに生成されたハッシュ名を使用して、作成されたボリュームを調べます。

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

DockerがDockerホストファイルシステムの`/var/lib/docker/volumes/$VOLUME_NAME/_data`以下にボリュームを作成して管理していることがわかります。これは、ホストマシン上のパスではなく、Dockerが管理するファイルシステムの一部であることに注意してください。

新しいデータベース「mydb」を作成し、「hello world」のメッセージを持つ新しいドキュメントを挿入します。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

コンテナを停止し、再度起動します。

```bash
docker stop my-couchdb
docker start my-couchdb
```

データが永続化されたことをテストするために、データベース内のドキュメントを取得します。

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

出力：

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## ボリュームの共有

`--volumes-from`オプションを使用することで、匿名ボリュームを別のコンテナと共有できます。

匿名ボリュームをコンテナ内の`/data`ディレクトリにマウントした`busybox`コンテナを作成し、シェルコマンドを使用して、ログファイルにメッセージを書き込みます。

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

コンテナ`busybox1`が停止していることを確認しますが、削除しないでください。

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

次に、`--volumes-from`オプションを使用して、`busybox1`によって作成されたボリュームを共有するための2番目の`busybox`コンテナ`busybox2`を作成します。

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

Dockerは、`--volumes-from`オプションを使用して共有できる匿名ボリュームを作成し、新しい匿名ボリュームを作成しました。

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

既存のボリュームとコンテナをクリーンアップします。

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## 名前付きボリューム

「名前付きボリューム」と「匿名ボリューム」は、Dockerがそれらの配置場所を管理する点で似ています。ただし、「名前付きボリューム」は、コンテナディレクトリにマウントする際に名前で参照できます。これは、複数のコンテナ間でボリュームを共有したい場合に便利です。

まず、「名前付きボリューム」を作成します。

```bash
docker volume create my-couchdb-data-volume
```

ボリュームが作成されたことを確認します。

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

次に、「名前付きボリューム」を使用して、名前が「my-couchdb-name-vol」のCouchDBコンテナを作成します。

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDBコンテナが実行され、インスタンスが利用可能になるまで待ちます。

新しいデータベース「mydb」を作成し、「hello world」のメッセージを持つ新しいドキュメントを挿入します。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

これで、他のコンテナとボリュームを共有することが簡単になりました。たとえば、`busybox`イメージを使用してボリュームの内容を読み取り、`busybox`コンテナのディレクトリにボリュームをマウントすることで、「my-couchdb-data-volume」ボリュームを共有します。

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

特権付きの権限で`busybox`コンテナを実行し、プロセスIDを`host`に設定してホストシステムを調べ、Dockerが管理するディレクトリに移動することで、Dockerが管理するボリュームのファイルシステムを確認できます。

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

クリーンアップします。

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## ホストボリューム

ホストマシンから直接ボリュームディレクトリにアクセスしたい場合、Dockerが管理するディレクトリではなく、「ホストボリューム」を作成できます。

現在の作業ディレクトリ（コマンド`pwd`で示される）にある`data`というディレクトリを使用します。または、ホストマシン上の独自のデータディレクトリを選択します。たとえば、`/home/couchdb/data`です。まだ存在しない場合は、dockerが`$(pwd)/data`ディレクトリを作成します。CouchDBの既定のデータディレクトリであるコンテナディレクトリ`/opt/couchdb/data`に、CouchDBコンテナ内の「ホストボリューム」をマウントします。

次のコマンドを実行します。

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

ディレクトリ`data`が作成されたことを確認します。

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

そして、CouchDBがここにデータファイルを作成したことを確認します。

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

また、dockerが管理するボリュームは作成されていないことを確認します。なぜなら、今回は「ホストボリューム」を使用しているからです。

```bash
docker volume ls
```

そして

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

新しいデータベース「mydb」を作成し、「hello world」のメッセージを持つ新しいドキュメントを挿入します。

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

CouchDBが`shards`フォルダを作成したことに注意してください。

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

`shards`ディレクトリの内容を一覧表示します。

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

そして、最初のシャードを表示します。

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

[シャード](https://docs.couchdb.org/en/stable/cluster/sharding.html)は、データベース内のデータの水平分割です。データをシャードに分割し、各シャードのコピーをクラスタ内の異なるノードに分散させることで、ノードの損失に対するデータの耐久性を高めます。CouchDBは自動的にデータベースをシャード化し、ドキュメントのサブセットをノード間で分散させます。

クリーンアップします。

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
