# 创建并构建 Docker 镜像

现在，如果你本地没有安装 Python 怎么办？别担心！因为你不需要在本地安装。使用容器的优点之一是你可以在容器内部构建 Python 环境，而无需在主机上安装 Python。

通过运行以下命令创建一个 `Dockerfile`。（复制粘贴整个代码块）

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

一个 Dockerfile 列出了构建 Docker 镜像所需的指令。让我们逐行分析上述文件。

**FROM python:3.8-alpine**
这是你的 Dockerfile 的起始点。每个 Dockerfile 都必须以 `FROM` 行开头，这是构建你的镜像层所基于的起始镜像。

在这种情况下，我们选择 `python:3.8-alpine` 基础层（请参阅 [python3.8/alpine3.12 的 Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)），因为它已经包含了运行我们的应用程序所需的 Python 和 pip 版本。

`alpine` 版本意味着它使用 [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux) 发行版，该发行版比许多其他 Linux 变体小得多，大小约为 8MB，而最小的磁盘安装可能约为 130MB。较小的镜像意味着它将更快地下载（部署），并且在安全方面也有优势，因为它的攻击面较小。[Alpine Linux](https://alpinelinux.org/downloads/) 是一个基于 musl 和 BusyBox 的 Linux 发行版。

在这里，我们使用“3.8-alpine”标签来标记 Python 镜像。查看 [Docker Hub](https://hub.docker.com/_/python/) 上官方 Python 镜像的可用标签。在继承父镜像时使用特定标签是最佳实践，这样可以控制对父依赖项的更改。如果未指定标签，则“latest”标签将生效，它充当指向镜像最新版本的动态指针。

出于安全原因，了解你在其上构建 Docker 镜像的层非常重要。因此，强烈建议仅使用在 [docker hub](https://hub.docker.com/) 中找到的“官方”镜像，或在 docker-store 中找到的非社区镜像。这些镜像经过 [审核](https://docs.docker.com/docker-hub/official_repos/) 以满足某些安全要求，并且也有非常好的文档供用户参考。你可以在 [docker hub](https://hub.docker.com) 上找到有关此 [Python 基础镜像](https://hub.docker.com/_/python) 以及所有其他可用镜像的更多信息。

对于更复杂的应用程序，你可能会发现需要使用更高层次的 `FROM` 镜像。例如，我们的 Python 应用程序的父 [Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) 以 `FROM alpine` 开头，然后为镜像指定一系列 `CMD` 和 `RUN` 命令。如果你需要更精细的控制，可以从 `FROM alpine`（或其他发行版）开始并自己运行这些步骤。不过，一开始，我建议使用与你需求紧密匹配的官方镜像。

**RUN pip install flask**
`RUN` 命令执行设置应用程序镜像所需的命令，例如安装软件包、编辑文件或更改文件权限。在这种情况下，我们正在安装 flask。`RUN` 命令在构建时执行，并添加到你的镜像层中。

**CMD ["python","app.py"]**
`CMD` 是启动容器时执行的命令。在这里，我们使用 `CMD` 来运行我们的 Python 应用程序。

每个 Dockerfile 只能有一个 `CMD`。如果你指定多个 `CMD`，则最后一个 `CMD` 将生效。父镜像 python:3.8-alpine 也指定了一个 `CMD`（`CMD python3`）。你可以在 [这里](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) 找到官方 python:alpine 镜像的 Dockerfile。

你可以直接使用官方 Python 镜像来运行 Python 脚本，而无需在主机上安装 Python。但今天，我们正在创建一个自定义镜像以包含我们的源代码，以便我们可以使用我们的应用程序构建一个镜像并将其部署到其他环境中。

**COPY app.py /app.py**
这将本地目录（你将在其中运行 `docker image build`）中的 app.py 复制到镜像的新层中。此指令是 Dockerfile 中的最后一行。频繁更改的层，例如将源代码复制到镜像中，应放在文件底部以充分利用 Docker 层缓存。这使我们能够避免重建原本可以缓存的层。例如，如果 `FROM` 指令发生更改，它将使此镜像的所有后续层的缓存无效。我们将在本实验后面演示这一点。

将此指令放在 `CMD ["python","app.py"]` 行之后似乎违反直觉。请记住，`CMD` 行仅在容器启动时执行，所以我们在这里不会得到 `文件未找到` 错误。

这样你就有了一个非常简单的 Dockerfile。你可以在 [这里](https://docs.docker.com/engine/reference/builder/) 找到可以放入 Dockerfile 的完整命令列表。现在我们已经定义了 Dockerfile，让我们用它来构建我们的自定义 Docker 镜像。

构建 Docker 镜像。

传入 `-t` 来将你的镜像命名为 `python-hello-world`。

```bash
docker image build -t python-hello-world.
```

验证你的镜像是否出现在你的镜像列表中。

```bash
docker image ls
```

**注意** 你的基础镜像 `python:3.8-alpine` 也在你的列表中。

你可以运行历史命令来查看镜像及其层的历史记录，

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
