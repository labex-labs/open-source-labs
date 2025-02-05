# 推送到中央注册表

如果你还没有账号，请访问 [Docker Hub](https://hub.docker.com) 并创建一个。或者，你也可以使用 [https://quay.io](https://quay.io) 等。

在本实验中，我们将使用 Docker Hub 作为我们的中央注册表。Docker Hub 是一项免费服务，用于存储公开可用的镜像，或者你也可以付费存储私有镜像。访问 [Docker Hub](https://hub.docker.com) 网站并创建一个免费账号。

大多数大量使用 Docker 的组织会在内部设置自己的注册表。为了简化操作，我们将使用 Docker Hub，但以下概念适用于任何注册表。

登录

你可以在终端中输入 `docker login` 登录到镜像注册表账户，如果使用 podman，则输入 `podman login`。

```bash
labex:project/ $ export DOCKERHUB_USERNAME=<your_docker_username>
labex:project/ $ docker login docker.io -u $DOCKERHUB_USERNAME
Password:
WARNING! Your password will be stored unencrypted in /home/labex/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
```

用你的用户名标记你的镜像

Docker Hub 的命名规范是用 [dockerhub 用户名]/[镜像名] 来标记你的镜像。为此，我们要将之前创建的镜像 `python-hello-world` 标记为符合该格式。

```bash
docker tag python-hello-world $DOCKERHUB_USERNAME/python-hello-world
```

将你的镜像推送到注册表

一旦我们有了一个标记正确的镜像，就可以使用 `docker push` 命令将我们的镜像推送到 Docker Hub 注册表。

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

在浏览器中查看 Docker Hub 上的镜像

访问 [Docker Hub](https://hub.docker.com)，进入你的个人资料，在 `https://hub.docker.com/repository/docker/<dockerhub-username>/python-hello-world` 查看你新上传的镜像。

现在你的镜像已在 Docker Hub 上，其他开发者和运维人员可以使用 `docker pull` 命令将你的镜像部署到其他环境。

**注意**：Docker 镜像包含运行镜像内应用程序所需的所有依赖项。这很有用，因为当我们依赖在每个部署环境中安装的依赖项时，我们不再需要处理环境差异（版本差异）。我们也不必再经历额外的步骤来配置这些环境。只需一步：安装 Docker，然后你就可以开始了。
