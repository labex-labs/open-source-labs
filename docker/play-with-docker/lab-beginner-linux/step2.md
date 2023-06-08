# Run some simple Docker containers

There are different ways to use containers. These include:

1. **To run a single task:** This could be a shell script or a custom app.
2. **Interactively:** This connects you to the container similar to the way you SSH into a remote server.
3. **In the background:** For long-running services like websites and databases.

In this section you'll try each of those options and see how Docker manages the workload.

## Run a single task in an Alpine Linux container

In this step we're going to start a new container and tell it to run the `hostname` command. The container will start, execute the `hostname` command, then exit.

1. Run the following command in your Linux console.

   ```bash
   docker container run alpine hostname
   ```

   The output below shows that the `alpine:latest` image could not be found locally. When this happens, Docker automatically _pulls_ it from Docker Hub.

   After the image is pulled, the container's hostname is displayed (`888e89a3b36b` in the example below).

   ```
   Unable to find image 'alpine:latest' locally
   latest: Pulling from library/alpine
   88286f41530e: Pull complete
   Digest: sha256:f006ecbb824d87947d0b51ab8488634bf69fe4094959d935c0c103f4820a417d
   Status: Downloaded newer image for alpine:latest
   888e89a3b36b
   ```

2. Docker keeps a container running as long as the process it started inside the container is still running. In this case the `hostname` process exits as soon as the output is written. This means the container stops. However, Docker doesn't delete resources by default, so the container still exists in the `Exited` state.

   List all containers.

   ```bash
   docker container ls --all
   ```

   Notice that your Alpine Linux container is in the `Exited` state.

   ```
   CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS            PORTS               NAMES
   888e89a3b36b        alpine              "hostname"          50 seconds ago      Exited (0) 49 seconds ago                       awesome_elion
   ```

   > **Note:** The container ID _is_ the hostname that the container displayed. In the example above it's `888e89a3b36b`.

Containers which do one task and then exit can be very useful. You could build a Docker image that executes a script to configure something. Anyone can execute that task just by running the container - they don't need the actual scripts or configuration information.

## Run an interactive Ubuntu container

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

## Run a background MySQL container

Background containers are how you'll run most applications. Here's a simple example using MySQL.

1. Run a new MySQL container with the following command.

   ```bash
   docker container run \
   --detach \
   --name mydb \
   -e MYSQL_ROOT_PASSWORD=my-secret-pw \
   mysql:latest
   ```

   - `--detach` will run the container in the background.
   - `--name` will name it **mydb**.
   - `-e` will use an environment variable to specify the root password (NOTE: This should never be done in production).

   As the MySQL image was not available locally, Docker automatically pulled it from Docker Hub.

   ```
   Unable to find image 'mysql:latest' locallylatest: Pulling from library/mysql
   aa18ad1a0d33: Pull complete
   fdb8d83dece3: Pull complete
   75b6ce7b50d3: Pull complete
   ed1d0a3a64e4: Pull complete
   8eb36a82c85b: Pull complete
   41be6f1a1c40: Pull complete
   0e1b414eac71: Pull complete
   914c28654a91: Pull complete
   587693eb988c: Pull complete
   b183c3585729: Pull complete
   315e21657aa4: Pull complete
   Digest: sha256:0dc3dacb751ef46a6647234abdec2d47400f0dfbe77ab490b02bffdae57846ed
   Status: Downloaded newer image for mysql:latest
   41d6157c9f7d1529a6c922acb8167ca66f167119df0fe3d86964db6c0d7ba4e0
   ```

   As long as the MySQL process is running, Docker will keep the container running in the background.

2. List the running containers.

   ```bash
   docker container ls
   ```

   Notice your container is running.

   ```
   CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS            NAMES
   3f4e8da0caf7        mysql:latest        "docker-entrypoint..."   52 seconds ago      Up 51 seconds       3306/tcp            mydb
   ```

3. You can check what's happening in your containers by using a couple of built-in Docker commands: `docker container logs` and `docker container top`.

   ```bash
   docker container logs mydb
   ```

   This shows the logs from the MySQL Docker container.

   ```
     <output truncated>
     2017-09-29T16:02:58.605004Z 0 [Note] Executing 'SELECT * FROM INFORMATION_SCHEMA.TABLES;' to get a list of tables using the deprecated partition engine. You may use the startup option '--disable-partition-engine-check' to skip this check.
     2017-09-29T16:02:58.605026Z 0 [Note] Beginning of list of non-natively partitioned tables
     2017-09-29T16:02:58.616575Z 0 [Note] End of list of non-natively partitioned tables
   ```

   Let's look at the processes running inside the container.

   ```bash
     docker container top mydb
   ```

   You should see the MySQL daemon (`mysqld`) is running in the container.

   ```
   PID                 USER                TIME                COMMAND
   2876                999                 0:00                mysqld
   ```

   Although MySQL is running, it is isolated within the container because no network ports have been published to the host. Network traffic cannot reach containers from the host unless ports are explicitly published.

4. List the MySQL version using `docker container exec`.

   `docker container exec` allows you to run a command inside a container. In this example, we'll use `docker container exec` to run the command-line equivalent of `mysql --user=root --password=$MYSQL_ROOT_PASSWORD --version` inside our MySQL container.

   ```bash
   docker exec -it mydb \
   mysql --user=root --password=$MYSQL_ROOT_PASSWORD --version
   ```

   You will see the MySQL version number, as well as a handy warning.

   ```
   mysql: [Warning] Using a password on the command line interface can be insecure.
   mysql  Ver 14.14 Distrib 5.7.19, for Linux (x86_64) using  EditLine wrapper
   ```

5. You can also use `docker container exec` to connect to a new shell process inside an already-running container. Executing the command below will give you an interactive shell (`sh`) inside your MySQL container.

   ```bash
   docker exec -it mydb sh
   ```

   Notice that your shell prompt has changed. This is because your shell is now connected to the `sh` process running inside of your container.

6. Let's check the version number by running the same command again, only this time from within the new shell session in the container.

   ```bash
   mysql --user=root --password=$MYSQL_ROOT_PASSWORD --version
   ```

   Notice the output is the same as before.

7. Type `exit` to leave the interactive shell session.

   ```bash
   exit
   ```
