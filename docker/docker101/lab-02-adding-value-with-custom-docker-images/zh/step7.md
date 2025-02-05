# 清理

完成本实验后，你的主机上会有一堆正在运行的容器。让我们清理一下这些容器。

对于每个正在运行的容器，运行 `docker container stop [容器ID]`

首先使用 `docker container ls` 获取正在运行的容器列表。

```bash
$ docker container ls
```

然后对列表中的每个容器运行该命令。

```bash
$ docker container stop <容器ID>
```

删除已停止的容器

`docker system prune` 是一个非常方便的命令，用于清理你的系统。它将删除任何已停止的容器、未使用的卷和网络以及悬空镜像。

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
