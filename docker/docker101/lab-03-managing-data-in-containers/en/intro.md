# Introduction

By default all files created inside a container are stored on a writable container layer. That means that:

- If the container no longer exists, the data is lost,
- The container's writable layer is tightly coupled to the host machine, and
- To manage the file system, you need a storage driver that provides a union file system, using the Linux kernel. This extra abstraction reduces performance compared to `data volumes` which write directly to the filesystem.

Docker provides two options to store files in the host machine: `volumes` and `bind mounts`. If you're running Docker on Linux, you can also use a `tmpfs mount`, and with Docker on Windows you can also use a `named pipe`.

![Types of Mounts](../assets/types-of-mounts.png)

- `Volumes` are stored in the host filesystem that is managed by Docker.
- `Bind mounts` are stored anywhere on the host system.
- `tmpfs mounts` are stored in the host memory only.

Originally, the `--mount` flag was used for Docker Swarm services and the `--volume` flag was used for standalone containers. From Docker 17.06 and higher, you can also use `--mount` for standalone containers and it is in general more explicit and verbose than `--volume`.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
This is a Guided Lab, which provides step-by-step instructions to help you learn and practice. Follow the instructions carefully to complete each step and gain hands-on experience. Historical data shows that this is a <span class="text-green-600 dark:text-green-400">beginner</span> level lab with a <span class="text-green-600 dark:text-green-400">100%</span> completion rate.
</div>
