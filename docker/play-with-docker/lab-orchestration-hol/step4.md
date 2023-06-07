# Step 3.1 - Deploy the application components as Docker services

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

# Section 4: Scale the application

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

# Section 5: Drain a node and reschedule the containers

Your sleep-app has been doing amazing after hitting Reddit and HN. It's now number 1 on the App Store! You have scaled up during the holidays and down during the slow season. Now you are doing maintenance on one of your servers so you will need to gracefully take a server out of the swarm without interrupting service to your customers.

Take a look at the status of your nodes again by running `docker node ls` on **node1**.

```bash
docker node ls
```

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
6dlewb50pj2y66q4zi3egnwbi *  node1   Ready   Active        Leader
ym6sdzrcm08s6ohqmjx9mk3dv    node3   Ready   Active
yu3hbegvwsdpy9esh9t2lr431    node2   Ready   Active
```

You will be taking **node2** out of service for maintenance.

Let's see the containers that you have running on **node2**.

```.term2
docker ps
```

```
CONTAINER ID        IMAGE                                                                            COMMAND             CREATED             STATUS              PORTS               NAMES
4e7ea1154ea4        ubuntu@sha256:dd7808d8792c9841d0b460122f1acf0a2dd1f56404f8d1e56298048885e45535   "sleep infinity"    9 minutes ago       Up 9 minutes                            sleep-app.6.35t0eamu0rueeozz0pj2xaesi
```

You can see that we have one of the slepp-app containers running here (your output might look different though).

Now let's jump back to **node1** (the Swarm manager) and take **node2** out of service. To do that, let's run `docker node ls` again.

```bash
docker node ls
```

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
6dlewb50pj2y66q4zi3egnwbi *  node1   Ready   Active        Leader
ym6sdzrcm08s6ohqmjx9mk3dv    node3   Ready   Active
yu3hbegvwsdpy9esh9t2lr431    node2   Ready   Active
```

We are going to take the **ID** for **node2** and run `docker node update --availability drain yournodeid`. We are using the **node2** host **ID** as input into our `drain` command. Replace yournodeid with the id of **node2**.

```
docker node update --availability drain yournodeid
```

Check the status of the nodes

```bash
docker node ls
```

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
6dlewb50pj2y66q4zi3egnwbi *  node1   Ready   Active        Leader
ym6sdzrcm08s6ohqmjx9mk3dv    node3   Ready   Active
yu3hbegvwsdpy9esh9t2lr431    node2   Ready   Drain
```

Node **node2** is now in the `Drain` state.

Switch back to **node2** and see what is running there by running `docker ps`.

```.term2
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

**node2** does not have any containers running on it.

Lastly, check the service again on **node1** to make sure that the container were rescheduled. You should see all four containers running on the remaining two nodes.

```bash
docker service ps sleep-app
```

```
ID            NAME             IMAGE          NODE     DESIRED STATE  CURRENT STATE           ERROR  PORTS
7k0flfh2wpt1  sleep-app.1      ubuntu:latest  node1  Running        Running 25 minutes ago
wol6bzq7xf0v  sleep-app.2      ubuntu:latest  node3  Running        Running 18 minutes ago
s3548wki7rlk  sleep-app.6      ubuntu:latest  node3  Running        Running 3 minutes ago
35t0eamu0rue   \_ sleep-app.6  ubuntu:latest  node2  Shutdown       Shutdown 3 minutes ago
44s8d59vr4a8  sleep-app.7      ubuntu:latest  node1  Running        Running 18 minutes ago
```

# Cleaning Up

Execute the `docker service rm sleep-app` command on **node1** to remove the service called _myservice_.

```bash
docker service rm sleep-app
```

Execute the `docker ps` command on **node1** to get a list of running containers.

```bash
docker ps
```

```
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
044bea1c2277        ubuntu              "sleep infinity"    17 minutes ago      17 minutes ag                           distracted_mayer
```

You can use the `docker kill <CONTAINER ID>` command on **node1** to kill the sleep container we started at the beginning.

```
docker kill yourcontainerid
```

Finally, let's remove node1, node2, and node3 from the Swarm. We can use the `docker swarm leave --force` command to do that.

Lets run `docker swarm leave --force` on **node1**.

```bash
docker swarm leave --force
```

Then, run `docker swarm leave --force` on **node2**.

```.term2
docker swarm leave --force
```

Finally, run `docker swarm leave --force` on **node3**.

```.term3
docker swarm leave --force
```

Congratulations! You've completed this lab. You now know how to build a swarm, deploy applications as collections of services, and scale individual services up and down.