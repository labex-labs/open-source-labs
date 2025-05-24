# 볼륨 (Volumes)

`data volume` 또는 `volume`은 Docker 의 `Union File System`을 우회하는 디렉토리입니다.

볼륨에는 세 가지 유형이 있습니다.

- 익명 볼륨 (anonymous volume),
- 명명된 볼륨 (named volume), 그리고
- 호스트 볼륨 (host volume).

## 익명 볼륨 (Anonymous Volume)

인기 있는 오픈 소스 NoSQL 데이터베이스인 CouchDB 의 인스턴스를 생성하고 `익명 볼륨`을 사용하여 데이터베이스의 데이터 파일을 저장해 보겠습니다.

CouchDB 의 인스턴스를 실행하려면 [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb)에서 Docker Hub 의 CouchDB 이미지를 사용하십시오. 문서에 따르면 CouchDB 의 기본값은 `자체 내부 볼륨 관리를 사용하여 호스트 시스템의 디스크에 데이터베이스 파일을 쓰는 것`입니다.

다음 명령을 실행합니다.

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB 는 익명 볼륨을 생성하고 해시된 이름을 생성합니다. 호스트 시스템에서 볼륨을 확인합니다.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

생성된 이름의 값을 사용하여 환경 변수 `VOLUME`을 설정합니다.

```bash
export VOLUME=<VOLUME NAME>
```

생성된 볼륨을 검사하려면 볼륨에 대해 생성된 해시 이름을 사용합니다.

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

Docker 가 `/var/lib/docker/volumes/$VOLUME_NAME/_data` 아래의 Docker 호스트 파일 시스템에 볼륨을 생성하고 관리하는 것을 볼 수 있습니다. 이는 호스트 머신의 경로가 아니라 Docker 가 관리하는 파일 시스템의 일부입니다.

새 데이터베이스 `mydb`를 생성하고 `hello world` 메시지가 있는 새 문서를 삽입합니다.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

컨테이너를 중지하고 다시 시작합니다.

```bash
docker stop my-couchdb
docker start my-couchdb
```

데이터가 지속되었는지 테스트하기 위해 데이터베이스에서 문서를 검색합니다.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

출력:

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## 볼륨 공유 (Sharing Volumes)

`--volumes-from` 옵션을 사용하여 익명 볼륨을 다른 컨테이너와 공유할 수 있습니다.

익명 볼륨이 컨테이너의 `/data` 디렉토리에 마운트된 `busybox` 컨테이너를 생성하고 셸 명령을 사용하여 로그 파일에 메시지를 씁니다.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

`busybox1` 컨테이너가 중지되었지만 제거되지 않았는지 확인합니다.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

그런 다음 `--volumes-from` 옵션을 사용하여 `busybox1`에서 생성된 볼륨을 공유하는 `busybox2`라는 두 번째 `busybox` 컨테이너를 생성합니다.

```bash
$ docker run --rm -it --name busybox2 --volumes-from busybox1 busybox sh
/ # ls -al /data
total 12
drwxr-xr-x 2 root root 4096 Jan 23 07:20 .
drwxr-xr-x 1 root root 4096 Jan 23 07:24 ..
-rw-r--r-- 1 root root 20 Jan 23 07:20 hi.log
/ # cat /data/hi.log
hello from busybox1
/ # exit
```

Docker 는 `--volumes-from` 옵션을 사용하여 공유할 수 있었던 익명 볼륨을 생성하고 새 익명 볼륨을 생성했습니다.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

기존 볼륨과 컨테이너를 정리합니다.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## 명명된 볼륨 (Named Volume)

`명명된 볼륨`과 `익명 볼륨`은 Docker 가 위치를 관리한다는 점에서 유사합니다. 그러나 `명명된 볼륨`은 컨테이너 디렉토리에 마운트할 때 이름으로 참조할 수 있습니다. 이는 여러 컨테이너에서 볼륨을 공유하려는 경우에 유용합니다.

먼저 `명명된 볼륨`을 생성합니다.

```bash
docker volume create my-couchdb-data-volume
```

볼륨이 생성되었는지 확인합니다.

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

이제 `명명된 볼륨`을 사용하여 `my-couchdb-name-vol`이라는 CouchDB 컨테이너를 생성합니다.

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB 컨테이너가 실행되고 인스턴스를 사용할 수 있을 때까지 기다립니다.

새 데이터베이스 `mydb`를 생성하고 `hello world` 메시지가 있는 새 문서를 삽입합니다.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

이제 다른 컨테이너와 볼륨을 쉽게 공유할 수 있습니다. 예를 들어 `busybox` 이미지를 사용하여 볼륨의 내용을 읽고 `my-couchdb-data-volume` 볼륨을 `busybox` 컨테이너의 디렉토리에 마운트하여 공유합니다.

```bash
labex:~/ $ docker run --rm -it --name busybox -v my-couchdb-data-volume:/myvolume busybox sh
/ #
/ # ls -al /myvolume
total 40
drwxr-xr-x 4 5984 5984 4096 Jan 23 07:30 .
drwxr-xr-x 1 root root 4096 Jan 23 07:31 ..
drwxr-xr-x 2 5984 5984 4096 Jan 23 07:29 .delete
-rw-r--r-- 1 5984 5984 8388 Jan 23 07:30 _dbs.couch
-rw-r--r-- 1 5984 5984 8385 Jan 23 07:29 _nodes.couch
drwxr-xr-x 4 5984 5984 4096 Jan 23 07:30 shards
/ # exit
```

특권 권한으로 busybox 컨테이너를 실행하고 프로세스 ID 를 `host`로 설정하여 호스트 시스템을 검사하고 Docker 관리 디렉토리를 탐색하여 볼륨에 대한 Docker 관리 파일 시스템을 확인할 수 있습니다.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

정리,

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## 호스트 볼륨 (Host Volume)

Docker 관리 디렉토리를 사용하는 대신 호스트 머신에서 볼륨 디렉토리에 직접 쉽게 액세스하려는 경우 `호스트 볼륨`을 생성할 수 있습니다.

현재 작업 디렉토리 (명령 `pwd`로 표시됨) 의 `data`라는 디렉토리를 사용하거나 호스트 머신에서 자체 데이터 디렉토리 (예: `/home/couchdb/data`) 를 선택합니다. docker 가 아직 존재하지 않는 경우 `$(pwd)/data` 디렉토리를 생성하도록 합니다. CouchDB 의 기본 데이터 디렉토리인 CouchDB 컨테이너 내의 `호스트 볼륨`을 컨테이너 디렉토리 `/opt/couchdb/data`에 마운트합니다.

다음 명령을 실행합니다.

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

`data` 디렉토리가 생성되었는지 확인합니다.

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 .
drwxr-x--- 25 labex labex 4096 Aug 29 14:14 ..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

그리고 CouchDB 가 여기에 데이터 파일을 생성했는지 확인합니다.

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 .
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 ..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14 .delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

또한 이제 `호스트 볼륨`을 사용하고 있으므로 docker 에서 관리하는 볼륨이 생성되지 않았는지 확인합니다.

```bash
docker volume ls
```

그리고

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

새 데이터베이스 `mydb`를 생성하고 `hello world` 메시지가 있는 새 문서를 삽입합니다.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

CouchDB 가 `shards` 폴더를 생성했음을 참고하십시오.

```bash
$ ls -al data
total 40
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 .
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 ..
-rw-r--r-- 1 5984 5984 8388 Aug 29 14:15 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14 .delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 shards
```

`shards` 디렉토리의 내용을 나열합니다.

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

그리고 첫 번째 샤드 (shard) 를 나열합니다.

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

[샤드 (shard)](https://docs.couchdb.org/en/stable/cluster/sharding.html)는 데이터베이스의 데이터 수평 분할입니다. 데이터를 샤드로 분할하고 각 샤드의 복사본을 클러스터의 서로 다른 노드에 배포하면 노드 손실에 대한 데이터 내구성이 향상됩니다. CouchDB 는 자동으로 데이터베이스를 샤딩하고 문서의 하위 집합을 노드 간에 배포합니다.

정리,

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
