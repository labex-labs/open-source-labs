# 理解镜像层

Docker 的主要设计特性之一是其对联合文件系统的使用。

考虑一下我们之前创建的 `Dockerfile`：

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

这些行中的每一行都是一个层。每个层仅包含与它之前的层相比的增量、差异或更改。为了将这些层组合成一个正在运行的容器，Docker 使用联合文件系统将这些层透明地叠加到一个单一视图中。

镜像的每个层都是只读的，除了为正在运行的容器创建的最顶层。读写容器层实现了“写时复制”，这意味着只有在对存储在较低镜像层中的文件进行编辑时，这些文件才会被提升到读写容器层。然后，这些更改会存储在正在运行的容器层中。“写时复制”功能非常快，并且在几乎所有情况下，对性能都没有明显影响。你可以使用 `docker diff` 命令检查哪些文件已被提升到容器级别。有关如何使用 `docker diff` 的更多信息，请参阅 [此处](https://docs.docker.com/engine/reference/commandline/diff/)。

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

由于镜像层是只读的，它们可以被镜像和正在运行的容器共享。例如，使用具有相似基础层的自己的 Dockerfile 创建一个新的 Python 应用程序，将共享它与第一个 Python 应用程序共有的所有层。

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

当你从同一个镜像启动多个容器时，你也可以体验到层的共享。由于容器使用相同的只读层，你可以想象启动容器非常快，并且在主机上占用的资源非常少。

你可能会注意到这个 Dockerfile 和你在本实验前面创建的 Dockerfile 中有重复的行。虽然这是一个非常简单的例子，但你可以将两个 Dockerfile 的公共行提取到一个“基础”Dockerfile 中，然后使用 `FROM` 命令让每个子 Dockerfile 指向它。

镜像分层为构建和推送启用了 Docker 缓存机制。例如，你最后一次 `docker push` 的输出表明，你的镜像的某些层已经存在于 Docker Hub 上。

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

为了更仔细地查看层，你可以使用我们创建的 Python 镜像的 `docker image history` 命令。

```bash
$ docker image history python-hello-world
```

每一行代表镜像的一个层。你会注意到顶部的行与你创建的 Dockerfile 匹配，下面的行是从父 Python 镜像中提取的。不用担心“<缺失>”标签。这些仍然是正常的层；它们只是没有被 Docker 系统赋予一个 ID。
