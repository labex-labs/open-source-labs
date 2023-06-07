# show members of the swarm

```bash
docker node ls
```

If you correctly execute, the above command, you must see 2 nodes:

```

$ docker node ls
ID                           HOSTNAME  STATUS  AVAILABILITY  MANAGER STATUS
7p167ggf1wi3ox52z8ga2myu6 *  node1     Ready   Active        Leader
og1irjjh2fjtwt7dko7ht0qnq    node2     Ready   Active        Reachable
```

### Create Docker Flow Proxy Docker Containers

We will start by creating a Docker Compose file named proxy.yml, which will defines our 2 services `proxy` and `swarm-listener` of our Docker Flow Proxy stack :

> You can Click on the grey box to automatically copy the content on the terminal (don't mess with the order of commands ;) )

```bash
cat <<EOF > proxy.yml
version: "3"

services:


  proxy:
    image: vfarcic/docker-flow-proxy
    ports:
      - "80:80"
      - "443:443"
      - "8080:8080"
    environment:
      - LISTENER_ADDRESS=swarm-listener
      - MODE=swarm
    networks:
      - public
    deploy:
      replicas: 2
      restart_policy:
        condition: on-failure


  swarm-listener:
    image: vfarcic/docker-flow-swarm-listener
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - public
    environment:
      - DF_NOTIFY_CREATE_SERVICE_URL=http://proxy:8080/v1/docker-flow-proxy/reconfigure
      - DF_NOTIFY_REMOVE_SERVICE_URL=http://proxy:8080/v1/docker-flow-proxy/remove
    deploy:
      replicas: 1
      placement:
        constraints: [node.role == manager]
      restart_policy:
        condition: on-failure

networks:
  public:
    driver: overlay
    ipam:
      driver: default
      config:
      - subnet: 10.1.0.0/24

EOF
```

- We are using version 3 of compose file (mandatory for docker stack deploy)
- We are using image from vfarcic on docker Hub
- Docker will create an overlay networks named **public**, on which will will add each container we want to publish
- We uses constraints to deploy the swarm-listener service on a swarm manager (as it needs to listen to swarm events)
- We gives the proxy service the address of the swarm-listener
- We gives the swarm-listener 2 API endpoint to reconfigure the Proxy through environment variables.
- `DF_NOTIFY_*` environments variables defines the url of the Proxy API for reconfiguration.

### Launch the Docker Containers

```bash
docker stack deploy proxy --compose-file proxy.yml
```

The proxy container is configured to listen on port 80 and 443 for the standard HTTP traffic, and will listen privately on the internal network on port 8080 for the reconfiguration API requests.

### Check docker networks

```bash
docker network ls
```

You should see that a network named **proxy_public** has been created with Driver **overlay**.

Later If we want others containers to be able to be accessible through the proxy load balancer we will need to **attached them** to this network.

### See Your Docker Swarm Stack

List all your deployed stacks, and view detailed on a specific stack

```bash
docker stack ls
docker stack ps proxy
```

We must have 2 Proxy Running and 1 swarm-listener Running

> Since we have set 2 replicas for the `proxy` service it will be deployed on both nodes while `swarm-listener` must be on one manager node

### View logs of our Proxy service

```bash
docker service logs --tail=10 proxy_proxy
```

View logs of our swarm-listener service

```bash
docker service logs --tail=10 proxy_swarm-listener
```

#### Scaling the Proxy service

Normally, creating a new instance of the proxy service, means that it will starts without any state, as a result, the new instances would not have any knowledge of our already deployed services.
Fortunately docker-flow provides an environment variable `LISTEN_ADDRESS=swarm-listener` which tells the proxy the adress of the `swarm-listener` to resend notifications for all the services. As a result, each proxy instance will soon have the same state as the other :)

### Deploy our first service and connect it to the Docker Flow Proxy

The **swarm-listener** service is listening to **docker swarm events** informations, and will reconfigure the **proxy** service based on the service's metadatas, we need to configure thoses metadata as docker service labels:

#### Configure service with routing based on URL Path

We can set a label to inform the proxy to route the traffic according to the target service URI Path using `com.df.*` rules labels:

```bash
cat <<EOF > http.yml
version: "3"

services:
  http:
    image: emilevauge/whoami
    networks:
      - proxy_public
    deploy:
      replicas: 3
      labels:
        - com.df.notify=true
        - com.df.distribute=true
        - com.df.servicePath=/http/
        - com.df.reqPathSearch=/http/
        - com.df.reqPathReplace=/renamed/
        - com.df.port=80

networks:
  proxy_public:
    external: true

EOF
```

> !!Note: Because we are working with Docker Swarm Mode, labels must be set at the **service** level in the **deploy** section, instead of at **container** level!!

- The `notify` label ask `swarm-listener` to re-configure `Flow Proxy`
- The `distribute` label means that reconfiguration should be applied to all Proxy instances.

> We are using Docker 1.13 networking features (routing mesh, and VIP) So that Docker takes care of load balancing on all instances of our service, and so that there is no need to reconfigure the proxy every time a new instance is deployed. (We configure our docker's VIP service IP adress in the proxy, so 1 IP per service)

#### launch the container

```bash
docker stack deploy http --compose-file http.yml
```

The proxy container should have been attached the **proxy_public** network, which we can verify by inspecting the network:

```bash
docker network inspect proxy_public
```

#### check Service status

```bash
docker stack ps http
```

#### Request the service

> We have defined that our service will be receive the request if an incoming request starts with the path `/http`. This was done using the rule in the service's `com.df.servicePath=/http` label

We may now be able to reach our service from any host :
from node1

```bash
curl http://localhost/http/
```

from node2

```.term2
curl http://localhost/http/
```

We should see a response that was generated by the service. The Url on the service site may have been rewritten (see the `/rewrited/` in the GET parameter)

You can request the service in your Browser:

- [Link to http service](/http/){:data-term=".term1"}{:data-port="80"}

You can request the logs of the Proxy Load Balancer:

```.term2
docker service logs --tail=10 -f proxy_proxy
```

You can request the logs of the application

```bash
docker service logs --tail=10 http_http
```

### Scaling Service

Swarm is continuously monitoring containers health. If one of them fails, it will redeployed to one of available nodes. If a whole node fails, or if we ask to drain all containers out of a node for maintenance, Swarm will recreate all the containers that were running on that node.
In production we need to reach zero down time, and so to guarentee our nodes will be available, we need to scale our services, so that we have many instances of our service running on severals nodes. That way, while we are waiting for one instance to recuperate from a failure, others can take over the load.

We can use docker swarm to scale the services of our applications: Exemple, scale our http service to use 5 instances:

```bash
docker service scale http_http=5
```

Check that you have 5 instances of the service :

```bash
docker service ps http_http
```

You can make local calls to the http service and see the loadbalancing :

```bash
curl http://localhost/http/
```

On every request, it's a different docker container that will respond!

### Retrieve Proxy Configuration

If we have activated the admin port (8080), then we can request the proxy to retrieve the configuration
Docker Flow Proxy is base on HAProxy so what we retrieve here is the HAProxy configuration

```bash
curl http://localhost:8080/v1/docker-flow-proxy/config
```
