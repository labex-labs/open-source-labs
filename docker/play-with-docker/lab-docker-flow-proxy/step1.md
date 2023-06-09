# Predictive Load-balancing name using Docker Flow Proxy

Docker Flow Proxy is composed on two parts :

- [swarm-listener](https://github.com/vfarcic/docker-flow-swarm-listener)
- [Docker Flow: Proxy](https://github.com/vfarcic/docker-flow-proxy)

The purpose of `swarm-listener` is to monitore swarm services (add, remove, scale..) and to send requests to the proxy whenever a service is created or destroyed.
It must be running on a `Swarm Manager` and will queries Docker API in search for newly created services.

It uses docker **service's labels** (`com.df.*`) to define the metadata and rules for dynamically configure routing rules of the Proxy.

## First we will enable the Swarm mode

> In this tutorial, we will only use a 2 node swarm cluster, but it will work exactly the same way with more nodes!

```bash
docker swarm init --advertise-addr=$(hostname -i)
docker swarm join-token manager
```

> Copy the join command output and paste it in the other terminal to form a 2 node swarm cluster.
