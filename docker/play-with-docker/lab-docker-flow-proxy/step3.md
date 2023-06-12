# Launch the Docker Containers

```bash
docker stack deploy proxy --compose-file proxy.yml
```

The proxy container is configured to listen on port 80 and 443 for the standard HTTP traffic, and will listen privately on the internal network on port 8080 for the reconfiguration API requests.

## Check docker networks

```bash
docker network ls
```

You should see that a network named **proxy_public** has been created with Driver **overlay**.

Later If we want others containers to be able to be accessible through the proxy load balancer we will need to **attached them** to this network.

## See Your Docker Swarm Stack

List all your deployed stacks, and view detailed on a specific stack

```bash
docker stack ls
docker stack ps proxy
```

We must have 2 Proxy Running and 1 swarm-listener Running

> Since we have set 2 replicas for the `proxy` service it will be deployed on both nodes while `swarm-listener` must be on one manager node

## View logs of our Proxy service

```bash
docker service logs --tail=10 proxy_proxy
```

View logs of our swarm-listener service

```bash
docker service logs --tail=10 proxy_swarm-listener
```

## Scaling the Proxy service

Normally, creating a new instance of the proxy service, means that it will starts without any state, as a result, the new instances would not have any knowledge of our already deployed services.
Fortunately docker-flow provides an environment variable `LISTEN_ADDRESS=swarm-listener` which tells the proxy the adress of the `swarm-listener` to resend notifications for all the services. As a result, each proxy instance will soon have the same state as the other.
