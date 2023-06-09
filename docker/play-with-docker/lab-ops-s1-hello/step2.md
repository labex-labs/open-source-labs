# Docker Images

In this rest of this lab, you are going to run an [Alpine Linux](http://www.alpinelinux.org/) container. Alpine is a lightweight Linux distribution so it is quick to pull down and run, making it a popular starting point for many other images.

To get started, let's run the following in our terminal:

```bash
docker image pull alpine
```

The `pull` command fetches the alpine **image** from the **Docker registry** and saves it in our system. In this case the registry is **[Docker Hub](https://hub.docker.com)**. You can change the registry, but that's a different lab.

You can use the `docker image` command to see a list of all images on your system.

```bash
docker image ls
```

```
REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
alpine                 latest              c51f86c28340        4 weeks ago         1.109 MB
hello-world             latest              690ed74de00f        5 months ago        960 B
```
