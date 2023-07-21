# Container Isolation

In the steps above we ran several commands via container instances with the help of `docker container run`. The `docker container ls -a` command showed us that there were several containers listed. Why are there so many containers listed if they are all from the _alpine_ image?

This is a critical security concept in the world of Docker containers! Even though each `docker container run` command used the same alpine **_image_**, each execution was a separate, isolated **_container_**. Each container has a separate filesystem and runs in a different namespace; by default a container has no way of interacting with other containers, even those from the same image. Let's try another exercise to learn more about isolation.

```bash
docker container run -it alpine /bin/ash
```

The `/bin/ash` is another type of shell available in the alpine image. Once the container launches and you are at the container's command prompt type the following commands:

```
 echo "hello world" > hello.txt

 ls
```

The first `echo` command creates a file called "hello.txt" with the words "hello world" inside it. The second command gives you a directory listing of the files and should show your newly created "hello.txt" file. Now type `exit` to leave this container.

To show how isolation works, run the following:

```bash
docker container run alpine ls
```

It is the same `ls` command we used inside the container's interactive ash shell, but this time, did you notice that your "hello.txt" file is missing? That's isolation! Your command ran in a new and separate _instance_, even though it is based on the same _image_. The 2nd instance has no way of interacting with the 1st instance because the Docker Engine keeps them separated and we have not setup any extra parameters that would enable these two instances to interact.

In every day work, Docker users take advantage of this feature not only for security, but to test the effects of making application changes. Isolation allows users to quickly create separate, isolated test copies of an application or service and have them run side-by-side without interfering with one another. In fact, there is a whole lifecycle where users take their changes and move them up to production using this basic concept and the built-in capabilities of Docker Enteprise. We will explore more of that in later exercises.

Right now, the obvious question is "how do I get back to the container that has my 'hello.txt' file?"

Once again run the

```bash
docker container ls -a
```

command again and you should see output similar to the following:

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
36171a5da744        alpine              "ls"                     2 minutes ago       Exited (0) 2 minutes ago                        distracted_bhaskara
3030c9c91e12        alpine              "/bin/ash"               5 minutes ago       Exited (0) 2 minutes ago                        fervent_newton
a6a9d46d0b2f        alpine             "echo 'hello from alp"    6 minutes ago       Exited (0) 6 minutes ago                        lonely_kilby
ff0a5c3750b9        alpine             "ls -l"                   8 minutes ago       Exited (0) 8 minutes ago                        elated_ramanujan
c317d0a9e3d2        hello-world         "/hello"                 34 seconds ago      Exited (0) 12 minutes ago                       stupefied_mcclintock
```

Graphically this is what happened on our Docker Engine:
![Docker container isolation](/images/ops-basics-isolation.svg)

The container in which we created the "hello.txt" file is the same one where we used the `/bin/ash` shell, which we can see listed in the "COMMAND" column. The _Container ID_ number from the first column uniquely identifies that particular container instance. In the sample output above the container ID is `3030c9c91e12`. We can use a slightly different command to tell Docker to run this specific container instance. Try typing:

```
docker container start <container ID>
```

- **Pro tip:** Instead of using the full container ID you can use just the first few characters, as long as they are enough to uniquely ID a container. So we could simply use "3030" to identify the container instance in the example above, since no other containers in this list start with these characters.

Now use the `docker container ls` command again to list the running containers.

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
3030c9c91e12        alpine              "/bin/ash"                2 minutes ago       Up 14 seconds                        distracted_bhaskara
```

Notice this time that our container instance is still running. We used the ash shell this time so the rather than simply exiting the way /bin/sh did earlier, ash waits for a command. We can send a command in to the container to run by using the `exec` command, as follows:

```
docker container exec <container ID> ls
```

This time we get a directory listing and it shows our "hello.txt" file because we used the container instance where we created that file.

![Docker container exec command](/images/ops-basics-exec.svg)

Now you are starting to see some of the important concepts of containers. In the next exercise we will start to see how you can create your own Docker images and how to use a Dockerfile to standardize images such that you can create larger, more complex images in a simple, automated manner.

## Terminology

In the last section, you saw a lot of Docker-specific jargon which might be confusing to some. So before you go further, let's clarify some terminology that is used frequently in the Docker ecosystem.

- _Images_ - The file system and configuration of our application which are used to create containers. To find out more about a Docker image, run `docker image inspect alpine`. In the demo above, you used the `docker image pull` command to download the **alpine** image. When you executed the command `docker container run hello-world`, it also did a `docker image pull` behind the scenes to download the **hello-world** image.
- _Containers_ - Running instances of Docker images &mdash; containers run the actual applications. A container includes an application and all of its dependencies. It shares the kernel with other containers, and runs as an isolated process in user space on the host OS. You created a container using `docker run` which you did using the alpine image that you downloaded. A list of running containers can be seen using the `docker container ls` command.
- _Docker daemon_ - The background service running on the host that manages building, running and distributing Docker containers.
- _Docker client_ - The command line tool that allows the user to interact with the Docker daemon.
- _Docker Hub_ - Store is, among other things, a [registry](https://store.docker.com/) of Docker images. You can think of the registry as a directory of all available Docker images. You'll be using this later in this tutorial.

{:.quiz}
Where do images get pulled from by default when not found locally?

- ( ) Docker Trusted Registry
- (x) Docker Hub
- ( ) There is no default
- ( ) Docker Store

{:.quiz}
Which command lists your Docker images?

- (x) docker image ls
- ( ) docker run
- ( ) docker container ls
