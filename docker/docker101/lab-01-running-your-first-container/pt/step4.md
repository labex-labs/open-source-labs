# Limpeza

Completar este laboratório resulta em um monte de contêineres em execução em seu host. Vamos limpá-los.

Primeiro, obtenha uma lista dos contêineres em execução usando `docker container ls`.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon ..." 3 minutes ago Up 3 minutes 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 minutes ago Up 3 minutes 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 minutes ago Up 8 minutes priceless_kepler
```

Em seguida, execute `docker container stop [container id]` para cada contêiner na lista. Você também pode usar os nomes dos contêineres que você especificou antes.

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**Observação**: Você só precisa referenciar dígitos suficientes do ID para serem exclusivos. Três dígitos são quase sempre suficientes.

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
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Total reclaimed space: 12B
```
