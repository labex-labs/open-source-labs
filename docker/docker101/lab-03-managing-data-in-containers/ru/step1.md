# Томы

«Датовый том» (`data volume`) или «том» (`volume`) — это каталог, который обходит объединенную файловую систему Docker.

Есть три типа томов:

- анонимный том,
- именованный том, и
- хостовой том.

## Анонимный том

Создадим экземпляр популярной открытой исходной кодовой NoSQL-базы данных CouchDB и используем анонимный том для хранения файлов данных для базы данных.

Для запуска экземпляра CouchDB используйте образ CouchDB с Docker Hub по адресу [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). В документации сказано, что по умолчанию для CouchDB `записываются файлы базы данных на диск в системе хоста с использованием собственного внутреннего управления томами`.

Запустите следующую команду:

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB создаст анонимный том и сгенерирует именованный хэш. Проверьте тома на вашей системе хоста:

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Установите переменную окружения `VOLUME` со значением сгенерированного имени:

```bash
export VOLUME=<VOLUME NAME>
```

И проверьте том, который был создан, используя хэш-имя, сгенерированное для тома:

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

Вы видите, что Docker создал и управляет томом в файловой системе Docker-хоста по пути `/var/lib/docker/volumes/$VOLUME_NAME/_data`. Обратите внимание, что это не путь на хост-машине, а часть управляемой Docker файловой системы.

Создайте новую базу данных `mydb` и вставьте новый документ с сообщением `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Остановите контейнер и запустите его снова:

```bash
docker stop my-couchdb
docker start my-couchdb
```

Получите документ из базы данных, чтобы проверить, сохранились ли данные.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

Вывод:

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Общий доступ к томам

Вы можете поделиться анонимным томом с другим контейнером, используя параметр `--volumes-from`.

Создайте контейнер `busybox` с анонимным томом, смонтированным в каталог `/data` внутри контейнера, и с использованием командной строки напишите сообщение в файл журнала.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Убедитесь, что контейнер `busybox1` остановлен, но не удален.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

Затем создайте второй контейнер `busybox` с именем `busybox2`, используя параметр `--volumes-from`, чтобы поделиться томом, созданным контейнером `busybox1`:

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

Docker создал анонимный том, который вы смогли поделиться с использованием параметра `--volumes-from`, и создал новый анонимный том.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Очистите существующие тома и контейнеры.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Именованный том

«Именованный том» (`named volume`) и «анонимный том» похожи тем, что Docker управляет их расположением. Однако именованный том можно ссылаться по имени при монтировании в каталог контейнера. Это полезно, если вы хотите поделиться томом между несколькими контейнерами.

Сначала создайте именованный том:

```bash
docker volume create my-couchdb-data-volume
```

Проверьте, был ли том создан:

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

Теперь создайте контейнер CouchDB с именем `my-couchdb-name-vol`, используя именованный том:

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Подождите, пока контейнер CouchDB запустится и будет доступен.

Создайте новую базу данных `mydb` и вставьте новый документ с сообщением `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

Теперь легко поделиться томом с другим контейнером. Например, прочитайте содержимое тома с использованием образа `busybox` и поделитесь томом `my-couchdb-data-volume`, смонтировав том в каталог внутри контейнера `busybox`.

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

Вы можете проверить файловую систему Docker для томов, запустив контейнер `busybox` с привилегированными правами и установив идентификатор процесса в `host`, чтобы проверить систему хоста, и перейти по управляемым Docker каталогам.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Очистите:

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Хостовой том

Когда вы хотите легко получить доступ к каталогу тома напрямую с хост-машины, вместо использования управляемых Docker каталогов, вы можете создать хостовой том.

Используйте каталог в текущем рабочем каталоге (указанный командой `pwd`), называемый `data`, или выберите свой собственный каталог данных на хост-машине, например, `/home/couchdb/data`. Мы позволим Docker создать каталог `$(pwd)/data`, если он еще не существует. Мы монтируем хостовой том внутри контейнера CouchDB в каталог контейнера `/opt/couchdb/data`, который является стандартным каталогом данных для CouchDB.

Запустите следующую команду:

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Проверьте, был ли создан каталог `data`:

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

и что CouchDB создал здесь файлы данных:

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

Также проверьте, что теперь Docker не создал управляемый том, потому что мы теперь используем хостовой том.

```bash
docker volume ls
```

и

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

Создайте новую базу данных `mydb` и вставьте новый документ с сообщением `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Обратите внимание, что CouchDB создал папку `shards`:

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

Выведите содержимое каталога `shards`:

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

и первый шар:

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

[Шарды](https://docs.couchdb.org/en/stable/cluster/sharding.html) — это горизонтальное разделение данных в базе данных. Разделение данных на шарды и распределение копий каждого шарда по разным узлам в кластере обеспечивает большую устойчивость данных к потере узлов. CouchDB автоматически разбивает базы данных на шарды и распределяет подмножества документов между узлами.

Очистите:

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
