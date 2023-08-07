# Mount host's folder into a container

The last item we will talk about is named bind-mount and consist of mounting a host's folder into a container's folder. This is done using the **-v** option of the **docker container run** command. Instead of specifying one single path (as we did when defining volumes) we will specified 2 paths separated by a column.

```
docker container run -v HOST_PATH:CONTAINER_PATH [OPTIONS] IMAGE [CMD]
```

Note: HOST_PATH and CONTAINER_PATH can be a folder or file. None of the Paths have to exist before starting the Container as they will be created automatically during the start.

## 1st case

Let's run an alpine container bind mounting the local /tmp folder inside the container /data folder.

```bash
docker container run -ti -v /tmp:/data alpine sh
```

We end up in a shell inside our container. By default, there is no /data folder in an alpine distribution. What is the impact of the bind-mount ?

```bash
ls /data
```

The /data folder has been created inside the container and it contains the content of the /tmp folder of the host. We can now, from the container, change files on the host and the other way round.

## 2nd case

Let's run a nginx container bind mounting the local /tmp folder inside the /usr/share/nginx/html folder of the container.

```bash
docker container run -ti -v /tmp:/usr/share/nginx/html nginx bash
```

Are the default index.html and 50x.html files still there in the container's /usr/share/nginx/html folder ?

```bash
ls /usr/share/nginx/html
```

No ! The content of the container's folder has been overridden with the content of the host folder.

**Bind-mounting** is very usefull in development as it enables, for instance, to share source code on the host with the container.
