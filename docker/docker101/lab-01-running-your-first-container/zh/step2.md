# 运行你的第一个容器

我们将使用 Docker CLI 来运行我们的第一个容器。

在 LabEx VM 上打开一个终端。

运行命令。

```bash
docker container run -t ubuntu top
```

使用 `docker container run` 命令，通过 `top` 命令运行一个使用 `ubuntu` 镜像的容器。`-t` 标志会分配一个伪终端，这是 `top` 命令正常工作所必需的。

```bash
$ docker container run -it ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
aafe6b5e13de: Pull complete
0a2b43a72660: Pull complete
18bdd1e546d2: Pull complete
8198342c3e05: Pull complete
f56970a44fd4: Pull complete
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
```

`docker run` 命令首先会执行 `docker pull`，将 `ubuntu` 镜像下载到你的主机上。下载完成后，它会启动容器。正在运行的容器的输出应该如下所示：

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top` 是一个 Linux 实用工具，它会打印系统上的进程，并按资源消耗对它们进行排序。请注意，此输出中只有一个进程：它就是 `top` 进程本身。由于 PID 命名空间隔离，我们在这个列表中看不到主机上的其他进程。

容器使用 Linux 命名空间来提供与其他容器或主机的系统资源隔离。PID 命名空间为进程 ID 提供隔离。如果你在容器内部运行 `top`，你会注意到它显示的是容器的 PID 命名空间内的进程，这与你在主机上运行 `top` 时看到的情况大不相同。

尽管我们使用的是 `ubuntu` 镜像，但需要注意的是，我们的容器没有自己的内核。它使用主机的内核，而 `ubuntu` 镜像仅用于提供 Ubuntu 系统上可用的文件系统和工具。

使用 `docker container exec` 检查容器

`docker container exec` 命令是一种通过新进程“进入”正在运行的容器的命名空间的方法。

打开一个新终端。选择 `终端` > `新建终端`。

在新终端中，使用 `docker container ls` 命令获取你刚刚创建的正在运行的容器的 ID。

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

然后使用该 ID，通过 `docker container exec` 命令在该容器内运行 `bash`。由于我们使用的是 `bash` 并且希望从终端与这个容器进行交互，因此使用 `-it` 标志以交互模式运行，同时分配一个伪终端。

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

瞧！我们刚刚使用 `docker container exec` 命令通过我们的 `bash` 进程“进入”了容器的命名空间。将 `docker container exec` 与 `bash` 一起使用是检查 Docker 容器的常见模式。

注意终端前缀的变化。例如 `root@b3ad2a23fab3:/`。这表明我们正在容器“内部”运行 `bash`。

**注意**：这与通过 SSH 连接到单独的主机或 VM 不同。我们不需要 SSH 服务器来连接到 `bash` 进程。请记住，容器使用内核级功能来实现隔离，并且容器运行在内核之上。我们的容器只是在同一主机上隔离运行的一组进程，我们可以使用 `docker container exec` 通过 `bash` 进程进入该隔离环境。运行 `docker container exec` 后，隔离运行的进程组（即我们的容器）包括 `top` 和 `bash`。

在同一个终端中，运行 `ps -ef` 来检查正在运行的进程。

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34? 00:00:00 top
root 17 0 0 21:06? 00:00:00 bash
root 27 17 0 21:14? 00:00:00 ps -ef
```

你应该只看到 `top` 进程、`bash` 进程和我们的 `ps` 进程。

为了进行比较，退出容器，然后在主机上运行 `ps -ef` 或 `top`。这些命令在 Linux 或 Mac 上都可以使用。对于 Windows，你可以使用 `tasklist` 来检查正在运行的进程。

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# 很多进程！
```

**技术深入探讨**
PID 只是为容器提供系统资源隔离的 Linux 命名空间之一。其他 Linux 命名空间包括：

- MNT - 挂载和卸载目录，而不会影响其他命名空间
- NET - 容器有自己的网络栈
- IPC - 隔离的进程间通信机制，如消息队列。
- User - 系统上用户的隔离视图
- UTC - 为每个容器设置主机名和域名

这些命名空间共同为容器提供了隔离，使它们能够安全地一起运行，并且不会与在同一系统上运行的其他容器发生冲突。接下来，我们将演示容器的不同用途，以及在同一主机上运行多个容器时隔离的好处。

**注意**：命名空间是 **Linux** 内核的一个特性。但是 Docker 允许你在 Windows 和 Mac 上运行容器……这是如何实现的呢？秘密在于 Docker 产品或 Docker 引擎中嵌入了一个 Linux 子系统。Docker 将这个 Linux 子系统开源到了一个新项目：[LinuxKit](https://github.com/linuxkit/linuxkit)。能够在许多不同平台上运行容器是将 Docker 工具与容器一起使用的一个优势。

除了使用 Linux 子系统在 Windows 上运行 Linux 容器之外，由于在 Windows 操作系统上创建了容器原语，现在原生 Windows 容器也成为可能。原生 Windows 容器可以在 Windows 10 或 Windows Server 2016 或更高版本上运行。

**注意**：如果你在容器化的终端中运行此练习，并在终端中执行 `ps -ef` 命令，在退出 `exec` 命令后，你仍然只会看到一组有限的进程。你可以尝试在本地机器的终端中运行 `ps -ef` 命令以查看所有进程。

通过按 `<ctrl>-c` 来清理运行 `top` 进程的容器，列出所有容器并通过它们的 ID 删除容器。

```bash
docker ps -a

docker rm <CONTAINER ID>
```
