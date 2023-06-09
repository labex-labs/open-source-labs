# Switch to high availability in swarm mode

Swarm mode lets you join several Docker servers together and treat them as a single unit. You deploy your app as services to the swarm, and Docker runs containers across all the servers.

You can run multiple instances of a container to deal with scale, and if a server goes down and you lose containers, Docker starts replacement containers on other servers.

First clear down all the containers from part 2:

```bash
docker container rm --force $(docker container ls --quiet)
```

Now switch to swarm mode:

```bash
docker swarm init --advertise-addr $(hostname -i)
```

This creates a single-node swarm. The output of the command shows you how to join other Docker servers to the swarm - all you need are more servers running Docker in the same network. You can scale Docker swarm up to hundreds of nodes.

The normal `docker` commands still work in swarm mode. Switch to the v3 source code branch:

```bash
git checkout v3
```

And build the application with Docker Compose:

```bash
docker-compose build
```

Version 3 has the same source code, but the [Dockerfile for v3](https://github.com/dockersamples/node-bulletin-board/blob/v3/bulletin-board-app/Dockerfile) of the the web app includes a `HEALTHCHECK` instruction. That tells Docker how to test if the application is healthy, and unhealthy containers are stopped and replaced with new ones.

You use the same Docker Compose file format to deploy in swarm mode, and there are some additional options available. Deploy version 3 of the app using the [docker-stack.yml](https://github.com/dockersamples/node-bulletin-board/blob/v3/docker-stack.yml) file:

```bash
docker stack deploy -c docker-stack.yml bb
```

A stack is a way to group many services together, so you can manage them as one unit. You can see the services in the stack, which tells you if the application is up:

```bash
docker stack services bb
```

[Click here for v3 of the app](/){:data-term=".term1"}{:data-port="8080"}

You'll see the application behaviour is exactly the same - containers are running from the same Docker images, but now they're being scheduled by Docker swarm.

Docker swarm also supports rolling updates for applications running as stacks. In the next part you'll add more functionality to the app, by running a web proxy.
