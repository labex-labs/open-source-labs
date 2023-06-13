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

## Create Docker Flow Proxy Docker Containers

We will start by creating a Docker Compose file named proxy.yml, which will defines our 2 services `proxy` and `swarm-listener` of our Docker Flow Proxy stack :

> You can Click on the grey box to automatically copy the content on the terminal (don't mess with the order of commands ;)

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
