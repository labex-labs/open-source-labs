# Cleaning Up

Hopefully you were able to learn a little about how Docker Networking works during this lab. Lets clean up the service we created, the containers we started, and finally disable Swarm mode.

Execute the `docker service rm myservice` command to remove the service called _myservice_.

```.term1
docker service rm myservice
```

Execute the `docker ps` command to get a list of running containers.

```.term1
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                           NAMES
846af8479944        ubuntu              "sleep infinity"         17 minutes ago      Up 17 minutes                                       heuristic_boyd
4e0da45b0f16        nginx               "nginx -g 'daemon ..."   12 minutes ago      Up 12 minutes       443/tcp, 0.0.0.0:8080->80/tcp   web1
```

You can use the `docker kill <CONTAINER ID ...>` command to kill the ubunut and nginx containers we started at the beginning.

```
docker kill yourcontainerid1 yourcontainerid2
```

Finally, lets remove node1 and node2 from the Swarm. We can use the `docker swarm leave --force` command to do that.

Lets run `docker swarm leave --force` on node1.

```.term1
docker swarm leave --force
```

Lets also run `docker swarm leave --force` on node2.

```.term2
docker swarm leave --force
```

Congratulations! You've completed this lab!
