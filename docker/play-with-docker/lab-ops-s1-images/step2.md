# Image creation using a Dockerfile

Instead of creating a static binary image, we can use a file called a _Dockerfile_ to create an image. The final result is essentially the same, but with a Dockerfile we are supplying the instructions for building the image, rather than just the raw binary files. This is useful because it becomes much easier to manage changes, especially as your images get bigger and more complex.

For example, if a new version of figlet is released we would either have to re-create our image from scratch, or run our image and upgrade the installed version of figlet. In contrast, a Dockerfile would include the `apt-get` commands we used to install figlet so that we - or anybody using the Dockerfile - could simply recompose the image using those instructions.

It is kind of like the old adage:

> _Give a sysadmin an image and their app will be up-to-date for a day, give a sysadmin a Dockerfile and their app will always be up-to-date_.

Ok, maybe that's a bit of a stretch but Dockerfiles are powerful because they allow us to manage _how_ an image is built, rather than just managing binaries. In practice, Dockerfiles can be managed the same way you might manage source code: they are simply text files so almost any version control system can be used to manage Dockerfiles over time.

We will use a simple example in this section and build a "hello world" application in Node.js. Do not be concerned if you are not familiar with Node.js: Docker (and this exercise) does not require you to know all these details.

We will start by creating a file in which we retrieve the hostname and display it.
NOTE: You should be at the Docker host's command line (`$`). If you see a command line that looks similar to `root@abcd1234567:/#` then you are probably still inside your ubuntu container from the previous exercise. Type `exit` to return to the host command line.

Type the following content into a file named _index.js_. You can use vi, vim or several other Linux editors in this exercise. If you need assistance with the Linux editor commands to do this follow this footnote[^2].

```
var os = require("os");
var hostname = os.hostname();
console.log("hello from " + hostname);
```

The file we just created is the javascript code for our server. As you can probably guess, Node.js will simply print out a "hello" message. We will Docker-ize this application by creating a Dockerfile. We will use **alpine** as the base OS image, add a Node.js runtime and then copy our source code in to the container. We will also specify the default command to be run upon container creation.

Create a file named _Dockerfile_ and copy the following content into it. Again, help creating this file with Linux editors is here [^3].

```dockerfile
FROM alpine
RUN apk update && apk add nodejs
COPY . /app
WORKDIR /app
CMD ["node","index.js"]
```

Let's build our first image out of this Dockerfile and name it _hello:v0.1_:

```bash
docker image build -t hello:v0.1 .
```

This is what you just completed:
![build container from dockerfile](/images/ops-images-dockerfile.svg)

We then start a container to check that our applications runs correctly:

```bash
docker container run hello:v0.1
```

You should then have an output similar to the following one (the ID will be different though).

```
hello from 92d79b6de29f
```

**What just happened?**
We created two files: our application code (index.js) is a simple bit of javascript code that prints out a message. And the Dockerfile is the instructions for Docker engine to create our custom container. This Dockerfile does the following:

1. Specifies a base image to pull **FROM** - the _alpine_ image we used in earlier labs.
2. Then it **RUN**s two commands (_apk update_ and _apk add_) inside that container which installs the Node.js server.
3. Then we told it to **COPY** files from our working directory in to the container. The only file we have right now is our _index.js_.
4. Next we specify the **WORKDIR** - the directory the container should use when it starts up
5. And finally, we gave our container a command (**CMD**) to run when the container starts.

Recall that in previous labs we put commands like `echo "hello world"` on the command line. With a Dockerfile we can specify precise commands to run for everyone who uses this container. Other users do not have to build the container themselves once you push your container up to a repository (which we will cover later) or even know what commands are used. The _Dockerfile_ allows us to specify _how_ to build a container so that we can repeat those steps precisely everytime and we can specify _what_ the container should do when it runs. There are actually multiple methods for specifying the commands and accepting parameters a container will use, but for now it is enough to know that you have the tools to create some pretty powerful containers.
