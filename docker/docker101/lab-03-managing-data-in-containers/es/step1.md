# Volúmenes

Un `volumen de datos` o `volumen` es un directorio que omite el `Sistema de Archivos Union` de Docker.

Hay tres tipos de volúmenes:

- volumen anónimo,
- volumen nombrado, y
- volumen host.

## Volumen Anónimo

Vamos a crear una instancia de una popular base de datos NoSQL de código abierto llamada CouchDB y usar un `volumen anónimo` para almacenar los archivos de datos de la base de datos.

Para ejecutar una instancia de CouchDB, use la imagen de CouchDB de Docker Hub en [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). La documentación dice que el predeterminado para CouchDB es `escribir los archivos de la base de datos en el disco del sistema host usando su propio sistema de gestión de volúmenes interno`.

Ejecute el siguiente comando:

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB creará un volumen anónimo y generará un nombre hash. Verifique los volúmenes en su sistema host:

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Establezca una variable de entorno `VOLUME` con el valor del nombre generado:

```bash
export VOLUME=<VOLUME NAME>
```

Y examine el volumen que se creó, use el nombre hash que se generó para el volumen:

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

Vea que Docker ha creado y gestiona un volumen en el sistema de archivos del host de Docker en `/var/lib/docker/volumes/$VOLUME_NAME/_data`. Tenga en cuenta que este no es un camino en la máquina host, sino una parte del sistema de archivos administrado por Docker.

Cree una nueva base de datos `mydb` e inserte un nuevo documento con un mensaje `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Detenga el contenedor y vuelva a iniciarlo:

```bash
docker stop my-couchdb
docker start my-couchdb
```

Recupere el documento de la base de datos para probar que los datos se persistieron.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

Salida:

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Compartir Volúmenes

Puede compartir un volumen anónimo con otro contenedor usando la opción `--volumes-from`.

Cree un contenedor `busybox` con un volumen anónimo montado en un directorio `/data` en el contenedor y, usando comandos de shell, escriba un mensaje en un archivo de registro.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Asegúrese de que el contenedor `busybox1` esté detenido pero no eliminado.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

Luego cree un segundo contenedor `busybox` llamado `busybox2` usando la opción `--volumes-from` para compartir el volumen creado por `busybox1`:

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

Docker creó el volumen anónimo que pudo compartir usando la opción `--volumes-from` y creó un nuevo volumen anónimo.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Limpie los volúmenes y contenedores existentes.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Volumen nombrado

Un `volumen nombrado` y un `volumen anónimo` son similares en que Docker gestiona donde se encuentran. Sin embargo, un `volumen nombrado` se puede referenciar por nombre al montarlo en un directorio de contenedor. Esto es útil si desea compartir un volumen entre múltiples contenedores.

Primero, cree un `volumen nombrado`:

```bash
docker volume create my-couchdb-data-volume
```

Verifique que el volumen se haya creado:

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

Ahora cree el contenedor de CouchDB llamado `my-couchdb-name-vol` usando el `volumen nombrado`:

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Espere a que el contenedor de CouchDB se esté ejecutando y la instancia esté disponible.

Cree una nueva base de datos `mydb` e inserte un nuevo documento con un mensaje `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

Ahora es fácil compartir el volumen con otro contenedor. Por ejemplo, lea el contenido del volumen usando la imagen `busybox` y comparta el volumen `my-couchdb-data-volume` montando el volumen en un directorio en el contenedor `busybox`.

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

Puede verificar el sistema de archivos administrado por Docker para volúmenes ejecutando un contenedor `busybox` con permisos privilegiados y estableciendo el identificador de proceso en `host` para inspeccionar el sistema host y navegar a los directorios administrados por Docker.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Limpie:

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Volumen Host

Cuando desea acceder fácilmente al directorio de volumen desde la máquina host directamente en lugar de usar los directorios administrados por Docker, puede crear un `volumen host`.

Usemos un directorio en el directorio de trabajo actual (indicado con el comando `pwd`) llamado `data`, o elija su propio directorio de datos en la máquina host, por ejemplo, `/home/couchdb/data`. Permitimos que Docker cree el directorio `$(pwd)/data` si aún no existe. Montamos el `volumen host` dentro del contenedor de CouchDB en el directorio de contenedor `/opt/couchdb/data`, que es el directorio de datos predeterminado para CouchDB.

Ejecute el siguiente comando:

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Verifique que se haya creado un directorio `data`:

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14.
drwxr-x--- 25 labex labex 4096 Aug 29 14:14..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

y que CouchDB ha creado archivos de datos aquí:

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14.
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14.delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

También verifique que ahora Docker no ha creado ningún volumen administrado, porque ahora estamos usando un `volumen host`.

```bash
docker volume ls
```

y

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

Cree una nueva base de datos `mydb` e inserte un nuevo documento con un mensaje `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Tenga en cuenta que CouchDB creó una carpeta `shards`:

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

Liste el contenido del directorio `shards`:

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

y el primer fragmento:

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15.
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

Un [fragmento](https://docs.couchdb.org/en/stable/cluster/sharding.html) es una partición horizontal de datos en una base de datos. Particionar los datos en fragmentos y distribuir copias de cada fragmento a diferentes nodos en un clúster le da a los datos una mayor durabilidad frente a la pérdida de nodos. CouchDB particiona automáticamente las bases de datos y distribuye los subconjuntos de documentos entre los nodos.

Limpie:

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
