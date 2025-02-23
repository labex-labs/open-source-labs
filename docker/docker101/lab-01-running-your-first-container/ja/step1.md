# はじめに

LabEx VM 上でターミナルを開き、`docker -h` を実行すると、Docker CLI のヘルプ ページが表示されます。

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

Docker コマンド ラインを使用して、Docker Engine のいくつかの機能を管理できます。この実験では、主に `container` コマンドに焦点を当てます。

LabEx VM 上に `podman` をインストールします。

```bash
sudo apt-get update
sudo apt-get install podman -y
```

`podman` がインストールされている場合、比較のために代替コマンドを実行できます。

```bash
sudo podman -h
```

また、`docker version` を使用して、Docker インストールのバージョンを確認できます。

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

Docker は `Client` と `Server: Docker Engine` の両方をインストールすることに注意してください。たとえば、同じコマンドを podman に対して実行すると、CLI バージョンのみが表示されます。なぜなら、podman はデーモンレスで実行され、実行中のコンテナを作成するために OS とインターフェイスするために OCI 準拠のコンテナ ランタイム (runc、crun、runv など) に依存するからです。

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
