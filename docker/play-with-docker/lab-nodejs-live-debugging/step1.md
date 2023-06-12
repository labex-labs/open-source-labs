# Getting Started

The first thing to notice is that you don't actually need to have Node.js installed on your machine. You can just use Docker and your IDE. In this case we're going to show you how to use Visual Studio Code.

We've created a simple application which includes an error. You can see the app in the [app/ directory](https://github.com/docker/labs/tree/master/developer-tools/nodejs-debugging/app) of this repository. You can either clone this repository, or create the files yourself. Make sure they're all in the same directory. You will need the following files:

- app.js
- package.json
- index.html
- Dockerfile
- docker-compose.yml

`app.js` defines a simple node app. It serves up `index.html`, refreshing every 2 seconds with quote from an array. Here's what it looks like:

![Image of Browser with quotations from app](../images/browser-broken.gif "Image of a green background with quotes cycling through. Last image is just two quotation marks")

Let's take a look at the `Dockerfile`:

```dockerfile
FROM node:5.11.0-slim

WORKDIR /code

RUN npm install -g nodemon

COPY package.json /code/package.json
RUN npm install && npm ls
RUN mv /code/node_modules /node_modules

COPY . /code

CMD ["npm", "start"]
```

As you can see it installs [nodemon](http://nodemon.io/), a utility that will monitor for any changes in your source and automatically restart your server.

You'll start the app with the `docker-compose.yml`

```
version: "3"

services:
  web:
    build: .
    command: nodemon --debug=5858
    volumes:
      - .:/code
    ports:
      - "8000:8000"
      - "5858:5858"
```

A few things are going on here:

- It defines a service called “web”, which uses the image built from the Dockerfile in the current directory.
- It overrides the command specified in the Dockerfile to enable the remote debugging feature built into Node.js. We do that here because when you ship this application’s container image to production, you don’t want the debugger enabled – it’s a development-only override.
- It overwrites the application code in the container by mounting the current directory as a volume. This means that the code inside the running container will update whenever you update the local files on your hard drive. This is very useful, as it means you don’t have to rebuild the image every time you make a change to the application.
- It maps port 8000 inside the container to port 8000 on localhost, so you can actually visit the application.
- Finally, it maps port 5858 inside the container to the same port on localhost, so you can connect to the remote debugger.
