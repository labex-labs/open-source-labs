# Run an interactive Ubuntu container

You can run a container based on a different version of Linux than is running on your Docker host.

In the next example, we are going to run an Ubuntu Linux container on top of an Alpine Linux Docker host (Play With Docker uses Alpine Linux for its nodes).

1. Run a Docker container and access its shell.

   ```bash
   docker container run --interactive --tty --rm ubuntu bash
   ```

   In this example, we're giving Docker three parameters:

   - `--interactive` says you want an interactive session.
   - `--tty` allocates a pseudo-tty.
   - `--rm` tells Docker to go ahead and remove the container when it's done executing.

   The first two parameters allow you to interact with the Docker container.

   We're also telling the container to run `bash` as its main process (PID 1).

   When the container starts you'll drop into the bash shell with the default prompt `root@<container id>:/#`. Docker has attached to the shell in the container, relaying input and output between your local session and the shell session in the container.

2. Run the following commands in the container.

   `ls /` will list the contents of the root directory in the container, `ps aux` will show running processes in the container, `cat /etc/issue` will show which Linux distro the container is running, in this case Ubuntu 20.04.3 LTS.

   ```bash
   ls /
   ```

   ```bash
   ps aux
   ```

   ```bash
   cat /etc/issue
   ```

3. Type `exit` to leave the shell session. This will terminate the `bash` process, causing the container to exit.

   ```bash
   exit
   ```

   > **Note:** As we used the `--rm` flag when we started the container, Docker removed the container when it stopped. This means if you run another `docker container ls --all` you won't see the Ubuntu container.

4. For fun, let's check the version of our host VM.

   ```bash
   cat /etc/issue
   ```

   You should see:

   ```
   Welcome to Alpine Linux 3.8
   Kernel \r on an \m (\l)
   ```

Notice that our host VM is running Alpine Linux, yet we were able to run an Ubuntu container. As previously mentioned, the distribution of Linux inside the container does not need to match the distribution of Linux running on the Docker host.

However, Linux containers require the Docker host to be running a Linux kernel. For example, Linux containers cannot run directly on Windows Docker hosts. The same is true of Windows containers - they need to run on a Docker host with a Windows kernel.

Interactive containers are useful when you are putting together your own image. You can run a container and verify all the steps you need to deploy your app, and capture them in a Dockerfile.

> You _can_ [commit](https://docs.docker.com/engine/reference/commandline/commit/) a container to make an image from it - but you should avoid that wherever possible. It's much better to use a repeatable [Dockerfile](https://docs.docker.com/engine/reference/builder/) to build your image. You'll see that shortly.
