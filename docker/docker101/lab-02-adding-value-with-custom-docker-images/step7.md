# Step 7: Clean up

Completing this lab results in a bunch of running containers on your host. Let's clean these up.

Run `docker container stop [container id]` for each container that is running

First get a list of the containers running using `docker container ls`.

```bash
$ docker container ls
CONTAINER ID        IMAGE                COMMAND             CREATED             STATUS              PORTS                    NAMES
0b2ba61df37f        python-hello-world   "python app.py"     7 minutes ago       Up 7 minutes        0.0.0.0:5001->5000/tcp   practical_kirch
```

Then run `docker container stop [container id]` for each container in the list.

```bash
$ docker container stop 0b2
0b2
```

Remove the stopped containers

`docker system prune` is a really handy command to clean up your system. It will remove any stopped containers, unused volumes and networks, and dangling images.

```bash
$ docker system prune
WARNING! This will remove:
         - all stopped containers
         - all volumes not used by at least one container
         - all networks not used by at least one container
         - all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Total reclaimed space: 300.3kB
```
