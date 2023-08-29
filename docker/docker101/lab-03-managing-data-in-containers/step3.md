# [Optional] OverlayFS

OverlayFS is a `union mount filesystem` implementation for Linux. To understand what a Docker volume is, it helps to understand how layers and the filesystem work in Docker.

To start a container, Docker takes the read-only image and creates a new read-write layer on top. To view the layers as one, Docker uses a Union File System or OverlayFS (Overlay File System), specifically the `overlay2` storage driver.

To see Docker host managed files, you need access to the Docker process file system. Using the `--privileged` and `--pid=host` flags you can access the host's process ID namespace from inside a container like `busybox`. You can then browse to Docker's `/var/lib/docker/overlay2` directory to see the downloaded layers that are managed by Docker.

To view the current list of layers in Docker,

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------    3 root     root          4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------    5 root     root          4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------    4 root     root          4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------    2 root     root          4096 Sep 25 19:44 l

/ # exit
```

Pull down the `ubuntu` image and check again,

```bash
$ docker pull ubuntu
Using default tag: latest
latest: Pulling from library/ubuntu
e6ca3592b144: Pull complete
534a5505201d: Pull complete
990916bd23bb: Pull complete
Digest: sha256:cbcf86d7781dbb3a6aa2bcea25403f6b0b443e20b9959165cf52d2cc9608e4b9
Status: Downloaded newer image for ubuntu:latest

$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2/
total 36
drwx------    3 root     root          4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------    4 root     root          4096 Sep 25 19:45 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------    4 root     root          4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------    4 root     root          4096 Sep 25 19:46 a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
drwx------    3 root     root          4096 Sep 25 19:46 d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
drwx------    4 root     root          4096 Sep 25 19:46 dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
drwx------    5 root     root          4096 Sep 25 19:47 f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709
drwx------    4 root     root          4096 Sep 25 19:47 f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709-init
drwx------    2 root     root          4096 Sep 25 19:47 l

/ # exit
```

You see that pulling down the `ubuntu` image, implicitly pulled down 4 new layers,

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

The `overlay2` storage driver in essence layers different directories on the host and presents them as a single directory.

- base layer or lowerdir,
- `diff` layer or upperdir,
- overlay layer (user view), and
- `work` dir.

OverlayFS refers to the lower directories as `lowerdir`, which contains the base image and the read-only (R/O) layers that are pulled down.

The upper directory is called `upperdir` and is the read-write (R/W) container layer.

The unified view or `overlay` layer is called `merged`.

Finally, a `workdir` is a required, which is an empty directory used by overlay for internal use.

The `overlay2` driver supports up to 128 lower OverlayFS layers. The `l` directory contains shortened layer identifiers as symbolic links.

![Overlay2 Storage Driver](./assets/overlay2-driver.png)

Cleanup,

```bash
docker system prune -a
clear
```
