# Filesystem exploration

We first stop and remove all containers from your host (you might not be able to remove images if containers are using some of the layers).

```bash
docker container stop $(docker container ls -aq)
docker container rm $(docker container ls -aq)
```

Note: containers can also be removed in a non graceful way:

```
docker container rm -f $(docker container ls -aq)
```

We also remove all the images

```bash
docker image rm $(docker image ls -q)
```

We will now have a look inside the **/var/lib/docker/overlay2** folder where the image and container layers are stored.

```bash
ls /var/lib/docker/overlay2
```

As we do not have any images yet, there should not be anything in this folder.

Let's pull an nginx image

```bash
docker image pull nginx
```

You should get something like the following where we can see that 3 layers are pulled.

```
Using default tag: latest
latest: Pulling from library/nginx
5040bd298390: Pull complete
d7a91cdb22f0: Pull complete
9cac4850e5df: Pull complete
Digest: sha256:33ff28a2763feccc1e1071a97960b7fef714d6e17e2d0ff573b74825d0049303
Status: Downloaded newer image for nginx:latest
```

If we have a look to the changes that occurs in the /var/lib/docker/overlay2 folder

```bash
ls /var/lib/docker/overlay2
```

we can see the following:

```
261fed39e3aca63326758681c96cad5bfe7eeeabafda23408bee0f5ae365d3fd
28f7998921ca5e4b28231b59b619394ba73571b5127a9c28cc9bacb3db706d2a
backingFsBlockDev
c1ae1be1c1c62dbaacf26bb9a5cde02e30d5364e06a437d0626f31c55af82a58
l
```

Some folders, with names that looks like hash, were created. Those are the layers which, merged together, build the image filesystem.

Let's run a container based on nginx.

```bash
docker container run -d nginx
```

We can now see 2 additional folders (ID, ID-init), those ones correspond to the read-write layer of the running container.

```
11995e6da1dc5acab33aceacea3656d3795a4fb136c3a65b37d40b97747b5f84
11995e6da1dc5acab33aceacea3656d3795a4fb136c3a65b37d40b97747b5f84-init
261fed39e3aca63326758681c96cad5bfe7eeeabafda23408bee0f5ae365d3fd
28f7998921ca5e4b28231b59b619394ba73571b5127a9c28cc9bacb3db706d2a
backingFsBlockDev
c1ae1be1c1c62dbaacf26bb9a5cde02e30d5364e06a437d0626f31c55af82a58
l
```

Feel free to go into those folder and explore their filesystems.
