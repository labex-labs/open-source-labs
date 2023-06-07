# What You Will Learn

You'll learn how to:

- run a local registry in a container and configure your Docker engine to use the registry;

- generate SSL certificates (using Docker!) and run a secure local registry with a friendly domain name;

- generate encrypted passwords (using Docker!) and run an authenticated, secure local registry over HTTPS with basic auth.

> Note. The open-source registry does not have a Web UI, so there's no interface like [Docker Hub](https://hub.docker.com) or [Docker Store](https://store.docker.com). Instead there is a [REST API](https://docs.docker.com/registry/spec/api/) you can use to query the registry. For a local registry which has a Web UI and role-based access control, Docker, Inc. has the [Trusted Registry](https://www.docker.com/sites/default/files/Docker%20Trusted%20Registry.pdf) product.

You'll need Docker running on in this tutorial, or on a Linux machine and be familiar with the key Docker concepts, and with Docker volumes:

- [Docker concepts](https://docs.docker.com/engine/understanding-docker/)
- [Docker volumes](https://docs.docker.com/engine/tutorials/dockervolumes/)

# Part 1 - Running a Registry Container in Linux

There are several ways to run a registry container. The simplest is to run an insecure registry over HTTP, but for that we need to configure Docker to explicitly allow insecure access to the registry.

Docker expects all registries to run on HTTPS. The next section of this lab will introduce a secure version of our registry container, but for this part of the tutorial we will run a version on HTTP. When registering a image, Docker returns an error message like this:

```
http: server gave HTTP response to HTTPS client
```

The Docker Engine needs to be explicitly setup to use HTTP for the insecure registry. For this sample it has already been done, `127.0.0.1:5000` has already been added to the daemon.

**_ Running on your own Linux machine instead of in this browser window _**
Edit or create `/etc/docker/docker` file:

```
vi /etc/docker/docker

# add this line
DOCKER_OPTS="--insecure-registry 127.0.0.1:5000"
```

Close and save the file, then restart the docker daemon.

```bash
pkill dockerd
dockerd > /dev/null 2>&1 &
```

**_ If you're running on your own Mac or Windows machine instead of in this browser window _**
In Docker for Mac, the `Preferences` menu lets you set the address for an insecure registry under the `Daemon` panel:
![MacOS menu](/images/docker_osx_insecure_registry.png)

In Docker for Windows, the `Settings` menu lets you set the address for an insecure registry under the `Daemon` panel:
![MacOS menu](/images/docker_windows_insecure_registry.png)
