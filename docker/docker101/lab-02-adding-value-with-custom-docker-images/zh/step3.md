# 运行 Docker 镜像

既然你已经构建了镜像，就可以运行它来查看是否能正常工作。

运行 Docker 镜像

```bash
docker run -p 5001:5000 -d python-hello-world
```

`-p` 标志将容器内运行的端口映射到你的主机。在这种情况下，我们将容器内运行在端口 5000 的 Python 应用程序映射到主机上的端口 5001。请注意，如果端口 5001 已被主机上的另一个应用程序使用，你可能需要将 5001 替换为另一个值，例如 5002。

在终端窗口中导航到 **PORTS** 标签，并点击链接在新的浏览器标签页中打开应用程序。

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

在终端中运行 `curl localhost:5001`，它将返回 `hello world!`。

检查容器的日志输出。

如果你想查看应用程序的日志，可以使用 `docker container logs` 命令。默认情况下，`docker container logs` 会打印出应用程序发送到标准输出的内容。使用 `docker container ls` 来查找正在运行的容器的 ID。

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Dockerfile 是你为应用程序创建可重复构建的方式。常见的工作流程是让你的 CI/CD 自动化在其构建过程中运行 `docker image build`。一旦镜像构建完成，它们将被发送到中央注册表，在那里需要运行该应用程序实例的所有环境（如测试环境）都可以访问。在下一步中，我们将把我们的自定义镜像推送到公共 Docker 注册表：Docker Hub，其他开发者和运维人员可以在那里使用它。
