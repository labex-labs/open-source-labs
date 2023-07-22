# Join Worker nodes to the Swarm

You will perform the following procedure on **node2** and **node3**. Towards the end of the procedure you will switch back to **node1**.

Now, take the entire `docker swarm join ...` command we copied earlier from `node1` where it was displayed as terminal output. We need to paste the copied command into the terminal of **node2** and **node3**.

It should look something like this for **node2**. By the way, if the `docker swarm join ...` command scrolled off your screen already, you can run the `docker swarm join-token worker` command on the Manager node to get it again.

> Remember, the tokens displayed here are not the actual tokens you will use. Copy the command from the output on **node1**. On **node2** and **node3** it should look like this:

```
docker swarm join \
    --token SWMTKN-1-1wxyoueqgpcrc4xk2t3ec7n1poy75g4kowmwz64p7ulqx611ih-68pazn0mj8p4p4lnuf4ctp8xy \
    10.0.0.5:2377
```

```
docker swarm join \
    --token SWMTKN-1-1wxyoueqgpcrc4xk2t3ec7n1poy75g4kowmwz64p7ulqx611ih-68pazn0mj8p4p4lnuf4ctp8xy \
    10.0.0.5:2377
```

Once you have run this on **node2** and **node3**, switch back to **node1**, and run a `docker node ls` to verify that both nodes are part of the Swarm. You should see three nodes, **node1** as the Manager node and **node2** and **node3** both as Worker nodes.

```bash
docker node ls
```

```
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
6dlewb50pj2y66q4zi3egnwbi *  node1   Ready   Active        Leader
ym6sdzrcm08s6ohqmjx9mk3dv    node3   Ready   Active
yu3hbegvwsdpy9esh9t2lr431    node2   Ready   Active
```

The `docker node ls` command shows you all of the nodes that are in the swarm as well as their roles in the swarm. The `*` identifies the node that you are issuing the command from.

Congratulations! You have configured a swarm with one manager node and two worker nodes.
