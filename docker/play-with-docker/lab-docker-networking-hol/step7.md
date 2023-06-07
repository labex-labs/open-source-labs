# Step 2: Connect a container

The **bridge** network is the default network for new containers. This means that unless you specify a different network, all new containers will be connected to the **bridge** network.

Create a new container by running `docker run -dt ubuntu sleep infinity`.

```bash
docker run -dt ubuntu sleep infinity
```

```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
d54efb8db41d: Pull complete
f8b845f45a87: Pull complete
e8db7bf7c39f: Pull complete
9654c40e9079: Pull complete
6d9ef359eaaa: Pull complete
Digest: sha256:dd7808d8792c9841d0b460122f1acf0a2dd1f56404f8d1e56298048885e45535
Status: Downloaded newer image for ubuntu:latest
846af8479944d406843c90a39cba68373c619d1feaa932719260a5f5afddbf71
```

This command will create a new container based on the `ubuntu:latest` image and will run the `sleep` command to keep the container running in the background. You can verify our example container is up by running `docker ps`.

```bash
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
846af8479944        ubuntu              "sleep infinity"    55 seconds ago      Up 54 seconds                           heuristic_boyd
```

As no network was specified on the `docker run` command, the container will be added to the **bridge** network.

Run the `brctl show` command again.

```bash
brctl show
```

```
bridge name	bridge id		STP enabled	interfaces
docker0		8000.024252ed52f7	no		vethd630437
```

Notice how the **docker0** bridge now has an interface connected. This interface connects the **docker0** bridge to the new container just created.

You can inspect the **bridge** network again, by running `docker network inspect bridge`, to see the new container attached to it.

```bash
docker network inspect bridge
```

```
<Snip>
        "Containers": {
            "846af8479944d406843c90a39cba68373c619d1feaa932719260a5f5afddbf71": {
                "Name": "heuristic_boyd",
                "EndpointID": "1265c418f0b812004d80336bafdc4437eda976f166c11dbcc97d365b2bfa91e5",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
<Snip>
```
