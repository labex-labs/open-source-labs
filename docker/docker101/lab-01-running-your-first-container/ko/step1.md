# 시작하기

LabEx VM 에서 터미널을 열고 `docker -h`를 실행합니다. 그러면 Docker CLI 에 대한 도움말 페이지가 표시됩니다.

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

Docker 명령줄은 Docker Engine 의 여러 기능을 관리하는 데 사용할 수 있습니다. 이 랩에서는 주로 `container` 명령에 집중합니다.

LabEx VM 에 `podman`을 설치합니다.

```bash
sudo apt-get update
sudo apt-get install podman -y
```

`podman`이 설치된 경우, 비교를 위해 대체 명령을 실행할 수 있습니다.

```bash
sudo podman -h
```

`docker version`을 사용하여 Docker 설치 버전을 추가로 확인할 수 있습니다.

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

Docker 는 `Client`와 `Server: Docker Engine`을 모두 설치한다는 점에 유의하십시오. 예를 들어, podman 에 대해 동일한 명령을 실행하면 CLI 버전만 표시됩니다. 이는 podman 이 데몬리스로 실행되며, 실행 중인 컨테이너를 생성하기 위해 OS 와 인터페이스하는 OCI 호환 컨테이너 런타임 (runc, crun, runv 등) 에 의존하기 때문입니다.

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
