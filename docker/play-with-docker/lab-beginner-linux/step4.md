# Run a background MySQL container

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
