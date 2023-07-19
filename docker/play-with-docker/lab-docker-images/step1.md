# Image creation from a container

Let's start by running an interactive shell in a ubuntu container.

```bash
docker container run -ti ubuntu bash
```

As we've done in the previous lab, we will install the figlet package in this container.

```bash
apt-get update
apt-get install -y figlet
```

We then exit from this container

```bash
exit
```

Get the ID of this container using the ls command (do not forget the -a option as the non running container are not returned by the ls command).

```bash
docker container ls -a
```

Run the following command, using the ID retreived, in order to commit the container and create an image out of it.

```
docker container commit CONTAINER_ID
```

Once it has been commited, we can see the newly created image in the list of available images.

```bash
docker image ls
```

From the previous command, get the ID of the newly created image and tag it so it's named **ourfiglet**.

```
docker image tag IMAGE_ID ourfiglet
```

Now we will run a container based on the newly created image named **ourfiglet**, and specify the command to be ran such as it uses the figlet package.

```bash
docker container run ourfiglet figlet hello
```

As figlet is present in our **ourfiglet** image, the command ran returns the following output.

```
 _          _ _
| |__   ___| | | ___
| '_ \ / _ \ | |/ _ \
| | | |  __/ | | (_) |
|_| |_|\___|_|_|\___/

```

This example shows that we can create a container, add all the libraries and binaries in it and then commit this one in order to create an image. We can then use that image as we would do for any other images. This approach is not the recommended one as it is not very portable.

In the following we will see how images are usually created, using a Dockerfile, which is a text file that contains all the instructions to build an image.
