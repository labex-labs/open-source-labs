# Step 1: Run your first container

We are going to use the Docker CLI to run our first container.

1. Open a terminal on your local computer

1. Run `docker container run -t ubuntu top`

   Use the `docker container run` command to run a container with the ubuntu image using the `top` command. The `-t` flags allocate a pseudo-TTY which we need for the `top` to work correctly.

   ```bash
   $ docker container run -it ubuntu top
   Unable to find image 'ubuntu:latest' locally
   latest: Pulling from library/ubuntu
   aafe6b5e13de: Pull complete
   0a2b43a72660: Pull complete
   18bdd1e546d2: Pull complete
   8198342c3e05: Pull complete
   f56970a44fd4: Pull complete
   Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
   Status: Downloaded newer image for ubuntu:latest
   ```

   The `docker run` command will result first in a `docker pull` to download the ubuntu image onto your host. Once it is downloaded, it will start the container. The output for the running container should look like this:

   ```bash
   top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
   Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
   %Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
   KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
   KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

   PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
       1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
   ```

   `top` is a linux utility that prints the processes on a system and orders them by resource consumption. Notice that there is only a single process in this output: it is the `top` process itself. We don't see other processes from our host in this list because of the PID namespace isolation.

   Containers use linux namespaces to provide isolation of system resources from other containers or the host. The PID namespace provides isolation for process IDs. If you run `top` while inside the container, you will notice that it shows the processes within the PID namespace of the container, which is much different than what you can see if you ran `top` on the host.

   Even though we are using the `ubuntu` image, it is important to note that our container does not have its own kernel. Its uses the kernel of the host and the `ubuntu` image is used only to provide the file system and tools available on an ubuntu system.

1. Inspect the container with `docker container exec`

   The `docker container exec` command is a way to "enter" a running container's namespaces with a new process.

   Open a new terminal. On cognitiveclass.ai, select `Terminal` > `New Terminal`.

   Using play-with-docker.com, to open a new terminal connected to node1, click "Add New Instance" on the lefthand side, then ssh from node2 into node1 using the IP that is listed by 'node1 '. For example:

   ```bash
   [node2] (local) root@192.168.0.17 ~
   $ ssh 192.168.0.18
   [node1] (local) root@192.168.0.18 ~
   $
   ```

   In the new terminal, use the `docker container ls` command to get the ID of the running container you just created.

   ```bash
   $ docker container ls
   CONTAINER ID        IMAGE                      COMMAND                  CREATED             STATUS                         PORTS                       NAMES
   b3ad2a23fab3        ubuntu                     "top"                    29 minutes ago      Up 29 minutes                                              goofy_nobel
   ```

   Then use that id to run `bash` inside that container using the `docker container exec` command. Since we are using bash and want to interact with this container from our terminal, use `-it` flags to run using interactive mode while allocating a psuedo-terminal.

   ```bash
   $ docker container exec -it b3ad2a23fab3 bash
   root@b3ad2a23fab3:/#
   ```

   And Voila! We just used the `docker container exec` command to "enter" our container's namespaces with our bash process. Using `docker container exec` with `bash` is a common pattern to inspect a docker container.

   Notice the change in the prefix of your terminal. e.g. `root@b3ad2a23fab3:/`. This is an indication that we are running bash "inside" of our container.

   **Note**: This is not the same as ssh'ing into a separate host or a VM. We don't need an ssh server to connect with a bash process. Remember that containers use kernel-level features to achieve isolation and that containers run on top of the kernel. Our container is just a group of processes running in isolation on the same host, and we can use `docker container exec` to enter that isolation with the `bash` process. After running `docker container exec`, the group of processes running in isolation (i.e. our container) include `top` and `bash`.

   From the same termina, run `ps -ef` to inspect the running processes.

   ```bash
   root@b3ad2a23fab3:/# ps -ef
   UID        PID  PPID  C STIME TTY          TIME CMD
   root         1     0  0 20:34 ?        00:00:00 top
   root        17     0  0 21:06 ?        00:00:00 bash
   root        27    17  0 21:14 ?        00:00:00 ps -ef
   ```

   You should see only the `top` process, `bash` process and our `ps` process.

   For comparison, exit the container, and run `ps -ef` or `top` on the host. These commands will work on linux or mac. For windows, you can inspect the running processes using `tasklist`.

   ```bash
   root@b3ad2a23fab3:/# exit
   exit
   $ ps -ef
   # Lots of processes!
   ```

   _Technical Deep Dive_
   PID is just one of the linux namespaces that provides containers with isolation to system resources. Other linux namespaces include:

   - MNT - Mount and unmount directories without affecting other namespaces
   - NET - Containers have their own network stack
   - IPC - Isolated interprocess communication mechanisms such as message queues.
   - User - Isolated view of users on the system
   - UTC - Set hostname and domain name per container

   These namespaces together provide the isolation for containers that allow them to run together securely and without conflict with other containers running on the same system. Next, we will demonstrate different uses of containers. and the benefit of isolation as we run multiple containers on the same host.

   **Note**: Namespaces are a feature of the **linux** kernel. But Docker allows you to run containers on Windows and Mac... how does that work? The secret is that embedded in the Docker product or Docker engine is a linux subsystem. Docker open-sourced this linux subsystem to a new project: [LinuxKit](https://github.com/linuxkit/linuxkit). Being able to run containers on many different platforms is one advantage of using the Docker tooling with containers.

   In addition to running linux containers on Windows using a linux subsystem, native Windows containers are now possible due the creation of container primitives on the Windows OS. Native Windows containers can be run on Windows 10 or Windows Server 2016 or newer.

   **Note**: if you run this exercise in a containerized terminal and execute the `ps -ef` command in the terminal, e.g. in `https://labs.cognitiveclass.ai`, you will still see a limited set of processes after exiting the `exec` command. You can try to run the `ps -ef` command in a terminal on your local machine to see all processes.

1. Clean up the container running the `top` processes by typing: `<ctrl>-c`, list all containers and remove the containers by their id.

   ```bash
   docker ps -a

   docker rm <CONTAINER ID>
   ```
