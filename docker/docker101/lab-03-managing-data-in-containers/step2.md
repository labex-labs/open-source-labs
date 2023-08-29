# Bind Mounts

The `mount` syntax is recommended by Docker over the `volume` syntax. Bind mounts have limited functionality compared to volumes. A file or directory is referenced by its full path on the host machine when mounted into a container. Bind mounts rely on the host machine’s filesystem having a specific directory structure available and you cannot use the Docker CLI to manage bind mounts. Note that bind mounts can change the host filesystem via processes running in a container.

Instead of using the `-v` syntax with three fields separated by colon separator (:), the `mount` syntax is more verbose and uses multiple `key-value` pairs:

- type: bind, volume or tmpfs,
- source: path to the file or directory on host machine,
- destination: path in container,
- readonly,
- bind-propagation: rprivate, private, rshared, shared, rslave, slave,
- consistency: consistent, delegated, cached,
- mount.

```bash
mkdir data
docker run -it --name busybox --mount type=bind,source="$(pwd)"/data,target=/data busybox sh
/ # echo "hello busybox" > /data/hi.txt
/ # exit
cat data/hi.txt
```
