# Cleanup

You can easily remove the whole application by removing the stack:

```bash
docker stack rm bb
```

And you can leave swarm mode to return to a single-server Docker host:

```bash
docker swarm leave --force
```

Thanks for completing the Node.js and SQL Server lab! You've learned how to build and run applications with Docker and Docker Compose, how to achieve high availability with Docker Swarm and how to get your application production ready by adding a proxy and a metrics dashboard.

The [Play with Docker Training site](http://training.play-with-docker.com) is always on, and there are plenty more labs you can try at home.