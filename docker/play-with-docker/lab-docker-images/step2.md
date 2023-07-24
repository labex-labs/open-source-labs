# Image creation using a Dockerfile

We will use a simple example in this section and build a hello world application in Node.js. We will start by creating a file in which we retrieve the hostname and display it.

Copy the following content into index.js file.

```js
var os = require("os");
var hostname = os.hostname();
console.log("hello from " + hostname);
```

We will dockerrize this application and start by creating a Dockerfile for this purpose. We will use **alpine** as the base image, add a Node.js runtime and then copy our source code. We will also specify the default command to be ran upon container creation.

Create a file named Dockerfile and copy the following content into it.

```dockerfile
FROM alpine
RUN apk update && apk add nodejs
COPY . /app
WORKDIR /app
CMD ["node","index.js"]
```

Let's build our first image out of this Dockerfile, we will name it hello:v0.1

```bash
docker image build -t hello:v0.1 .
```

We then create a container to check it is running fine.

```bash
docker container run hello:v0.1
```

You should then have an output similar to the following one (the ID will be different though).

```
hello from 92d79b6de29f
```

There are always several ways to write a Dockerfile, we can start from a Linux distribution and then install a runtime (as we did above) or use images where this has already been done for us.

To illustrate that, we will now create a new Dockerfile but we will use the **mhart/alpine-node:6.9.4** image. This is not an official image but it's a very well known and used one.

Create a new Dockerfile named Dockerfile-v2 and make sure it has the following content.

```dockerfile
FROM mhart/alpine-node:6.9.4
COPY . /app
WORKDIR /app
CMD ["node","index.js"]
```

Basically, it is not that different from the previous one, it just uses a base image that embeds alpine and a Node.js runtime so we do not have to install it ourself. In this example, installing Node.js is not a big deal, but it is really helpful to use image where a runtime (or else) is already packages when using more complex environments.

We will now create a new image using this Dockerfile.

```bash
docker image build -f Dockerfile-v2 -t hello:v0.2 .
```

Note: as we do not use the default name for our Dockerfile, we use the -f option to point towards the one we need to use.

We now run a container from this image.

```bash
docker container run hello:v0.2
```

Once again, the output will look like the following.

```
hello from 4094ff6bffbd
```
