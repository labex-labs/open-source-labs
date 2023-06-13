# Docker Container Run

Great! Let's now run a Docker **container** based on this image. To do that you are going to use the `docker container run` command.

```bash
docker container run alpine ls -l
```

```
total 48
drwxr-xr-x    2 root     root          4096 Mar  2 16:20 bin
drwxr-xr-x    5 root     root           360 Mar 18 09:47 dev
drwxr-xr-x   13 root     root          4096 Mar 18 09:47 etc
drwxr-xr-x    2 root     root          4096 Mar  2 16:20 home
drwxr-xr-x    5 root     root          4096 Mar  2 16:20 lib
......
......
```

While the output of the `ls` command may not be all that exciting, behind the scenes quite a few things just took place. When you call `run`, the Docker client finds the image (alpine in this case), creates the container and then runs a command in that container. When you run `docker container run alpine`, you provided a command (`ls -l`), so Docker executed this command inside the container for which you saw the directory listing. After the `ls` command finished, the container shut down.

![docker run explainer](/images/ops-basics-run-details.svg)

The fact that the container exited after running our command is important, as you will start to see. Let's try something more exciting. Type in the following:

```bash
docker container run alpine echo "hello from alpine"
```

And you should get the following output:

```
hello from alpine
```

In this case, the Docker client dutifully ran the `echo` command inside our alpine container and then exited. If you noticed, all of that happened pretty quickly and again our container exited. As you will see in a few more steps, the `echo` command ran in a separate container instance. Imagine booting up a virtual machine (VM), running a command and then killing it; it would take a minute or two just to boot the VM before running the command. A VM has to emulate a full hardware stack, boot an operating system, and then launch your app - it's a virtualized _hardware_ environment. Docker containers function at the application layer so they skip most of the steps VMs require and just run what is required for the app. Now you know why they say containers are fast!

Try another command.

```bash
docker container run alpine /bin/sh
```

Wait, nothing happened! Is that a bug? No! In fact, something did happen. You started a 3rd instance of the alpine container and it ran the command `/bin/sh` and then exited. You did not supply any additional commands to `/bin/sh` so it just launched the shell, exited the shell, and then stopped the container. What you might have _expected_ was an interactive shell where you could type some commands. Docker has a facility for that by adding a flag to run the container in an interactive terminal. For this example, type the following:

```bash
 docker container run -it alpine /bin/sh
```

You are now inside the container running a Linux shell and you can try out a few commands like `ls -l`, `uname -a` and others. Note that Alpine is a small Linux OS so several commands might be missing. Exit out of the shell and container by typing the `exit` command.

Ok, we said that we had run each of our commands above in a separate container instance. We can see these instances using the `docker container ls` command. The `docker container ls` command by itself shows you all containers that are currently running:

```bash
docker container ls
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

Since no containers are running, you see a blank line. Let's try a more useful variant: `docker container ls -a`

```bash
docker container ls -a
```

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
36171a5da744        alpine              "/bin/sh"                5 minutes ago       Exited (0) 2 minutes ago                        fervent_newton
a6a9d46d0b2f        alpine             "echo 'hello from alp"    6 minutes ago       Exited (0) 6 minutes ago                        lonely_kilby
ff0a5c3750b9        alpine             "ls -l"                   8 minutes ago       Exited (0) 8 minutes ago                        elated_ramanujan
c317d0a9e3d2        hello-world         "/hello"                 34 seconds ago      Exited (0) 12 minutes ago                       stupefied_mcclintock
```

What you see now is a list of all containers that you ran. Notice that the `STATUS` column shows that these containers exited some time ago.

Here is the same output of the `docker container ls -a` command, shown diagrammatically (note that your container IDs and names will be different):

![Docker container instances](/images/ops-basics-instances.svg)

It makes sense to spend some time getting comfortable with the `docker run` commands. To find out more about `run`, use `docker container run --help` to see a list of all flags it supports. As you proceed further, we'll see a few more variants of `docker container run` but feel free to experiment here before proceeding.
