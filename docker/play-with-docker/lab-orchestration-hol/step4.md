# Deploy applications across multiple hosts

Now that you have a swarm up and running, it is time to deploy our really simple sleep application.

You will perform the following procedure from **node1**.

## Deploy the application components as Docker services

Our `sleep` application is becoming very popular on the internet (due to hitting Reddit and HN). People just love it. So, you are going to have to scale your application to meet peak demand. You will have to do this across multiple hosts for high availability too. We will use the concept of _Services_ to scale our application easily and manage many containers as a single entity.

> _Services_ were a new concept in Docker 1.12. They work with swarms and are intended for long-running containers.

You will perform this procedure from **node1**.

Let's deploy `sleep` as a _Service_ across our Docker Swarm.

```bash
docker service create --name sleep-app ubuntu sleep infinity
```

```
of5rxsxsmm3asx53dqcq0o29c
```

Verify that the `service create` has been received by the Swarm manager.

```bash
docker service ls
```

```
ID            NAME       MODE        REPLICAS  IMAGE
of5rxsxsmm3a  sleep-app  replicated  1/1       ubuntu:latest
```

The state of the service may change a couple times until it is running. The image is being downloaded from Docker Store to the other engines in the Swarm. Once the image is downloaded the container goes into a running state on one of the three nodes.

At this point it may not seem that we have done anything very differently than just running a `docker run ...`. We have again deployed a single container on a single host. The difference here is that the container has been scheduled on a swarm cluster.

Well done. You have deployed the sleep-app to your new Swarm using Docker services.
