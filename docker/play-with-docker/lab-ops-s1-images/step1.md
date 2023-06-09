# Image creation from a container

Let's start by running an interactive shell in a ubuntu container:

```bash
docker container run -ti ubuntu bash
```

As you know from earlier labs, you just grabbed the image called "ubuntu" from Docker Store and are now running the bash shell inside that container.[^1]

To customize things a little bit we will install a package called [figlet](http://www.figlet.org "make large letters out of ordinary text") in this container. Your container should still be running so type the following commands at your ubuntu container command line:

```bash
apt-get update
apt-get install -y figlet
figlet "hello docker"
```

You should see the words "hello docker" printed out in large ascii characters on the screen. Go ahead and exit from this container

```bash
exit
```

Now let us pretend this new figlet application is quite useful and you want to share it with the rest of your team. You _could_ tell them to do exactly what you did above and install figlet in to their own container, which is simple enough in this example. But if this was a real world application where you had just installed several packages and run through a number of configuration steps the process could get cumbersome and become quite error prone. Instead, it would be easier to create an _image_ you can share with your team.

To start, we need to get the ID of this container using the ls command (do not forget the -a option as the non running container are not returned by the ls command).

```bash
docker container ls -a
```

Before we create our own image, we might want to inspect all the changes we made. Try typing the command `docker container diff <container ID>` for the container you just created. You should see a list of all the files that were added to or changed in the container when you installed figlet. Docker keeps track of all of this information for us. This is part of the _layer_ concept we will explore in a few minutes.

Now, to create an image we need to "commit" this container. Commit creates an image locally on the system running the Docker engine. Run the following command, using the container ID you retrieved, in order to commit the container and create an image out of it.

```
docker container commit CONTAINER_ID
```

That's it - you have created your first image! Once it has been commited, we can see the newly created image in the list of available images.

```bash
docker image ls
```

You should see something like this:

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
<none>              <none>              a104f9ae9c37        46 seconds ago      160MB
ubuntu              latest              14f60031763d        4 days ago          120MB
```

Note that the image we pulled down in the first step (ubuntu) is listed here along with our own custom image. Except our custom image has no information in the REPOSITORY or TAG columns, which would make it tough to identify exactly what was in this container if we wanted to share amongst multiple team members.

Adding this information to an image is known as _tagging_ an image. From the previous command, get the ID of the newly created image and tag it so it's named **ourfiglet**:

```
docker image tag <IMAGE_ID> ourfiglet
docker image ls
```

Now we have the more friendly name "ourfiglet" that we can use to identify our image.

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ourfiglet           latest              a104f9ae9c37        5 minutes ago       160MB
ubuntu              latest              14f60031763d        4 days ago          120MB
```

Here is a graphical view of what we just completed:
![commit container to image](/images/ops-images-commit.svg)

Now we will run a container based on the newly created _ourfiglet_ image:

```bash
docker container run ourfiglet figlet hello
```

As the figlet package is present in our _ourfiglet_ image, the command returns the following output:

```
 _          _ _
| |__   ___| | | ___
| '_ \ / _ \ | |/ _ \
| | | |  __/ | | (_) |
|_| |_|\___|_|_|\___/

```

This example shows that we can create a container, add all the libraries and binaries in it and then commit it in order to create an image. We can then use that image just as we would for images pulled down from the Docker Store. We still have a slight issue in that our image is only stored locally. To share the image we would want to _push_ the image to a registry somewhere. This is beyond the scope of this lab (and you should not enter any personal login information in these labs) but you can get a free Docker ID, run these labs, and push to the [Docker Community Hub](https://hub.docker.com/) from your own system using [Docker for Windows](https://www.docker.com/docker-windows) or [Docker for Mac](https://www.docker.com/docker-mac) if you want to try this out.

As mentioned above, this approach of manually installing software in a container and then committing it to a custom image is just one way to create an image. It works fine and is quite common. However, there is a more powerful way to create images. In the following exercise we will see how images are created using a _Dockerfile_, which is a text file that contains all the instructions to build an image.
