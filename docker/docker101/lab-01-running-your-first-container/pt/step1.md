# Começando

Abra um terminal na VM do LabEx e execute `docker -h`, que mostrará a página de ajuda para a CLI do Docker.

```bash
$ docker -h
Flag shorthand -h has been deprecated, please use --help

Usage: docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

...

Management Commands:
builder Manage builds
config Manage Docker configs
container Manage containers
engine Manage the docker engine
image Manage images
network Manage networks
node Manage Swarm nodes
plugin Manage plugins
secret Manage Docker secrets
service Manage services
stack Manage Docker stacks
swarm Manage Swarm
system Manage Docker
trust Manage trust on Docker images
volume Manage volumes
```

A linha de comando do Docker pode ser usada para gerenciar vários recursos do Docker Engine. Neste laboratório, focaremos principalmente no comando `container`.

Instale o `podman` na sua VM do LabEx.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

Se o `podman` estiver instalado, você pode executar o comando alternativo para comparação.

```bash
sudo podman -h
```

Você pode, adicionalmente, revisar a versão da sua instalação do Docker com `docker version`

```bash
docker version

Client:
Version: 20.10.21
...

Server:
Engine:
Version: 20.10.21
...
```

Observe que o Docker instala tanto um `Client` quanto um `Server: Docker Engine`. Por exemplo, se você executar o mesmo comando para podman, verá apenas uma versão da CLI, porque o podman é executado sem daemon e depende de um runtime de contêiner compatível com OCI (runc, crun, runv etc.) para interagir com o sistema operacional para criar os contêineres em execução.

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
