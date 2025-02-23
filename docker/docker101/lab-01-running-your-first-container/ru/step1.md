# Начало работы

Откройте терминал на виртуальной машине LabEx и запустите `docker -h`, что покажет вам страницу помощи по CLI Docker.

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

CLI Docker можно использовать для управления несколькими функциями Docker Engine. В этом лабе мы сосредоточимся в основном на команде `container`.

Установите `podman` на вашей виртуальной машине LabEx.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

Если `podman` установлен, вы можете запустить альтернативную команду для сравнения.

```bash
sudo podman -h
```

Вы также можете проверить версию вашей установки Docker с помощью `docker version`

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

Вы замечаете, что Docker устанавливает как `Client`, так и `Server: Docker Engine`. Например, если вы запустите ту же команду для podman, вы увидите только версию CLI, потому что podman работает без демона и зависит от OCI-совместимого контейнерного времени выполнения (runc, crun, runv и т.д.) для взаимодействия с ОС для создания запускаемых контейнеров.

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
