# 入门指南

在 LabEx VM 上打开一个终端并运行 `docker -h`，这将显示 Docker CLI 的帮助页面。

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

Docker 命令行可用于管理 Docker 引擎的多个功能。在本实验中，我们将主要关注 `container` 命令。

在你的 LabEx VM 上安装 `podman`。

```bash
sudo apt-get update
sudo apt-get install podman -y
```

如果安装了 `podman`，你可以运行替代命令进行比较。

```bash
sudo podman -h
```

你还可以通过 `docker version` 查看 Docker 的安装版本

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

你会注意到 Docker 安装了一个 `客户端` 和一个 `服务器：Docker 引擎`。例如，如果你对 podman 运行相同的命令，你只会看到一个 CLI 版本，因为 podman 无守护进程运行，并且依赖于符合 OCI 的容器运行时（runc、crun、runv 等）与操作系统进行交互以创建正在运行的容器。

```bash
sudo podman version --events-backend=none
Version: 3.4.4
API Version: 3.4.4
Go Version: go1.17.3
Built: Thu Jan 1 08:00:00 1970
OS/Arch: linux/amd64
```
