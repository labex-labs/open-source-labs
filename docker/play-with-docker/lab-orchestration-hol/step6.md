# Drain a node and reschedule the containers

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
