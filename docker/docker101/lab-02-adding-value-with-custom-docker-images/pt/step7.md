# Limpeza

Completar este laboratório resulta em um monte de contêineres em execução no seu host. Vamos limpá-los.

Execute `docker container stop [container id]` para cada contêiner que estiver em execução

Primeiro, obtenha uma lista dos contêineres em execução usando `docker container ls`.

```bash
$ docker container ls
```

Em seguida, execute o comando para cada contêiner na lista.

```bash
$ docker container stop <container_id>
```

Remova os contêineres parados

`docker system prune` é um comando muito útil para limpar seu sistema. Ele removerá quaisquer contêineres parados, volumes e redes não utilizados e imagens pendentes.

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
