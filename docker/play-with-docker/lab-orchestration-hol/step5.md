# Scale the application

Demand is crazy! Everybody loves your `sleep` app! It's time to scale out.

One of the great things about _services_ is that you can scale them up and down to meet demand. In this step you'll scale the service up and then back down.

You will perform the following procedure from **node1**.

Scale the number of containers in the **sleep-app** service to 7 with the `docker service update --replicas 7 sleep-app` command. `replicas` is the term we use to describe identical containers providing the same service.

```bash
docker service update --replicas 7 sleep-app
```

The Swarm manager schedules so that there are 7 `sleep-app` containers in the cluster. These will be scheduled evenly across the Swarm members.

We are going to use the `docker service ps sleep-app` command. If you do this quick enough after using the `--replicas` option you can see the containers come up in real time.

```bash
docker service ps sleep-app
```

```
ID            NAME         IMAGE          NODE     DESIRED STATE  CURRENT STATE          ERROR  PORTS
7k0flfh2wpt1  sleep-app.1  ubuntu:latest  node1  Running        Running 9 minutes ago
wol6bzq7xf0v  sleep-app.2  ubuntu:latest  node3  Running        Running 2 minutes ago
id50tzzk1qbm  sleep-app.3  ubuntu:latest  node2  Running        Running 2 minutes ago
ozj2itmio16q  sleep-app.4  ubuntu:latest  node3  Running        Running 2 minutes ago
o4rk5aiely2o  sleep-app.5  ubuntu:latest  node2  Running        Running 2 minutes ago
35t0eamu0rue  sleep-app.6  ubuntu:latest  node2  Running        Running 2 minutes ago
44s8d59vr4a8  sleep-app.7  ubuntu:latest  node1  Running        Running 2 minutes ago
```

Notice that there are now 7 containers listed. It may take a few seconds for the new containers in the service to all show as **RUNNING**. The `NODE` column tells us on which node a container is running.

Scale the service back down to just four containers with the `docker service update --replicas 4 sleep-app` command.

```bash
docker service update --replicas 4 sleep-app
```

Verify that the number of containers has been reduced to 4 using the `docker service ps sleep-app` command.

```bash
docker service ps sleep-app
```

```
ID            NAME         IMAGE          NODE     DESIRED STATE  CURRENT STATE           ERROR  PORTS
7k0flfh2wpt1  sleep-app.1  ubuntu:latest  node1  Running        Running 13 minutes ago
wol6bzq7xf0v  sleep-app.2  ubuntu:latest  node3  Running        Running 5 minutes ago
35t0eamu0rue  sleep-app.6  ubuntu:latest  node2  Running        Running 5 minutes ago
44s8d59vr4a8  sleep-app.7  ubuntu:latest  node1  Running        Running 5 minutes ago
```

You have successfully scaled a swarm service up and down.
