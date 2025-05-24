# Volumes

Um `volume de dados` (data volume) ou `volume` é um diretório que ignora o `Sistema de Arquivos de União` (Union File System) do Docker.

Existem três tipos de volumes:

- volume anônimo,
- volume nomeado, e
- volume host.

## Volume Anônimo

Vamos criar uma instância de um popular banco de dados NoSQL de código aberto chamado CouchDB e usar um `volume anônimo` para armazenar os arquivos de dados do banco de dados.

Para executar uma instância do CouchDB, use a imagem CouchDB do Docker Hub em [https://hub.docker.com/\_/couchdb](https://hub.docker.com/_/couchdb). Os documentos dizem que o padrão para CouchDB é `escrever os arquivos do banco de dados no disco no sistema host usando sua própria gestão de volume interna`.

Execute o seguinte comando:

```bash
docker run -d -p 5984:5984 --name my-couchdb -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

CouchDB criará um volume anônimo e gerará um nome com hash. Verifique os volumes no seu sistema host:

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Defina uma variável de ambiente `VOLUME` com o valor do nome gerado:

```bash
export VOLUME=<VOLUME NAME>
```

E inspecione o volume que foi criado, use o nome com hash que foi gerado para o volume:

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

Você vê que o Docker criou e gerencia um volume no sistema de arquivos host do Docker em `/var/lib/docker/volumes/$VOLUME_NAME/_data`. Observe que este não é um caminho na máquina host, mas sim uma parte do sistema de arquivos gerenciado pelo Docker.

Crie um novo banco de dados `mydb` e insira um novo documento com uma mensagem `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Pare o container e inicie o container novamente:

```bash
docker stop my-couchdb
docker start my-couchdb
```

Recupere o documento no banco de dados para testar se os dados foram persistidos.

```bash
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
```

Saída:

```
# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/_all_docs
{"total_rows":1,"offset":0,"rows":[
{"id":"1","key":"1","value":{"rev":"1-c09289617e06b96bc747fb1201fea7f1"}}
]}

# $ curl -X GET -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1
{"_id":"1","_rev":"1-c09289617e06b96bc747fb1201fea7f1","msg":"hello world"}
```

## Compartilhando Volumes

Você pode compartilhar um volume anônimo com outro container usando a opção `--volumes-from`.

Crie um container `busybox` com um volume anônimo montado em um diretório `/data` no container e, usando comandos de shell, escreva uma mensagem em um arquivo de log.

```bash
$ docker run -it --name busybox1 -v /data busybox sh
/ # echo "hello from busybox1" > /data/hi.log
/ # ls /data
hi.log
/ # exit
```

Certifique-se de que o container `busybox1` esteja parado, mas não removido.

```bash
labex:~/ $ docker ps -a | grep busybox1
f4dbf9ee7513   busybox                               "sh"                     2 minutes ago   Exited (0) About a minute ago                                                                                                                                          busybox1

```

Em seguida, crie um segundo container `busybox` chamado `busybox2` usando a opção `--volumes-from` para compartilhar o volume criado por `busybox1`:

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

O Docker criou o volume anônimo que você pôde compartilhar usando a opção `--volumes-from` e criou um novo volume anônimo.

```bash
labex:~/ $ docker volume ls
DRIVER VOLUME NAME
local 0f971b2477d5fc0d0c2b31fc908ee59d6b577b4887e381964650ce6853890dc9
local 1d292aca855adb9de9be7acea88f6d3f8e6a08eef5bfd986a81f073f1906b82f
```

Limpe os volumes e o container existentes.

```bash
docker stop my-couchdb
docker rm my-couchdb
docker rm busybox1
docker volume rm $(docker volume ls -q)
docker system prune -a
clear
```

## Volume Nomeado

Um `volume nomeado` e um `volume anônimo` são semelhantes no sentido de que o Docker gerencia onde eles estão localizados. No entanto, um `volume nomeado` pode ser referenciado por nome ao montá-lo em um diretório de container. Isso é útil se você deseja compartilhar um volume entre vários containers.

Primeiro, crie um `volume nomeado`:

```bash
docker volume create my-couchdb-data-volume
```

Verifique se o volume foi criado:

```bash
$ docker volume ls
DRIVER VOLUME NAME
local my-couchdb-data-volume
```

Agora, crie o container CouchDB chamado `my-couchdb-name-vol` usando o `volume nomeado`:

```bash
docker run -d -p 59840:5984 --name my-couchdb-name-vol -v my-couchdb-data-volume:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Aguarde até que o container CouchDB esteja em execução e a instância esteja disponível.

Crie um novo banco de dados `mydb` e insira um novo documento com uma mensagem `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:59840/mydb/1 -d '{"msg": "hello world"}'
```

Agora é fácil compartilhar o volume com outro container. Por exemplo, leia o conteúdo do volume usando a imagem `busybox` e compartilhe o volume `my-couchdb-data-volume` montando o volume em um diretório no container `busybox`.

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

Você pode verificar o sistema de arquivos gerenciado pelo Docker para volumes executando um container busybox com permissão privilegiada e definindo o ID do processo como `host` para inspecionar o sistema host e navegar pelos diretórios gerenciados pelo Docker.

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
/ # ls -l /var/lib/docker/volumes
total 28
-rw------- 1 root root 32768 Nov 10 15:54 metadata.db
drwxr-xr-x 3 root root 4096 Nov 10 15:54 my-couchdb-data-volume
/ # exit
```

Limpeza:

```bash
docker stop my-couchdb
docker rm my-couchdb
docker volume rm my-couchdb-data-volume
docker system prune -a
docker volume prune
clear
```

## Volume Host

Quando você deseja acessar o diretório do volume facilmente da máquina host diretamente, em vez de usar os diretórios gerenciados pelo Docker, você pode criar um `volume host`.

Vamos usar um diretório no diretório de trabalho atual (indicado com o comando `pwd`) chamado `data`, ou escolher seu próprio diretório de dados na máquina host, por exemplo, `/home/couchdb/data`. Deixamos o docker criar o diretório `$(pwd)/data` se ele ainda não existir. Montamos o `volume host` dentro do container CouchDB no diretório do container `/opt/couchdb/data`, que é o diretório de dados padrão para CouchDB.

Execute o seguinte comando:

```bash
cd /home/labex/project
docker run -d -p 5984:5984 --name my-couchdb -v $(pwd)/data:/opt/couchdb/data -e COUCHDB_USER=admin -e COUCHDB_PASSWORD=passw0rd1 couchdb:3.1
```

Verifique se um diretório `data` foi criado:

```bash
$ ls -al
total 20
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 .
drwxr-x--- 25 labex labex 4096 Aug 29 14:14 ..
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 data
```

e que o CouchDB criou arquivos de dados aqui:

```bash
$ ls -al data
total 32
drwxr-xr-x 3 5984 5984 4096 Aug 29 14:14 .
drwxrwxr-x 3 labex labex 4096 Aug 29 14:14 ..
-rw-r--r-- 1 5984 5984 4257 Aug 29 14:14 _dbs.couch
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:14 .delete
-rw-r--r-- 1 5984 5984 8385 Aug 29 14:14 _nodes.couch
```

Verifique também que, agora, nenhum volume gerenciado foi criado pelo docker, porque estamos usando um `volume host`.

```bash
docker volume ls
```

e

```bash
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
sh-5.1# ls -l /var/lib/docker/volumes
total 28
brw------- 1 root root 252, 3 Jan 23 15:15 backingFsBlockDev
-rw------- 1 root root 32768 Jan 23 15:33 metadata.db
drwx-----x 3 root root 4096 Jan 23 15:26 my-couchdb-data-volume
sh-5.1# exit
```

Crie um novo banco de dados `mydb` e insira um novo documento com uma mensagem `hello world`.

```bash
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb
curl -X PUT -u admin:passw0rd1 http://127.0.0.1:5984/mydb/1 -d '{"msg": "hello world"}'
```

Observe que o CouchDB criou uma pasta `shards`:

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

Liste o conteúdo do diretório `shards`:

```bash
$ ls -al data/shards
total 16
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 00000000-7fffffff
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 80000000-ffffffff
```

e o primeiro shard:

```bash
$ ls -al data/shards/00000000-7fffffff/
total 20
drwxr-xr-x 2 5984 5984 4096 Aug 29 14:15 .
drwxr-xr-x 4 5984 5984 4096 Aug 29 14:15 ..
-rw-r--r-- 1 5984 5984 8346 Aug 29 14:15 mydb.1693289721.couch
```

Um [shard](https://docs.couchdb.org/en/stable/cluster/sharding.html) é uma partição horizontal de dados em um banco de dados. A partição de dados em shards e a distribuição de cópias de cada shard para diferentes nós em um cluster dão aos dados maior durabilidade contra perda de nós. O CouchDB divide automaticamente os bancos de dados e distribui os subconjuntos de documentos entre os nós.

Limpeza:

```bash
docker stop my-couchdb
docker rm my-couchdb
sudo rm -rf $(pwd)/data
docker system prune -a
```
