# Usage of the Volume API

The volume API introduced in Docker 1.9 enables to perform operations on volume very easily.

First have a look at the commands available in the volume API.

```bash
docker volume --help
```

We will start with the create command, and create a volume named `html`.

```bash
docker volume create --name html
```

If we list the existing volume, our `html` volume should be the only one.

```bash
docker volume ls
```

The output should be something like

```
DRIVER              VOLUME NAME
[other previously created volumes]
local               html
```

In the volume API, like for almost all the other Docker's API, there is an `inspect` command. Let's use it against the `html` volume.

```bash
docker volume inspect html
```

The output should be the following one.

```
[
    {
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/html/_data",
        "Name": "html",
        "Options": {},
        "Scope": "local"
    }
]
```

The `Mountpoint` defined here is the path on the Docker host where the volume can be accessed. We can note that this path uses the name of the volume instead of the auto-generated ID we saw in the example above.

We can now use this volume and mount it on a specific path of a container. We will use a Nginx image and mount the `html` volume onto `/usr/share/nginx/html` folder within the container.

> Note: `/usr/share/nginx/html` is the default folder served by nginx. It contains 2 files: `index.html` and `50x.html`

```bash
docker run --name www -d -p 8080:80 -v html:/usr/share/nginx/html nginx
```

> Note: we use the `-p` option to map the nginx default port (80) to a port on the host (8080). We will come back to this in the lesson dedicated to the networking.

From the host, let's have a look at the content of the volume.

```bash
sudo ls /var/lib/docker/volumes/html/_data
```

The content of the `/usr/share/nginx/html` folder of the `www` container has been copied into the `/var/lib/docker/volumes/html/\_data` folder on the host.

Let's have a look at the nginx's [welcome page](/){:data-term=".term1"}{:data-port="8080"}
