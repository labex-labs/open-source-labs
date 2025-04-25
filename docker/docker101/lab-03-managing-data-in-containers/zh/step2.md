# 绑定挂载

与「卷」语法相比，Docker 推荐使用「挂载」（mount）语法。与卷相比，绑定挂载的功能有限。当一个文件或目录挂载到容器中时，它是通过主机上的完整路径来引用的。绑定挂载依赖于主机文件系统具有特定的目录结构，并且你不能使用 Docker CLI 来管理绑定挂载。请注意，绑定挂载可以通过容器中运行的进程来更改主机文件系统。

与使用由冒号分隔符（:）分隔的三个字段的`-v`语法不同，「挂载」语法更详细，使用多个「键值」对：

- type：bind、volume 或 tmpfs，
- source：主机上文件或目录的路径，
- destination：容器中的路径，
- readonly，
- bind-propagation：rprivate、private、rshared、shared、rslave、slave，
- consistency：consistent、delegated、cached，
- mount。

```bash
cd /home/labex/project
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
```

在容器中输入命令：

```
echo "hello busybox" > /data/hi.txt
exit
```

验证文件是否在主机上创建。

```
cat data/hi.txt
```
