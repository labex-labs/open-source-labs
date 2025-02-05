# 清理

完成本实验后，你的主机上会有一堆正在运行的容器。让我们清理一下这些容器。

首先，使用 `docker container ls` 获取正在运行的容器列表。

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon..." 3 分钟前 已启动 3 分钟 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 分钟前 已启动 3 分钟 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 分钟前 已启动 8 分钟 priceless_kepler
```

接下来，对列表中的每个容器运行 `docker container stop [容器 ID]`。你也可以使用之前指定的容器名称。

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**注意**：你只需引用足够多的 ID 数字以确保其唯一性。三位数字几乎总是足够的。

删除已停止的容器

`docker system prune` 是一个非常方便的命令，用于清理你的系统。它将删除任何已停止的容器、未使用的卷和网络以及悬空镜像。

```bash
$ docker system prune
WARNING! This will remove:
- 所有已停止的容器
- 所有至少一个容器未使用的卷
- 所有至少一个容器未使用的网络
- 所有悬空镜像
你确定要继续吗？[y/N] y
已删除的容器：
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

总共回收的空间：12B
```
